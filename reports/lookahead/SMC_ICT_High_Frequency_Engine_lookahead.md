# تقرير Lookahead Analysis: SMC_ICT_High_Frequency_Engine

**التاريخ:** 2026-06-19 03:13
**الأمر:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade lookahead-analysis --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy SMC_ICT_High_Frequency_Engine --timeframe 15m --timerange 20250101-20260101 --fee 0 --targeted-trade-amount 100 -p EUR/USDT
```

## قاعدة التحقق المطبقة

- `targeted_trade_amount = 100` (ثابت حسب القاعدة الدائمة)
- يتم فحص حتى 100 إشارة. إذا كان عدد الإشارات أقل، يتم التوضيح.

## النتائج

```

```

## stderr

2026-06-19 03:13:04,139 - freqtrade - INFO - freqtrade 2026.6-dev-a29762684
2026-06-19 03:13:04,361 - numexpr.utils - INFO - NumExpr defaulting to 8 threads.
2026-06-19 03:13:05,158 - freqtrade.configuration.load_config - INFO - Using config: user_data/config.json ...
2026-06-19 03:13:05,159 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/63 ...
2026-06-19 03:13:05,161 - freqtrade.loggers - INFO - Enabling colorized output.
2026-06-19 03:13:05,161[38;5;243m - [0m[38;5;177mfreqtrade.loggers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLogfile configured
2026-06-19 03:13:05,161[38;5;243m - [0m[38;5;177mfreqtrade.loggers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mVerbosity set to 0
2026-06-19 03:13:05,162[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter -i/--timeframe detected ... Using timeframe: 15m ...
2026-06-19 03:13:05,162[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter --fee detected, setting fee to: 0.0 ...
2026-06-19 03:13:05,162[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter --timerange detected: 20250101-20260101 ...
2026-06-19 03:13:05,162[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing user-data directory: /home/fayez/freqtrade/user_data ...
2026-06-19 03:13:05,163[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing data directory: /home/fayez/freqtrade/user_data/data/binance ...
2026-06-19 03:13:05,163[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing pairs ['EUR/USDT']
2026-06-19 03:13:05,163[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[

**رمز الخروج:** 0
