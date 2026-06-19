# تقرير Lookahead Analysis: VSAConservativeTemplate

**التاريخ:** 2026-06-19 06:51
**الأمر:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade lookahead-analysis --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --config <(echo '{"entry_pricing": {"price_side": "other"}, "exit_pricing": {"price_side": "other"}}') --strategy VSAConservativeTemplate --timeframe 15m --timerange 20250101-20260101 --fee 0 --targeted-trade-amount 100 -p EUR/USDT
```

## قاعدة التحقق المطبقة

- `targeted_trade_amount = 100` (ثابت حسب القاعدة الدائمة)
- يتم فحص حتى 100 إشارة. إذا كان عدد الإشارات أقل، يتم التوضيح.

## النتائج

```
[3m                                                                                 Lookahead Analysis                                                                                  [0m
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃[1m [0m[1m                  filename[0m[1m [0m┃[1m [0m[1m               strategy[0m[1m [0m┃[1m [0m[1m                                 has_bias[0m[1m [0m┃[1m [0m[1mtotal_signals[0m[1m [0m┃[1m [0m[1mbiased_entry_signals[0m[1m [0m┃[1m [0m[1mbiased_exit_signals[0m[1m [0m┃[1m [0m[1mbiased_indicators[0m[1m [0m┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ VSAConservativeTemplate.py │ VSAConservativeTemplate │ too few trades caught (8/10).Test failed. │               │                      │                     │                   │
└────────────────────────────┴─────────────────────────┴───────────────────────────────────────────┴───────────────┴──────────────────────┴─────────────────────┴───────────────────┘

2026-06-19 06:51:19,769 - freqtrade - INFO - freqtrade 2026.6-dev-a29762684
2026-06-19 06:51:19,981 - numexpr.utils - INFO - NumExpr defaulting to 8 threads.
2026-06-19 06:51:20,772 - freqtrade.configuration.load_config - INFO - Using config: user_data/config.json ...
2026-06-19 06:51:20,773 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/63 ...
2026-06-19 06:51:20,773 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/62 ...
2026-06-19 06:51:20,775 - freqtrade.loggers - INFO - Enabling colorized output.
2026-06-19 06:51:20,776[38;5;243m - [0m[38;5;177mfreqtrade.loggers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLogfile configured
2026-06-19 06:51:20,776[38;5;243m - [0m[38;5;177mfreqtrade.loggers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mVerbosity set to 0
2026-06-19 06:51:20,776[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter -i/--timeframe detected ... Using timeframe: 15m ...
2026-06-19 06:51:20,777[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter --fee detected, setting fee to: 0.0 ...
2026-06-19 06:51:20,777[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter --timerange detected: 20250101-20260101 ...
2026-06-19 06:51:20,777[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing user-data directory: /home/fayez/freqtrade/user_data ...
2026-06-19 06:51:20,777[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing data directory: /home/fayez/freqtrade/user_data/data/binance ...
2026-06-19 06:51:20,778[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing pairs ['EUR/USDT']
2026-06-19 06:51:20,778[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mFilter trades by timerange: 20250101-20260101
2026-06-19 06:51:20,778[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mTargeted Trade amount: 100
2026-06-19 06:51:20,779[38;5;243m - [0m[38;5;177mfreqtrade.exchange.check_exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mChecking exchange...
2026-06-19 06:51:20,785[38;5;243m - [0m[38;5;177mfreqtrade.exchange.check_exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mExchange "binance" is officially supported by the Freqtrade development team.
2026-06-19 06:51:20,785[38;5;243m - [0m[38;5;177mfreqtrade.configuration.config_validation[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mValidating configuration ...
2026-06-19 06:51:20,787[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mForced order_types to market orders.
2026-06-19 06:51:20,787[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mForced max_open_trades to -1 (same amount as there are pairs)
2026-06-19 06:51:20,787[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mDry run wallet was not set to 1 billion, pushing it up there just to avoid false positives
2026-06-19 06:51:20,788[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mfixing stake_amount to 10k
2026-06-19 06:51:20,796[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR072.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR072.py, line 34)'
2026-06-19 06:51:20,797[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR069.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR069.py, line 34)'
2026-06-19 06:51:20,801[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR061.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR061.py, line 34)'
2026-06-19 06:51:20,802[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR062.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR062.py, line 34)'
2026-06-19 06:51:20,803[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR060.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR060.py, line 34)'
2026-06-19 06:51:20,804[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR074.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR074.py, line 34)'
2026-06-19 06:51:20,805[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR068.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR068.py, line 34)'
2026-06-19 06:51:20,808[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR073.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR073.py, line 34)'
2026-06-19 06:51:20,812[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR071.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR071.py, line 34)'
2026-06-19 06:51:20,816[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR065.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR065.py, line 34)'
2026-06-19 06:51:20,816[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mBias test of VSAConservativeTemplate.py started.
2026-06-19 06:51:20,818[38;5;243m - [0m[38;5;177mfreqtrade.exchange.exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mInstance is running with dry_run enabled
2026-06-19 06:51:20,818[38;5;243m - [0m[38;5;177mfreqtrade.exchange.exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing CCXT 4.5.58
2026-06-19 06:51:20,829[38;5;243m - [0m[38;5;177mfreqtrade.exchange.exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing Exchange "Binance"
2026-06-19 06:51:22,052[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.exchange_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing resolved exchange 'Binance'...
2026-06-19 06:51:22,058[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing resolved strategy VSAConservativeTemplate from '/home/fayez/freqtrade/user_data/strategies/VSAConservativeTemplate.py'...
2026-06-19 06:51:22,058[38;5;243m - [0m[38;5;177mfreqtrade.strategy.hyper[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mFound no parameter file.
2026-06-19 06:51:22,059[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'timeframe' with value from the configuration: 15m.
2026-06-19 06:51:22,059[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'order_types' with value from the configuration: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 
'stoploss_on_exchange': False}.
2026-06-19 06:51:22,059[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'stake_currency' with value from the configuration: USDT.
2026-06-19 06:51:22,060[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'stake_amount' with value from the configuration: 10000.
2026-06-19 06:51:22,060[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'unfilledtimeout' with value from the configuration: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 
'unit': 'minutes'}.
2026-06-19 06:51:22,060[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'max_open_trades' with value from the configuration: -1.
2026-06-19 06:51:22,061[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using minimal_roi: {'0': 0.03}
2026-06-19 06:51:22,061[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using timeframe: 15m
2026-06-19 06:51:22,061[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using stoploss: -0.015
2026-06-19 06:51:22,061[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using trailing_stop: False
2026-06-19 06:51:22,062[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using trailing_stop_positive_offset: 0.0
2026-06-19 06:51:22,062[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using trailing_only_offset_is_reached: False
2026-06-19 06:51:22,062[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using use_custom_stoploss: False
2026-06-19 06:51:22,062[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using process_only_new_candles: True
2026-06-19 06:51:22,063[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using order_types: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 'stoploss_on_exchange': False}
2026-06-19 06:51:22,063[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2026-06-19 06:51:22,063[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using stake_currency: USDT
2026-06-19 06:51:22,064[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using stake_amount: 10000
2026-06-19 06:51:22,064[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using startup_candle_count: 0
2026-06-19 06:51:22,064[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2026-06-19 06:51:22,065[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using use_exit_signal: True
2026-06-19 06:51:22,065[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using exit_profit_only: False
2026-06-19 06:51:22,065[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using ignore_roi_if_entry_signal: False
2026-06-19 06:51:22,065[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using exit_profit_offset: 0.0
2026-06-19 06:51:22,066[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using disable_dataframe_checks: False
2026-06-19 06:51:22,066[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using ignore_buying_expired_candle_after: 0
2026-06-19 06:51:22,066[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using position_adjustment_enable: False
2026-06-19 06:51:22,066[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using max_entry_position_adjustment: -1
2026-06-19 06:51:22,067[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using max_open_trades: -1
2026-06-19 06:51:22,067[38;5;243m - [0m[38;5;177mfreqtrade.configuration.config_validation[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mValidating configuration ...
2026-06-19 06:51:22,071[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing resolved pairlist StaticPairList from '/home/fayez/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2026-06-19 06:51:22,084[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing fee 0.0000% from config.
2026-06-19 06:51:22,134[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 24900 - after: 34944 - 40.34%
2026-06-19 06:51:22,135[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-31 21:45:00 (363 days).
2026-06-19 06:51:23,769[38;5;243m - [0m[38;5;177mfreqtrade.loggers.set_log_levels[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mReducing verbosity for bias tester.
2026-06-19 06:51:23,769[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOnly found 10 trades. Calculating all available trades.
2026-06-19 06:51:23,807[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-03 11:30:00 (1 days).
2026-06-19 06:51:23,896[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4214 - after: 5942 - 41.01%
2026-06-19 06:51:23,896[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-04 19:15:00 (61 days).
2026-06-19 06:51:24,320[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4226 - after: 5954 - 40.89%
2026-06-19 06:51:24,321[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-04 22:15:00 (62 days).
2026-06-19 06:51:24,692[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4694 - after: 6610 - 40.82%
2026-06-19 06:51:24,692[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-11 18:15:00 (68 days).
2026-06-19 06:51:25,144[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 5499 - after: 7799 - 41.83%
2026-06-19 06:51:25,144[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-24 03:30:00 (81 days).
2026-06-19 06:51:25,556[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6793 - after: 9477 - 39.51%
2026-06-19 06:51:25,557[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-10 15:00:00 (98 days).
2026-06-19 06:51:26,098[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6805 - after: 9489 - 39.44%
2026-06-19 06:51:26,099[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-10 18:00:00 (98 days).
2026-06-19 06:51:26,611[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 7437 - after: 10505 - 41.25%
2026-06-19 06:51:26,611[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-21 08:00:00 (109 days).
2026-06-19 06:51:27,259[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8505 - after: 11957 - 40.59%
2026-06-19 06:51:27,260[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-06 11:00:00 (124 days).
2026-06-19 06:51:27,863[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8875 - after: 12519 - 41.06%
2026-06-19 06:51:27,864[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-12 07:30:00 (130 days).
2026-06-19 06:51:28,556[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 9564 - after: 13400 - 40.11%
2026-06-19 06:51:28,557[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-21 11:45:00 (139 days).
2026-06-19 06:51:29,173[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 12012 - after: 16808 - 39.93%
2026-06-19 06:51:29,174[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-25 23:45:00 (175 days).
2026-06-19 06:51:30,050[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 13133 - after: 18313 - 39.44%
2026-06-19 06:51:30,050[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-11 16:00:00 (190 days).
2026-06-19 06:51:30,856[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 14273 - after: 20029 - 40.33%
2026-06-19 06:51:30,857[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-29 13:00:00 (208 days).
2026-06-19 06:51:31,896[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 14880 - after: 20828 - 39.97%
2026-06-19 06:51:31,897[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-06 20:45:00 (216 days).
2026-06-19 06:51:32,866[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 20988 - after: 29436 - 40.25%
2026-06-19 06:51:32,867[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-11-04 12:45:00 (306 days).
2026-06-19 06:51:34,351[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mfound force-exit in pair: EUR/USDT, timerange:2025-11-10 10:15:00+00:00-2025-12-31 21:45:00+00:00, idx: 8, skipping this one to
avoid a false-positive.
2026-06-19 06:51:34,352[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0monly found 10 after skipping forced exits which is smaller than minimum trade amount = 10. Exiting this lookahead-analysis
2026-06-19 06:51:34,352[38;5;243m - [0m[38;5;177mfreqtrade.loggers.set_log_levels[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mRestoring log verbosity.
2026-06-19 06:51:34,352[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0m -> VSAConservativeTemplate : too few trades. We only found 8 trades. Hint: Extend the timerange to get at least 10 or lower 
the value of minimum_trade_amount.
2026-06-19 06:51:34,353[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mChecking look ahead bias via backtests of VSAConservativeTemplate.py took 14 seconds.

```


**رمز الخروج:** 0
