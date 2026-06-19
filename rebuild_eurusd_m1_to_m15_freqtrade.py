import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd


# ============================================================
# إعدادات ثابتة
# ============================================================

SOURCE_CSV = Path("/home/fayez/AI_Forex_Manual_Signal_Lab/data/EURUSD/EURUSD_M1.csv")
FREQTRADE_DIR = Path("/home/fayez/freqtrade")
CONFIG_PATH = FREQTRADE_DIR / "user_data/config.json"

PAIR = "EUR/USDT"
PAIR_FILENAME = "EUR_USDT"
TIMEFRAME = "15m"
EXCHANGE_NAME = "binance"

OUTPUT_DIR = FREQTRADE_DIR / "user_data" / "data" / EXCHANGE_NAME
OUTPUT_FEATHER = OUTPUT_DIR / f"{PAIR_FILENAME}-{TIMEFRAME}.feather"

TARGET_START = pd.Timestamp("2025-01-01 00:00:00", tz="UTC")
TARGET_END = pd.Timestamp("2026-01-01 00:00:00", tz="UTC")


# ============================================================
# أدوات مساعدة
# ============================================================


def fail(msg: str) -> None:
    print(f"\n❌ خطأ: {msg}")
    sys.exit(1)


def normalize_col(name: str) -> str:
    return str(name).strip().lower().replace(" ", "_").replace("-", "_").replace(".", "_")


def find_column(columns, candidates):
    norm_map = {normalize_col(c): c for c in columns}
    for cand in candidates:
        key = normalize_col(cand)
        if key in norm_map:
            return norm_map[key]
    return None


def read_csv_auto(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, sep=None, engine="python", encoding="utf-8-sig")
    except Exception as e:
        fail(f"فشل قراءة CSV: {e}")


def parse_datetime_column(series: pd.Series) -> pd.Series:
    """
    يقرأ التاريخ ويحافظ عليه بصيغة UTC timezone-aware.
    مهم حتى لا يظهر خطأ:
    can't compare offset-naive and offset-aware datetimes
    """
    s = series.copy()

    dt_text = pd.to_datetime(s, utc=True, errors="coerce")
    text_ratio = dt_text.notna().mean()

    numeric = pd.to_numeric(s, errors="coerce")
    numeric_ratio = numeric.notna().mean()

    dt_num = pd.Series(pd.NaT, index=s.index, dtype="datetime64[ns, UTC]")

    if numeric_ratio > 0.90:
        max_val = numeric.dropna().abs().max()

        if max_val > 1e17:
            unit = "ns"
        elif max_val > 1e14:
            unit = "us"
        elif max_val > 1e11:
            unit = "ms"
        elif max_val > 1e9:
            unit = "s"
        else:
            unit = None

        if unit:
            dt_num = pd.to_datetime(numeric, unit=unit, utc=True, errors="coerce")

    num_ratio = dt_num.notna().mean()

    if text_ratio >= num_ratio:
        return dt_text

    return dt_num


def score_datetime_candidate(name: str, dt: pd.Series) -> dict:
    valid = dt.dropna()
    ratio = len(valid) / len(dt) if len(dt) else 0

    if valid.empty:
        return {
            "name": name,
            "score": -9999,
            "valid_ratio": ratio,
            "start": None,
            "end": None,
            "median_diff": None,
        }

    valid_sorted = valid.sort_values()
    start = valid_sorted.iloc[0]
    end = valid_sorted.iloc[-1]

    diffs = valid_sorted.diff().dropna()
    median_diff = diffs.median() if not diffs.empty else None

    score = 0
    score += ratio * 100

    n = normalize_col(name)

    if n == "datetime":
        score += 80
    elif n in ("date_time", "timestamp", "time", "open_time"):
        score += 40
    elif n == "date":
        score += 5

    if start.year <= 1971 and end.year <= 1971:
        score -= 500

    if 2000 <= start.year <= 2035 and 2000 <= end.year <= 2035:
        score += 120

    expected_m1 = pd.Timedelta(minutes=1)

    if median_diff == expected_m1:
        score += 180
    elif median_diff is not None:
        if abs(median_diff - expected_m1) <= pd.Timedelta(seconds=5):
            score += 100
        elif median_diff <= pd.Timedelta(seconds=2):
            score -= 250

    return {
        "name": name,
        "score": score,
        "valid_ratio": ratio,
        "start": start,
        "end": end,
        "median_diff": median_diff,
    }


