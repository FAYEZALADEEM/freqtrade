# تقرير Lookahead Analysis: LIB_STR065

**التاريخ:** 2026-06-19 06:44
**الأمر:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade lookahead-analysis --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR065 --timeframe 15m --timerange 20250101-20260101 --fee 0 --targeted-trade-amount 100 -p EUR/USDT
```

## قاعدة التحقق المطبقة

- `targeted_trade_amount = 100` (ثابت حسب القاعدة الدائمة)
- يتم فحص حتى 100 إشارة. إذا كان عدد الإشارات أقل، يتم التوضيح.

## النتائج

```

2026-06-19 06:44:43,432 - freqtrade - INFO - freqtrade 2026.6-dev-a29762684
2026-06-19 06:44:43,638 - numexpr.utils - INFO - NumExpr defaulting to 8 threads.
2026-06-19 06:44:44,473 - freqtrade.configuration.load_config - INFO - Using config: user_data/config.json ...
2026-06-19 06:44:44,474 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/63 ...
2026-06-19 06:44:44,476 - freqtrade.loggers - INFO - Enabling colorized output.
2026-06-19 06:44:44,476[38;5;243m - [0m[38;5;177mfreqtrade.loggers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLogfile configured
2026-06-19 06:44:44,476[38;5;243m - [0m[38;5;177mfreqtrade.loggers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mVerbosity set to 0
2026-06-19 06:44:44,477[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter -i/--timeframe detected ... Using timeframe: 15m ...
2026-06-19 06:44:44,477[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter --fee detected, setting fee to: 0.0 ...
2026-06-19 06:44:44,477[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter --timerange detected: 20250101-20260101 ...
2026-06-19 06:44:44,477[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing user-data directory: /home/fayez/freqtrade/user_data ...
2026-06-19 06:44:44,478[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing data directory: /home/fayez/freqtrade/user_data/data/binance ...
2026-06-19 06:44:44,478[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing pairs ['EUR/USDT']
2026-06-19 06:44:44,478[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mFilter trades by timerange: 20250101-20260101
2026-06-19 06:44:44,478[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mTargeted Trade amount: 100
2026-06-19 06:44:44,479[38;5;243m - [0m[38;5;177mfreqtrade.exchange.check_exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mChecking exchange...
2026-06-19 06:44:44,485[38;5;243m - [0m[38;5;177mfreqtrade.exchange.check_exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mExchange "binance" is officially supported by the Freqtrade development team.
2026-06-19 06:44:44,485[38;5;243m - [0m[38;5;177mfreqtrade.configuration.config_validation[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mValidating configuration ...
2026-06-19 06:44:44,487[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mForced order_types to market orders.
2026-06-19 06:44:44,487[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mForced max_open_trades to -1 (same amount as there are pairs)
2026-06-19 06:44:44,488[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mDry run wallet was not set to 1 billion, pushing it up there just to avoid false positives
2026-06-19 06:44:44,488[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mfixing stake_amount to 10k
2026-06-19 06:44:44,497[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR069.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR069.py, line 34)'
2026-06-19 06:44:44,502[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR061.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR061.py, line 34)'
2026-06-19 06:44:44,503[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR062.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR062.py, line 34)'
2026-06-19 06:44:44,505[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR060.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR060.py, line 34)'
2026-06-19 06:44:44,506[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR068.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR068.py, line 34)'
2026-06-19 06:44:44,513[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR071.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR071.py, line 34)'
2026-06-19 06:44:44,517[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR065.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR065.py, line 34)'
2026-06-19 06:44:44,518[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[1;31mERROR[0m[38;5;243m - [0mThere were no strategies specified neither through --strategy nor through --strategy-list or timeframe was not 
specified.

```


**رمز الخروج:** 0
