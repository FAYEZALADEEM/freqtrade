import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd


# =========================
# إعدادات ثابتة
# =========================

SOURCE_CSV = Path("/home/fayez/AI_Forex_Manual_Signal_Lab/data/EURUSD/M15.csv")
FREQTRADE_DIR = Path("/home/fayez/freqtrade")
CONFIG_PATH = FREQTRADE_DIR / "user_data/config.json"

PAIR = "EUR/USDT"
PAIR_FILENAME = "EUR_USDT"
TIMEFRAME = "15m"
EXCHANGE_NAME = "binance"

OUTPUT_DIR = FREQTRADE_DIR / "user_data" / "data" / EXCHANGE_NAME
OUTPUT_FEATHER = OUTPUT_DIR / f"{PAIR_FILENAME}-{TIMEFRAME}.feather"


# =========================
# أدوات مساعدة
# =========================


def fail(msg: str) -> None:
    print(f"\n❌ خطأ: {msg}")
    sys.exit(1)


def normalize_col(name: str) -> str:
    return str(name).strip().lower().replace(" ", "_").replace("-", "_").replace(".", "_")


def find_column(columns, candidates):
    normalized = {normalize_col(c): c for c in columns}
    for cand in candidates:
        key = normalize_col(cand)
        if key in normalized:
            return normalized[key]
    return None


def parse_date_series(series: pd.Series) -> pd.Series:
    """
    يحاول قراءة التاريخ سواء كان:
    - نص تاريخ
    - timestamp بالثواني
    - timestamp بالمللي ثانية
    - timestamp بالمايكرو/نانو ثانية
    """
    s = series.copy()

    # لو العمود رقمي
    numeric = pd.to_numeric(s, errors="coerce")
    numeric_valid_ratio = numeric.notna().mean()

    if numeric_valid_ratio > 0.90:
        max_val = numeric.dropna().abs().max()

        if max_val > 1e17:
            # nanoseconds
            dt = pd.to_datetime(numeric, unit="ns", utc=True, errors="coerce")
        elif max_val > 1e14:
            # microseconds
            dt = pd.to_datetime(numeric, unit="us", utc=True, errors="coerce")
        elif max_val > 1e11:
            # milliseconds
            dt = pd.to_datetime(numeric, unit="ms", utc=True, errors="coerce")
        else:
            # seconds
            dt = pd.to_datetime(numeric, unit="s", utc=True, errors="coerce")
    else:
        dt = pd.to_datetime(s, utc=True, errors="coerce")

    # نحول إلى UTC بدون timezone لتوافق أفضل مع ملفات Freqtrade
    try:
        dt = dt.dt.tz_convert("UTC").dt.tz_localize(None)
    except Exception:
        try:
            dt = dt.dt.tz_localize(None)
        except Exception:
            pass

    return dt


def load_csv_auto(path: Path) -> pd.DataFrame:
    """
    قراءة CSV مع محاولة كشف الفاصل تلقائيًا.
    """
    try:
        return pd.read_csv(path, sep=None, engine="python", encoding="utf-8-sig")
    except Exception as e:
        fail(f"فشل قراءة الملف CSV: {e}")


# =========================
# 1) فحص وجود الملفات
# =========================

print("🔎 فحص المسارات...")

if not SOURCE_CSV.exists():
    fail(f"ملف المصدر غير موجود: {SOURCE_CSV}")

if not CONFIG_PATH.exists():
    fail(f"ملف config غير موجود: {CONFIG_PATH}")

print(f"✅ ملف المصدر موجود: {SOURCE_CSV}")
print(f"✅ ملف config موجود: {CONFIG_PATH}")


# =========================
# 2) قراءة CSV وفحص الأعمدة
# =========================

print("\n📥 قراءة ملف EURUSD M15...")

raw = load_csv_auto(SOURCE_CSV)

if raw.empty:
    fail("ملف CSV فارغ.")

print(f"✅ عدد الصفوف الأصلي: {len(raw):,}")
print(f"✅ الأعمدة الأصلية: {list(raw.columns)}")


date_col = find_column(
    raw.columns,
    [
        "date",
        "datetime",
        "timestamp",
        "time",
        "open_time",
        "start_time",
        "Date",
        "Datetime",
        "Timestamp",
        "Time",
    ],
)

open_col = find_column(raw.columns, ["open", "o", "Open"])
high_col = find_column(raw.columns, ["high", "h", "High"])
low_col = find_column(raw.columns, ["low", "l", "Low"])
close_col = find_column(raw.columns, ["close", "c", "Close"])
volume_col = find_column(
    raw.columns,
    [
        "volume",
        "vol",
        "tick_volume",
        "tickvol",
        "real_volume",
        "Volume",
        "TickVolume",
    ],
)

if date_col is None:
    fail("لم أجد عمود تاريخ. يجب وجود أحد هذه الأسماء: date / datetime / timestamp / time")

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
    print(
        "⚠️ لم أجد عمود volume. سيتم إنشاء volume = 1.0 لكل الشموع حتى لا تفشل الاستراتيجيات التي تشترط volume > 0."
    )
else:
    print(f"✅ تم العثور على عمود volume: {volume_col}")