def choose_best_datetime_column(df: pd.DataFrame):
    candidate_names = [
        "datetime",
        "date_time",
        "timestamp",
        "time",
        "open_time",
        "start_time",
        "date",
        "Date",
        "Datetime",
        "Timestamp",
        "Time",
    ]

    wanted = {normalize_col(x) for x in candidate_names}

    candidates = []
    for col in df.columns:
        if normalize_col(col) in wanted:
            candidates.append(col)

    if not candidates:
        candidates = list(df.columns)

    unique = []
    seen = set()

    for c in candidates:
        if c not in seen:
            unique.append(c)
            seen.add(c)

    scored = []

    for col in unique:
        dt = parse_datetime_column(df[col])
        scored.append(score_datetime_candidate(col, dt))

    scored = sorted(scored, key=lambda x: x["score"], reverse=True)

    if not scored:
        fail("لم أجد أي عمود تاريخ محتمل.")

    print("\n📋 تقييم أعمدة التاريخ:")
    for item in scored:
        print(
            f"- {item['name']} | score={item['score']:.2f} | "
            f"valid={item['valid_ratio']:.2%} | "
            f"start={item['start']} | end={item['end']} | "
            f"median={item['median_diff']}"
        )

    best = scored[0]

    if best["score"] < 0 or best["valid_ratio"] < 0.80:
        fail("لم أستطع اختيار عمود تاريخ موثوق.")

    best_col = best["name"]
    best_dt = parse_datetime_column(df[best_col])

    return best_col, best_dt


# ============================================================
# 1) فحص المسارات
# ============================================================

print("🔎 فحص المسارات...")

if not SOURCE_CSV.exists():
    fail(f"ملف المصدر غير موجود: {SOURCE_CSV}")

if not CONFIG_PATH.exists():
    fail(f"ملف config غير موجود: {CONFIG_PATH}")

print(f"✅ ملف M1 موجود: {SOURCE_CSV}")
print(f"✅ ملف config موجود: {CONFIG_PATH}")


# ============================================================
# 2) قراءة ملف M1
# ============================================================

print("\n📥 قراءة ملف EURUSD M1...")

raw = read_csv_auto(SOURCE_CSV)

if raw.empty:
    fail("ملف CSV فارغ.")

print(f"✅ عدد الصفوف الأصلي: {len(raw):,}")
print(f"✅ الأعمدة الأصلية: {list(raw.columns)}")


# ============================================================
# 3) اختيار عمود التاريخ
# ============================================================

print("\n🕒 اختيار عمود التاريخ الصحيح...")

date_col, parsed_dates = choose_best_datetime_column(raw)

print(f"\n✅ عمود التاريخ المختار: {date_col}")


# ============================================================
# 4) تحديد أعمدة OHLCV
# ============================================================

open_col = find_column(raw.columns, ["open", "o"])
high_col = find_column(raw.columns, ["high", "h"])
low_col = find_column(raw.columns, ["low", "l"])
close_col = find_column(raw.columns, ["close", "c"])
volume_col = find_column(raw.columns, ["volume", "vol", "tick_volume", "tickvol", "real_volume"])

missing = []

if open_col is None:
    missing.append("open")
if high_col is None:
    missing.append("high")
if low_col is None:
    missing.append("low")
if close_col is None:
    missing.append("close")

if missing:
    fail(f"الأعمدة السعرية الناقصة: {missing}")

if volume_col is None:
    print("⚠️ لم أجد volume. سيتم إنشاء volume = 1.0")
else:
    print(f"✅ عمود volume المختار: {volume_col}")


# ============================================================
# 5) بناء بيانات M1 نظيفة
# ============================================================

print("\n🧱 تجهيز بيانات M1...")

df_m1 = pd.DataFrame()
df_m1["date"] = parsed_dates
df_m1["open"] = pd.to_numeric(raw[open_col], errors="coerce")
df_m1["high"] = pd.to_numeric(raw[high_col], errors="coerce")
df_m1["low"] = pd.to_numeric(raw[low_col], errors="coerce")
df_m1["close"] = pd.to_numeric(raw[close_col], errors="coerce")

if volume_col is not None:
    df_m1["volume"] = pd.to_numeric(raw[volume_col], errors="coerce").fillna(0)
else:
    df_m1["volume"] = 1.0

before = len(df_m1)

df_m1 = df_m1.dropna(subset=["date", "open", "high", "low", "close"])
df_m1 = df_m1.sort_values("date")
df_m1 = df_m1.drop_duplicates(subset=["date"], keep="last")
df_m1 = df_m1.reset_index(drop=True)

