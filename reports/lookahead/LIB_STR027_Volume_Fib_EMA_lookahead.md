# تقرير Lookahead Analysis: LIB_STR027_Volume_Fib_EMA

**التاريخ:** 2026-06-19 06:41
**الأمر:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade lookahead-analysis --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR027_Volume_Fib_EMA --timeframe 15m --timerange 20250101-20260101 --fee 0 --targeted-trade-amount 100 -p EUR/USDT
```

## قاعدة التحقق المطبقة

- `targeted_trade_amount = 100` (ثابت حسب القاعدة الدائمة)
- يتم فحص حتى 100 إشارة. إذا كان عدد الإشارات أقل، يتم التوضيح.

## النتائج

```

```

## stderr

2026-06-19 06:41:28,063 - freqtrade - INFO - freqtrade 2026.6-dev-a29762684
2026-06-19 06:41:28,447 - numexpr.utils - INFO - NumExpr defaulting to 8 threads.
2026-06-19 06:41:29,843 - freqtrade.configuration.load_config - INFO - Using config: user_data/config.json ...
2026-06-19 06:41:29,844 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/63 ...
2026-06-19 06:41:29,848 - freqtrade.loggers - INFO - Enabling colorized output.
2026-06-19 06:41:29,849[38;5;243m - [0m[38;5;177mfreqtrade.loggers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLogfile configured
2026-06-19 06:41:29,850[38;5;243m - [0m[38;5;177mfreqtrade.loggers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mVerbosity set to 0
2026-06-19 06:41:29,850[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter -i/--timeframe detected ... Using timeframe: 15m ...
2026-06-19 06:41:29,851[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter --fee detected, setting fee to: 0.0 ...
2026-06-19 06:41:29,851[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter --timerange detected: 20250101-20260101 ...
2026-06-19 06:41:29,852[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing user-data directory: /home/fayez/freqtrade/user_data ...
2026-06-19 06:41:29,852[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing data directory: /home/fayez/freqtrade/user_data/data/binance ...
2026-06-19 06:41:29,853[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing pairs ['EUR/USDT']
2026-06-19 06:41:29,853[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[

**رمز الخروج:** 0
