import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd


# ============================================================
# إعدادات ثابتة
# ============================================================

SOURCE_CSV = Path("/home/fayez/AI_Forex_Manual_Signal_Lab/data/EURUSD/M15.csv")
FREQTRADE_DIR = Path("/home/fayez/freqtrade")
CONFIG_PATH = FREQTRADE_DIR / "user_data/config.json"

PAIR = "EUR/USDT"
PAIR_FILENAME = "EUR_USDT"
TIMEFRAME = "15m"
EXCHANGE_NAME = "binance"

OUTPUT_DIR = FREQTRADE_DIR / "user_data" / "data" / EXCHANGE_NAME
OUTPUT_FEATHER = OUTPUT_DIR / f"{PAIR_FILENAME}-{TIMEFRAME}.feather"


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
    يحاول قراءة التاريخ من عمود نصي أو رقمي.
    يحمي من مشكلة اختيار عمود رقمي مثل 0,1,2 وتحويله إلى 1970.
    """
    s = series.copy()

    # محاولة أولى: قراءة كنص تاريخ
    dt_text = pd.to_datetime(s, utc=True, errors="coerce")
    text_ratio = dt_text.notna().mean()

    # محاولة ثانية: قراءة كرقم timestamp
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
            # أرقام صغيرة مثل 0..5605 ليست timestamp حقيقي
            unit = None

        if unit:
            dt_num = pd.to_datetime(numeric, unit=unit, utc=True, errors="coerce")

    num_ratio = dt_num.notna().mean()

    # اختر القراءة الأفضل
    if text_ratio >= num_ratio:
        dt = dt_text
    else:
        dt = dt_num

    # تحويل إلى UTC naive لأن Freqtrade يتعامل جيدًا معها في ملفات OHLCV
    try:
        dt = dt.dt.tz_convert("UTC").dt.tz_localize(None)
    except Exception:
        try:
            dt = dt.dt.tz_localize(None)
        except Exception:
            pass

    return dt


def score_datetime_candidate(name: str, dt: pd.Series) -> dict:
    """
    يعطي درجة لكل عمود تاريخ محتمل.
    الهدف اختيار العمود الذي يعطي:
    - نسبة تواريخ صالحة عالية
    - نطاق زمني منطقي
    - فاصل وسيط قريب من 15 دقيقة
    - ليس محصورًا في 1970
    """
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
            "reason": "لا توجد تواريخ صالحة",
        }

    valid_sorted = valid.sort_values()
    start = valid_sorted.iloc[0]
    end = valid_sorted.iloc[-1]

    diffs = valid_sorted.diff().dropna()
    median_diff = diffs.median() if not diffs.empty else None

    score = 0

    # نسبة الصلاحية
    score += ratio * 100

    # تفضيل الاسم datetime بقوة
    n = normalize_col(name)
    if n == "datetime":
        score += 50
    elif n in ("date_time", "timestamp", "time", "date"):
        score += 20

    # رفض قوي للتواريخ القديمة جدًا الناتجة من أرقام صغيرة
    if start.year <= 1971 and end.year <= 1971:
        score -= 500

    # تفضيل نطاق حديث/منطقي
    if 2000 <= start.year <= 2035 and 2000 <= end.year <= 2035:
        score += 100

    # تفضيل فاصل 15 دقيقة
    expected = pd.Timedelta(minutes=15)
    if median_diff == expected:
        score += 150
    elif median_diff is not None:
        diff_error = abs(median_diff - expected)
        if diff_error <= pd.Timedelta(minutes=1):
            score += 80
        elif median_diff <= pd.Timedelta(seconds=2):
            score -= 200

    return {
        "name": name,
        "score": score,
        "valid_ratio": ratio,
        "start": start,
        "end": end,
        "median_diff": median_diff,
        "reason": "ok",
    }


def choose_best_datetime_column(df: pd.DataFrame) -> tuple[str, pd.Series, list[dict]]:
    """
    يجرّب أعمدة التاريخ المحتملة كلها ثم يختار الأفضل.
    """
    preferred_names = [
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

    candidates = []

    # أضف المرشحين المعروفين أولًا
    for col in df.columns:
        if normalize_col(col) in [normalize_col(x) for x in preferred_names]:
            candidates.append(col)

    # لو ما وجد أي مرشح، جرّب كل الأعمدة
    if not candidates:
        candidates = list(df.columns)

    seen = set()
    unique_candidates = []
    for c in candidates:
        if c not in seen:
            unique_candidates.append(c)
            seen.add(c)

    scored = []

    for col in unique_candidates:
        dt = parse_datetime_column(df[col])
        item = score_datetime_candidate(col, dt)
        scored.append(item)

    scored = sorted(scored, key=lambda x: x["score"], reverse=True)

    if not scored:
        fail("لم أجد أي عمود تاريخ محتمل.")

    best = scored[0]

    if best["score"] < 0 or best["valid_ratio"] < 0.80:
        print("\n📋 تقييم أعمدة التاريخ:")
        for item in scored:
            print(
                f"- {item['name']} | score={item['score']:.2f} | "
                f"valid={item['valid_ratio']:.2%} | "
                f"start={item['start']} | end={item['end']} | "
                f"median={item['median_diff']}"
            )
        fail("لم أستطع اختيار عمود تاريخ موثوق.")

    best_col = best["name"]
    best_dt = parse_datetime_column(df[best_col])

    return best_col, best_dt, scored


# ============================================================
# 1) فحص المسارات
# ============================================================

print("🔎 فحص المسارات...")

if not SOURCE_CSV.exists():
    fail(f"ملف المصدر غير موجود: {SOURCE_CSV}")

if not CONFIG_PATH.exists():
    fail(f"ملف config غير موجود: {CONFIG_PATH}")

print(f"✅ ملف المصدر موجود: {SOURCE_CSV}")
print(f"✅ ملف config موجود: {CONFIG_PATH}")


# ============================================================
# 2) قراءة الملف
# ============================================================

print("\n📥 قراءة ملف EURUSD M15...")

raw = read_csv_auto(SOURCE_CSV)

if raw.empty:
    fail("ملف CSV فارغ.")

print(f"✅ عدد الصفوف الأصلي: {len(raw):,}")
print(f"✅ الأعمدة الأصلية: {list(raw.columns)}")


# ============================================================
# 3) اختيار عمود التاريخ الصحيح
# ============================================================

print("\n🕒 فحص أعمدة التاريخ واختيار الأفضل...")

date_col, parsed_dates, scored_dates = choose_best_datetime_column(raw)

print("📋 تقييم أعمدة التاريخ:")
for item in scored_dates:
    print(
        f"- {item['name']} | score={item['score']:.2f} | "
        f"valid={item['valid_ratio']:.2%} | "
        f"start={item['start']} | end={item['end']} | "
        f"median={item['median_diff']}"
    )

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
# 5) بناء DataFrame بصيغة Freqtrade
# ============================================================

print("\n🧱 تجهيز البيانات بصيغة Freqtrade...")

df = pd.DataFrame()
df["date"] = parsed_dates
df["open"] = pd.to_numeric(raw[open_col], errors="coerce")
df["high"] = pd.to_numeric(raw[high_col], errors="coerce")
df["low"] = pd.to_numeric(raw[low_col], errors="coerce")
df["close"] = pd.to_numeric(raw[close_col], errors="coerce")

if volume_col is not None:
    df["volume"] = pd.to_numeric(raw[volume_col], errors="coerce").fillna(0)
else:
    df["volume"] = 1.0

before = len(df)

df = df.dropna(subset=["date", "open", "high", "low", "close"])
df = df.sort_values("date")
df = df.drop_duplicates(subset=["date"], keep="last")
df = df.reset_index(drop=True)

after = len(df)

if df.empty:
    fail("بعد التنظيف لم يبقَ أي صف صالح.")

print(f"✅ الصفوف بعد التنظيف: {after:,}")
print(f"ℹ️ تم حذف/استبعاد: {before - after:,} صف")


# ============================================================
# 6) فحوصات جودة البيانات
# ============================================================

print("\n🧪 فحص جودة OHLC والزمن...")

bad_ohlc = df[
    (df["high"] < df[["open", "close", "low"]].max(axis=1))
    | (df["low"] > df[["open", "close", "high"]].min(axis=1))
]

if len(bad_ohlc) > 0:
    print(f"⚠️ يوجد {len(bad_ohlc):,} شمعة غير منطقية في OHLC.")
else:
    print("✅ فحص OHLC منطقي.")

start_date = df["date"].min()
end_date = df["date"].max()

print(f"✅ بداية البيانات: {start_date}")
print(f"✅ نهاية البيانات: {end_date}")

if start_date.year <= 1971 and end_date.year <= 1971:
    fail("التاريخ ما زال في 1970. هذا يعني أن عمود التاريخ غير صحيح.")

diffs = df["date"].diff().dropna()

if not diffs.empty:
    median_diff = diffs.median()
    expected = pd.Timedelta(minutes=15)

    print(f"✅ الفاصل الزمني الوسيط: {median_diff}")

    if median_diff == expected:
        print("✅ الفاصل يبدو M15 صحيح.")
    else:
        print(f"⚠️ الفاصل الوسيط ليس 15 دقيقة: {median_diff}")

    gaps = diffs[diffs > expected]
    if len(gaps) > 0:
        print(f"⚠️ يوجد فجوات زمنية أكبر من 15 دقيقة: {len(gaps):,}")
    else:
        print("✅ لا توجد فجوات أكبر من 15 دقيقة.")


# ============================================================
# 7) حفظ ملف Freqtrade
# ============================================================

print("\n💾 حفظ بيانات Freqtrade...")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

try:
    df.to_feather(OUTPUT_FEATHER)
except Exception as e:
    fail(f"فشل حفظ feather: {e}")

print("✅ تم حفظ البيانات هنا:")
print(f"   {OUTPUT_FEATHER}")


# ============================================================
# 8) تعديل config.json
# ============================================================

print("\n⚙️ تعديل user_data/config.json...")

backup_path = CONFIG_PATH.with_suffix(
    CONFIG_PATH.suffix + f".bak_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
)

shutil.copy2(CONFIG_PATH, backup_path)

print("✅ نسخة احتياطية:")
print(f"   {backup_path}")

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

with CONFIG_PATH.open("w", encoding="utf-8") as f:
    json.dump(config, f, indent=4, ensure_ascii=False)

print("✅ تم تعديل config.json بنجاح.")


# ============================================================
# 9) ملخص نهائي
# ============================================================

print("\n🎯 الملخص النهائي")
print("=" * 70)
print(f"عمود التاريخ المستخدم: {date_col}")
print(f"الزوج داخل Freqtrade: {PAIR}")
print(f"الفريم: {TIMEFRAME}")
print(f"عدد الشموع: {len(df):,}")
print(f"من: {start_date}")
print(f"إلى: {end_date}")
print(f"ملف البيانات: {OUTPUT_FEATHER}")
print(f"ملف الإعداد: {CONFIG_PATH}")
print("=" * 70)

print("\n✅ انتهى التجهيز.")
print("\nأمر تجربة الباكتيست:")
print(
    f"freqtrade backtesting --config user_data/config.json --strategy TestStrategy --timeframe {TIMEFRAME} -p {PAIR}"
)