after = len(df_m1)

if df_m1.empty:
    fail("بعد تنظيف M1 لم يبقَ أي صف صالح.")

print(f"✅ صفوف M1 بعد التنظيف: {after:,}")
print(f"ℹ️ تم حذف/استبعاد: {before - after:,} صف")

start_m1 = df_m1["date"].min()
end_m1 = df_m1["date"].max()

print(f"✅ بداية M1: {start_m1}")
print(f"✅ نهاية M1: {end_m1}")

if start_m1.year <= 1971 and end_m1.year <= 1971:
    fail("التاريخ ما زال في 1970. عمود التاريخ غير صحيح.")

diffs_m1 = df_m1["date"].diff().dropna()
if not diffs_m1.empty:
    median_m1 = diffs_m1.median()
    print(f"✅ الفاصل الزمني الوسيط M1: {median_m1}")


# ============================================================
# 6) تحويل M1 إلى M15
# ============================================================

print("\n🔁 تحويل M1 إلى M15...")

df_m1 = df_m1.set_index("date")

df_m15 = df_m1.resample("15min", label="left", closed="left").agg(
    {
        "open": "first",
        "high": "max",
        "low": "min",
        "close": "last",
        "volume": "sum",
    }
)

before_m15_drop = len(df_m15)

df_m15 = df_m15.dropna(subset=["open", "high", "low", "close"])
df_m15 = df_m15.reset_index()

after_m15_drop = len(df_m15)

if df_m15.empty:
    fail("بعد تحويل M15 لم يبقَ أي صف صالح.")

print(f"✅ عدد شموع M15: {len(df_m15):,}")
print(f"ℹ️ تم حذف شموع M15 الفارغة: {before_m15_drop - after_m15_drop:,}")

start_m15 = df_m15["date"].min()
end_m15 = df_m15["date"].max()

print(f"✅ بداية M15: {start_m15}")
print(f"✅ نهاية M15: {end_m15}")


# ============================================================
# 7) فحص تغطية الفترة المطلوبة
# ============================================================

print("\n📆 فحص تغطية فترة الاختبار المطلوبة...")

print(f"🎯 الفترة المطلوبة: {TARGET_START} إلى {TARGET_END}")

covers_start = start_m15 <= TARGET_START
covers_end = end_m15 >= TARGET_END

if covers_start:
    print("✅ البيانات تغطي بداية 2025-01-01.")
else:
    print("⚠️ البيانات لا تبدأ قبل 2025-01-01.")

if covers_end:
    print("✅ البيانات تغطي نهاية 2026-01-01.")
else:
    print("⚠️ البيانات لا تصل إلى 2026-01-01.")

pretrain_start = TARGET_START - pd.Timedelta(days=30)

if start_m15 <= pretrain_start:
    print("✅ توجد بيانات تدريب قبل 2025-01-01 تكفي تقريبًا لـ FreqAI train_period_days=30.")
else:
    print("⚠️ لا توجد 30 يوم تدريب قبل 2025-01-01.")
    print("   قد يبدأ التقييم الفعلي بعد أول فترة تدريب، أو نحتاج تخفيف train_period_days.")


# ============================================================
# 8) فحوصات جودة M15
# ============================================================

print("\n🧪 فحص جودة OHLC والزمن في M15...")

bad_ohlc = df_m15[
    (df_m15["high"] < df_m15[["open", "close", "low"]].max(axis=1))
    | (df_m15["low"] > df_m15[["open", "close", "high"]].min(axis=1))
]

if len(bad_ohlc) > 0:
    print(f"⚠️ يوجد {len(bad_ohlc):,} شمعة OHLC غير منطقية.")
else:
    print("✅ فحص OHLC منطقي.")

diffs_m15 = df_m15["date"].diff().dropna()
if not diffs_m15.empty:
    median_m15 = diffs_m15.median()
    expected_m15 = pd.Timedelta(minutes=15)
    print(f"✅ الفاصل الزمني الوسيط M15: {median_m15}")

    gaps = diffs_m15[diffs_m15 > expected_m15]
    print(f"ℹ️ عدد الفجوات الأكبر من 15 دقيقة: {len(gaps):,}")

print(f"✅ نوع عمود التاريخ قبل الحفظ: {df_m15['date'].dtype}")


# ============================================================
# 9) حفظ ملف Freqtrade
# ============================================================

print("\n💾 حفظ بيانات M15 داخل Freqtrade...")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

