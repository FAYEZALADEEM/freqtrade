import json
import shutil
from datetime import datetime
from pathlib import Path


CONFIG_PATH = Path("/home/fayez/freqtrade/user_data/config.json")

if not CONFIG_PATH.exists():
    raise SystemExit(f"config غير موجود: {CONFIG_PATH}")

backup = CONFIG_PATH.with_suffix(
    CONFIG_PATH.suffix + f".bak_freqai_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
)

shutil.copy2(CONFIG_PATH, backup)

with CONFIG_PATH.open("r", encoding="utf-8") as f:
    config = json.load(f)

# إعدادات عامة
config["timeframe"] = "15m"
config["trading_mode"] = "spot"
config["margin_mode"] = ""
config["dataformat_ohlcv"] = "feather"

# الزوج العملي داخل Freqtrade لبيانات EURUSD
config.setdefault("exchange", {})
config["exchange"]["name"] = "binance"
config["exchange"]["pair_whitelist"] = ["EUR/USDT"]
config["exchange"].setdefault("pair_blacklist", ["BNB/.*"])

config["pairlists"] = [{"method": "StaticPairList"}]

# إعدادات FreqAI
config["freqai"] = {
    "enabled": True,
    "identifier": "eurusd_m15_hybrid_freqai_v1",
    "train_period_days": 30,
    "backtest_period_days": 7,
    "expiration_hours": 0,
    "purge_old_models": 2,
    "save_backtest_models": True,
    "feature_parameters": {
        "include_timeframes": ["15m"],
        "include_corr_pairlist": [],
        "label_period_candles": 8,
        "include_shifted_candles": 2,
        "DI_threshold": 0,
        "weight_factor": 0.9,
        "principal_component_analysis": False,
        "use_SVM_to_remove_outliers": False,
        "indicator_periods_candles": [7, 14, 28],
    },
    "data_split_parameters": {"test_size": 0.20, "shuffle": False},
    "model_training_parameters": {
        "n_estimators": 300,
        "learning_rate": 0.03,
        "num_leaves": 31,
        "max_depth": -1,
        "min_child_samples": 20,
        "subsample": 0.8,
        "colsample_bytree": 0.8,
        "random_state": 42,
    },
}

with CONFIG_PATH.open("w", encoding="utf-8") as f:
    json.dump(config, f, indent=4, ensure_ascii=False)

print("✅ تم تعديل config.json وإضافة FreqAI.")
print(f"✅ نسخة احتياطية: {backup}")