# =========================
# 3) تحويل الأعمدة إلى صيغة Freqtrade
# =========================

print("\n🧱 تجهيز الأعمدة بصيغة Freqtrade...")

df = pd.DataFrame()
df["date"] = parse_date_series(raw[date_col])
df["open"] = pd.to_numeric(raw[open_col], errors="coerce")
df["high"] = pd.to_numeric(raw[high_col], errors="coerce")
df["low"] = pd.to_numeric(raw[low_col], errors="coerce")
df["close"] = pd.to_numeric(raw[close_col], errors="coerce")

if volume_col is not None:
    df["volume"] = pd.to_numeric(raw[volume_col], errors="coerce").fillna(0)
else:
    df["volume"] = 1.0

before_drop = len(df)

df = df.dropna(subset=["date", "open", "high", "low", "close"])
df = df.sort_values("date")
df = df.drop_duplicates(subset=["date"], keep="last")
df = df.reset_index(drop=True)

after_drop = len(df)

if df.empty:
    fail("بعد التنظيف لم يبقَ أي صف صالح.")

print(f"✅ الصفوف بعد التنظيف: {after_drop:,}")
print(f"ℹ️ تم حذف/استبعاد: {before_drop - after_drop:,} صف")


# =========================
# 4) فحوصات منطقية
# =========================

print("\n🧪 فحص منطقي للشموع...")

bad_ohlc = df[
    (df["high"] < df[["open", "close", "low"]].max(axis=1))
    | (df["low"] > df[["open", "close", "high"]].min(axis=1))
]

if len(bad_ohlc) > 0:
    print(
        f"⚠️ يوجد {len(bad_ohlc):,} شمعة فيها high/low غير منطقي. لن أوقف السكربت، لكن راجع جودة البيانات."
    )
else:
    print("✅ فحص OHLC منطقي.")

start_date = df["date"].min()
end_date = df["date"].max()

print(f"✅ بداية البيانات: {start_date}")
print(f"✅ نهاية البيانات: {end_date}")

diffs = df["date"].diff().dropna()
if not diffs.empty:
    median_diff = diffs.median()
    print(f"✅ الفاصل الزمني الوسيط: {median_diff}")

    expected = pd.Timedelta(minutes=15)
    if median_diff != expected:
        print(f"⚠️ الفاصل الوسيط ليس 15 دقيقة بالضبط: {median_diff}")
    else:
        print("✅ الفاصل يبدو M15.")

    gaps = diffs[diffs > expected]
    if len(gaps) > 0:
        print(f"⚠️ يوجد فجوات زمنية أكبر من 15 دقيقة: {len(gaps):,}")
    else:
        print("✅ لا توجد فجوات زمنية كبيرة حسب فحص الفواصل.")


# =========================
# 5) حفظ بيانات Freqtrade
# =========================

print("\n💾 حفظ ملف Freqtrade...")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

try:
    df.to_feather(OUTPUT_FEATHER)
except Exception as e:
    fail(f"فشل حفظ feather. تأكد من وجود pyarrow. الخطأ: {e}")

print("✅ تم حفظ الملف:")
print(f"   {OUTPUT_FEATHER}")


# =========================
# 6) تعديل config.json
# =========================

print("\n⚙️ تعديل user_data/config.json...")

backup_path = CONFIG_PATH.with_suffix(
    CONFIG_PATH.suffix + f".bak_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
)

shutil.copy2(CONFIG_PATH, backup_path)
print("✅ تم إنشاء نسخة احتياطية:")
print(f"   {backup_path}")

with CONFIG_PATH.open("r", encoding="utf-8") as f:
    config = json.load(f)

config["timeframe"] = TIMEFRAME
config["trading_mode"] = "spot"
config["margin_mode"] = ""
config["dataformat_ohlcv"] = "feather"

config.setdefault("exchange", {})
config["exchange"]["name"] = EXCHANGE_NAME
config["exchange"]["pair_whitelist"] = [PAIR]
config["exchange"].setdefault("pair_blacklist", ["BNB/.*"])

config["pairlists"] = [{"method": "StaticPairList"}]

with CONFIG_PATH.open("w", encoding="utf-8") as f:
    json.dump(config, f, indent=4, ensure_ascii=False)

print("✅ تم تعديل config.json بنجاح.")


# =========================
# 7) ملخص نهائي
# =========================

print("\n🎯 الملخص النهائي")
print("=" * 60)
print(f"الزوج داخل Freqtrade: {PAIR}")
print(f"الفريم: {TIMEFRAME}")
print(f"عدد الشموع: {len(df):,}")
print(f"من: {start_date}")
print(f"إلى: {end_date}")
print(f"ملف البيانات: {OUTPUT_FEATHER}")
print(f"ملف الإعداد: {CONFIG_PATH}")
print("=" * 60)

print("\n✅ انتهى التجهيز.")
print("\nجرّب بعدها أمر الباكتيست بدون تحديد timerange أول مرة:")
print(
    f"freqtrade backtesting --config user_data/config.json --strategy TestStrategy --timeframe {TIMEFRAME} -p {PAIR}"
)