if OUTPUT_FEATHER.exists():
    backup_feather = OUTPUT_FEATHER.with_suffix(
        OUTPUT_FEATHER.suffix + f".bak_m1_to_m15_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    )
    shutil.copy2(OUTPUT_FEATHER, backup_feather)
    print("✅ نسخة احتياطية من ملف البيانات القديم:")
    print(f"   {backup_feather}")

try:
    df_m15.to_feather(OUTPUT_FEATHER)
except Exception as e:
    fail(f"فشل حفظ feather: {e}")

print("✅ تم حفظ بيانات M15:")
print(f"   {OUTPUT_FEATHER}")


# ============================================================
# 10) تحقق بعد الحفظ
# ============================================================

print("\n🔁 تحقق من الملف بعد الحفظ...")

check_df = pd.read_feather(OUTPUT_FEATHER)

print(f"✅ نوع عمود date بعد القراءة: {check_df['date'].dtype}")
print(f"✅ أول تاريخ بعد القراءة: {check_df['date'].min()}")
print(f"✅ آخر تاريخ بعد القراءة: {check_df['date'].max()}")

if "UTC" not in str(check_df["date"].dtype):
    fail("عمود date بعد الحفظ ليس timezone-aware UTC. لن نكمل حتى لا يرجع خطأ FreqAI.")


# ============================================================
# 11) تحديث config.json
# ============================================================

print("\n⚙️ تحديث config.json...")

backup_config = CONFIG_PATH.with_suffix(
    CONFIG_PATH.suffix + f".bak_m1_to_m15_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
)

shutil.copy2(CONFIG_PATH, backup_config)

with CONFIG_PATH.open("r", encoding="utf-8") as f:
    config = json.load(f)

config["timeframe"] = TIMEFRAME
config["trading_mode"] = "spot"
config["margin_mode"] = ""
config["dataformat_ohlcv"] = "feather"

config.setdefault("exchange", {})
config["exchange"]["name"] = EXCHANGE_NAME
config["exchange"].setdefault("key", "")
config["exchange"].setdefault("secret", "")
config["exchange"].setdefault("ccxt_config", {})
config["exchange"].setdefault("ccxt_async_config", {})
config["exchange"]["pair_whitelist"] = [PAIR]
config["exchange"].setdefault("pair_blacklist", ["BNB/.*"])

config["pairlists"] = [{"method": "StaticPairList"}]

if "freqai" in config:
    config["freqai"]["enabled"] = True

with CONFIG_PATH.open("w", encoding="utf-8") as f:
    json.dump(config, f, indent=4, ensure_ascii=False)

print("✅ تم تحديث config.json.")
print("✅ نسخة احتياطية من config:")
print(f"   {backup_config}")


# ============================================================
# 12) ملخص نهائي
# ============================================================

print("\n🎯 الملخص النهائي")
print("=" * 90)
print(f"ملف المصدر M1: {SOURCE_CSV}")
print(f"عمود التاريخ المستخدم: {date_col}")
print(f"الزوج داخل Freqtrade: {PAIR}")
print(f"الفريم الناتج: {TIMEFRAME}")
print(f"شموع M1 بعد التنظيف: {len(df_m1):,}")
print(f"شموع M15 الناتجة: {len(df_m15):,}")
print(f"بداية M15: {check_df['date'].min()}")
print(f"نهاية M15: {check_df['date'].max()}")
print(f"ملف Freqtrade: {OUTPUT_FEATHER}")
print(f"ملف الإعداد: {CONFIG_PATH}")
print("=" * 90)

print("\n✅ انتهى تحويل EURUSD من M1 إلى M15 وتجهيزه لـ Freqtrade/FreqAI.")

print("\nأوامر اختبار مقترحة:")
print("1) اختبار بدون رسوم:")
print(
    "freqtrade backtesting "
    "--config user_data/config.json "
    "--strategy EURUSD_FreqAI_Hybrid "
    "--freqaimodel LightGBMRegressor "
    "--timeframe 15m "
    "--timerange 20250101-20260101 "
    "--fee 0 "
    "-p EUR/USDT"
)

print("\n2) اختبار مع رسوم Freqtrade الافتراضية:")
print(
    "freqtrade backtesting "
    "--config user_data/config.json "
    "--strategy EURUSD_FreqAI_Hybrid "
    "--freqaimodel LightGBMRegressor "
    "--timeframe 15m "
    "--timerange 20250101-20260101 "
    "-p EUR/USDT"
)
