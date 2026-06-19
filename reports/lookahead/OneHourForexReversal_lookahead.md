# تقرير Lookahead Analysis: OneHourForexReversal

**التاريخ:** 2026-06-19 06:47
**الأمر:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade lookahead-analysis --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --config <(echo '{"entry_pricing": {"price_side": "other"}, "exit_pricing": {"price_side": "other"}}') --strategy OneHourForexReversal --timeframe 15m --timerange 20250101-20260101 --fee 0 --targeted-trade-amount 100 -p EUR/USDT
```

## قاعدة التحقق المطبقة

- `targeted_trade_amount = 100` (ثابت حسب القاعدة الدائمة)
- يتم فحص حتى 100 إشارة. إذا كان عدد الإشارات أقل، يتم التوضيح.

## النتائج

```
[3m                                                                              Lookahead Analysis                                                                               [0m
┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃[1m [0m[1m               filename[0m[1m [0m┃[1m [0m[1m            strategy[0m[1m [0m┃[1m [0m[1m                                 has_bias[0m[1m [0m┃[1m [0m[1mtotal_signals[0m[1m [0m┃[1m [0m[1mbiased_entry_signals[0m[1m [0m┃[1m [0m[1mbiased_exit_signals[0m[1m [0m┃[1m [0m[1mbiased_indicators[0m[1m [0m┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ OneHourForexReversal.py │ OneHourForexReversal │ too few trades caught (0/10).Test failed. │               │                      │                     │                   │
└─────────────────────────┴──────────────────────┴───────────────────────────────────────────┴───────────────┴──────────────────────┴─────────────────────┴───────────────────┘

2026-06-19 06:47:19,474 - freqtrade - INFO - freqtrade 2026.6-dev-a29762684
2026-06-19 06:47:19,720 - numexpr.utils - INFO - NumExpr defaulting to 8 threads.
2026-06-19 06:47:20,566 - freqtrade.configuration.load_config - INFO - Using config: user_data/config.json ...
2026-06-19 06:47:20,566 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/63 ...
2026-06-19 06:47:20,567 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/62 ...
2026-06-19 06:47:20,569 - freqtrade.loggers - INFO - Enabling colorized output.
2026-06-19 06:47:20,570[38;5;243m - [0m[38;5;177mfreqtrade.loggers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLogfile configured
2026-06-19 06:47:20,570[38;5;243m - [0m[38;5;177mfreqtrade.loggers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mVerbosity set to 0
2026-06-19 06:47:20,571[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter -i/--timeframe detected ... Using timeframe: 15m ...
2026-06-19 06:47:20,571[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter --fee detected, setting fee to: 0.0 ...
2026-06-19 06:47:20,571[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter --timerange detected: 20250101-20260101 ...
2026-06-19 06:47:20,572[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing user-data directory: /home/fayez/freqtrade/user_data ...
2026-06-19 06:47:20,572[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing data directory: /home/fayez/freqtrade/user_data/data/binance ...
2026-06-19 06:47:20,572[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing pairs ['EUR/USDT']
2026-06-19 06:47:20,573[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mFilter trades by timerange: 20250101-20260101
2026-06-19 06:47:20,573[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mTargeted Trade amount: 100
2026-06-19 06:47:20,573[38;5;243m - [0m[38;5;177mfreqtrade.exchange.check_exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mChecking exchange...
2026-06-19 06:47:20,580[38;5;243m - [0m[38;5;177mfreqtrade.exchange.check_exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mExchange "binance" is officially supported by the Freqtrade development team.
2026-06-19 06:47:20,580[38;5;243m - [0m[38;5;177mfreqtrade.configuration.config_validation[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mValidating configuration ...
2026-06-19 06:47:20,582[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mForced order_types to market orders.
2026-06-19 06:47:20,583[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mForced max_open_trades to -1 (same amount as there are pairs)
2026-06-19 06:47:20,583[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mDry run wallet was not set to 1 billion, pushing it up there just to avoid false positives
2026-06-19 06:47:20,583[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mfixing stake_amount to 10k
2026-06-19 06:47:20,593[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR072.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR072.py, line 34)'
2026-06-19 06:47:20,594[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR069.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR069.py, line 34)'
2026-06-19 06:47:20,598[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR061.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR061.py, line 34)'
2026-06-19 06:47:20,599[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR062.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR062.py, line 34)'
2026-06-19 06:47:20,601[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR060.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR060.py, line 34)'
2026-06-19 06:47:20,602[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR074.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR074.py, line 34)'
2026-06-19 06:47:20,603[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR068.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR068.py, line 34)'
2026-06-19 06:47:20,607[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR073.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR073.py, line 34)'
2026-06-19 06:47:20,612[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR071.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR071.py, line 34)'
2026-06-19 06:47:20,616[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR065.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR065.py, line 34)'
2026-06-19 06:47:20,617[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mBias test of OneHourForexReversal.py started.
2026-06-19 06:47:20,619[38;5;243m - [0m[38;5;177mfreqtrade.exchange.exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mInstance is running with dry_run enabled
2026-06-19 06:47:20,619[38;5;243m - [0m[38;5;177mfreqtrade.exchange.exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing CCXT 4.5.58
2026-06-19 06:47:20,631[38;5;243m - [0m[38;5;177mfreqtrade.exchange.exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing Exchange "Binance"
2026-06-19 06:47:22,256[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.exchange_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing resolved exchange 'Binance'...
2026-06-19 06:47:22,267[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing resolved strategy OneHourForexReversal from '/home/fayez/freqtrade/user_data/strategies/OneHourForexReversal.py'...
2026-06-19 06:47:22,268[38;5;243m - [0m[38;5;177mfreqtrade.strategy.hyper[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mFound no parameter file.
2026-06-19 06:47:22,269[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'timeframe' with value from the configuration: 15m.
2026-06-19 06:47:22,269[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'order_types' with value from the configuration: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 
'stoploss_on_exchange': False}.
2026-06-19 06:47:22,270[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'stake_currency' with value from the configuration: USDT.
2026-06-19 06:47:22,270[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'stake_amount' with value from the configuration: 10000.
2026-06-19 06:47:22,271[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'unfilledtimeout' with value from the configuration: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 
'unit': 'minutes'}.
2026-06-19 06:47:22,271[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'max_open_trades' with value from the configuration: -1.
2026-06-19 06:47:22,271[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using minimal_roi: {'0': 0.02}
2026-06-19 06:47:22,272[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using timeframe: 15m
2026-06-19 06:47:22,272[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using stoploss: -0.02
2026-06-19 06:47:22,273[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using trailing_stop: False
2026-06-19 06:47:22,273[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using trailing_stop_positive_offset: 0.0
2026-06-19 06:47:22,273[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using trailing_only_offset_is_reached: False
2026-06-19 06:47:22,274[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using use_custom_stoploss: False
2026-06-19 06:47:22,274[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using process_only_new_candles: True
2026-06-19 06:47:22,274[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using order_types: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 'stoploss_on_exchange': False}
2026-06-19 06:47:22,275[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2026-06-19 06:47:22,275[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using stake_currency: USDT
2026-06-19 06:47:22,276[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using stake_amount: 10000
2026-06-19 06:47:22,276[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using startup_candle_count: 0
2026-06-19 06:47:22,276[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2026-06-19 06:47:22,277[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using use_exit_signal: True
2026-06-19 06:47:22,277[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using exit_profit_only: False
2026-06-19 06:47:22,278[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using ignore_roi_if_entry_signal: False
2026-06-19 06:47:22,278[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using exit_profit_offset: 0.0
2026-06-19 06:47:22,278[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using disable_dataframe_checks: False
2026-06-19 06:47:22,279[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using ignore_buying_expired_candle_after: 0
2026-06-19 06:47:22,279[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using position_adjustment_enable: False
2026-06-19 06:47:22,280[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using max_entry_position_adjustment: -1
2026-06-19 06:47:22,280[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using max_open_trades: -1
2026-06-19 06:47:22,280[38;5;243m - [0m[38;5;177mfreqtrade.configuration.config_validation[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mValidating configuration ...
2026-06-19 06:47:22,288[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing resolved pairlist StaticPairList from '/home/fayez/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2026-06-19 06:47:22,315[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing fee 0.0000% from config.
2026-06-19 06:47:22,384[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 24900 - after: 34944 - 40.34%
2026-06-19 06:47:22,385[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-31 21:45:00 (363 days).
2026-06-19 06:47:24,570[38;5;243m - [0m[38;5;177mfreqtrade.loggers.set_log_levels[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mReducing verbosity for bias tester.
2026-06-19 06:47:24,571[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mfound 9 trades which is less than minimum_trade_amount 10. Cancelling this backtest lookahead bias test.
2026-06-19 06:47:24,572[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mChecking look ahead bias via backtests of OneHourForexReversal.py took 4 seconds.

```


**رمز الخروج:** 0
