# تقرير Lookahead Analysis: LIB_STR053

**التاريخ:** 2026-06-19 06:56
**الأمر:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade lookahead-analysis --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --config <(echo '{"entry_pricing": {"price_side": "other"}, "exit_pricing": {"price_side": "other"}}') --strategy LIB_STR053 --timeframe 15m --timerange 20250101-20260101 --fee 0 --targeted-trade-amount 100 -p EUR/USDT
```

## قاعدة التحقق المطبقة

- `targeted_trade_amount = 100` (ثابت حسب القاعدة الدائمة)
- يتم فحص حتى 100 إشارة. إذا كان عدد الإشارات أقل، يتم التوضيح.

## النتائج

```
                                                    Lookahead Analysis                                                    
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃      filename ┃   strategy ┃ has_bias ┃ total_signals ┃ biased_entry_signals ┃ biased_exit_signals ┃ biased_indicators ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ LIB_STR053.py │ LIB_STR053 │       No │            46 │                    0 │                   0 │                   │
└───────────────┴────────────┴──────────┴───────────────┴──────────────────────┴─────────────────────┴───────────────────┘

2026-06-19 06:55:23,685 - freqtrade - INFO - freqtrade 2026.6-dev-a29762684
2026-06-19 06:55:24,043 - numexpr.utils - INFO - NumExpr defaulting to 8 threads.
2026-06-19 06:55:25,255 - freqtrade.configuration.load_config - INFO - Using config: user_data/config.json ...
2026-06-19 06:55:25,256 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/63 ...
2026-06-19 06:55:25,256 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/62 ...
2026-06-19 06:55:25,259 - freqtrade.loggers - INFO - Enabling colorized output.
2026-06-19 06:55:25,259 - freqtrade.loggers - INFO - Logfile configured
2026-06-19 06:55:25,259 - freqtrade.loggers - INFO - Verbosity set to 0
2026-06-19 06:55:25,259 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2026-06-19 06:55:25,260 - freqtrade.configuration.configuration - INFO - Parameter --fee detected, setting fee to: 0.0 ...
2026-06-19 06:55:25,260 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20250101-20260101 ...
2026-06-19 06:55:25,260 - freqtrade.configuration.configuration - INFO - Using user-data directory: /home/fayez/freqtrade/user_data ...
2026-06-19 06:55:25,261 - freqtrade.configuration.configuration - INFO - Using data directory: /home/fayez/freqtrade/user_data/data/binance ...
2026-06-19 06:55:25,261 - freqtrade.configuration.configuration - INFO - Using pairs ['EUR/USDT']
2026-06-19 06:55:25,261 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20250101-20260101
2026-06-19 06:55:25,262 - freqtrade.configuration.configuration - INFO - Targeted Trade amount: 100
2026-06-19 06:55:25,262 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2026-06-19 06:55:25,268 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2026-06-19 06:55:25,269 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2026-06-19 06:55:25,271 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Forced order_types to market orders.
2026-06-19 06:55:25,271 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Forced max_open_trades to -1 (same amount as there are pairs)
2026-06-19 06:55:25,271 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Dry run wallet was not set to 1 billion, pushing it up there just to avoid false positives
2026-06-19 06:55:25,272 - freqtrade.optimize.analysis.lookahead_helpers - INFO - fixing stake_amount to 10k
2026-06-19 06:55:25,282 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR072.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR072.py, line 34)'
2026-06-19 06:55:25,282 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR069.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR069.py, line 34)'
2026-06-19 06:55:25,287 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR061.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR061.py, line 34)'
2026-06-19 06:55:25,288 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR062.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR062.py, line 34)'
2026-06-19 06:55:25,290 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR060.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR060.py, line 34)'
2026-06-19 06:55:25,291 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR074.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR074.py, line 34)'
2026-06-19 06:55:25,292 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR068.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR068.py, line 34)'
2026-06-19 06:55:25,295 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR073.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR073.py, line 34)'
2026-06-19 06:55:25,300 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR071.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR071.py, line 34)'
2026-06-19 06:55:25,304 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR065.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR065.py, line 34)'
2026-06-19 06:55:25,304 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Bias test of LIB_STR053.py started.
2026-06-19 06:55:25,306 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2026-06-19 06:55:25,306 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.58
2026-06-19 06:55:25,319 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2026-06-19 06:55:27,478 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2026-06-19 06:55:27,482 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy LIB_STR053 from '/home/fayez/freqtrade/user_data/strategies/LIB_STR053.py'...
2026-06-19 06:55:27,483 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2026-06-19 06:55:27,483 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value from the configuration: 15m.
2026-06-19 06:55:27,484 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'order_types' with value from the configuration: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 
'stoploss_on_exchange': False}.
2026-06-19 06:55:27,484 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value from the configuration: USDT.
2026-06-19 06:55:27,485 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value from the configuration: 10000.
2026-06-19 06:55:27,485 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value from the configuration: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 
'unit': 'minutes'}.
2026-06-19 06:55:27,485 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value from the configuration: -1.
2026-06-19 06:55:27,486 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.01}
2026-06-19 06:55:27,486 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2026-06-19 06:55:27,486 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.01
2026-06-19 06:55:27,487 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2026-06-19 06:55:27,487 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2026-06-19 06:55:27,487 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2026-06-19 06:55:27,488 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: False
2026-06-19 06:55:27,488 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2026-06-19 06:55:27,488 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 'stoploss_on_exchange': False}
2026-06-19 06:55:27,489 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2026-06-19 06:55:27,489 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2026-06-19 06:55:27,490 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: 10000
2026-06-19 06:55:27,490 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2026-06-19 06:55:27,490 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2026-06-19 06:55:27,491 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2026-06-19 06:55:27,491 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2026-06-19 06:55:27,491 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2026-06-19 06:55:27,492 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2026-06-19 06:55:27,492 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2026-06-19 06:55:27,492 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2026-06-19 06:55:27,493 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2026-06-19 06:55:27,493 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2026-06-19 06:55:27,493 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: -1
2026-06-19 06:55:27,494 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2026-06-19 06:55:27,499 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/home/fayez/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2026-06-19 06:55:27,518 - freqtrade.optimize.backtesting - INFO - Using fee 0.0000% from config.
2026-06-19 06:55:27,574 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 24900 - after: 34944 - 40.34%
2026-06-19 06:55:27,575 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-31 21:45:00 (363 days).
2026-06-19 06:55:30,141 - freqtrade.loggers.set_log_levels - INFO - Reducing verbosity for bias tester.
2026-06-19 06:55:30,142 - freqtrade.optimize.analysis.lookahead - INFO - Only found 48 trades. Calculating all available trades.
2026-06-19 06:55:30,181 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-02 09:00:00 (0 days).
2026-06-19 06:55:30,268 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-02 16:15:00 (0 days).
2026-06-19 06:55:30,427 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-03 05:45:00 (1 days).
2026-06-19 06:55:30,548 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 246 - after: 438 - 78.05%
2026-06-19 06:55:30,549 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-06 11:15:00 (4 days).
2026-06-19 06:55:30,682 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 247 - after: 439 - 77.73%
2026-06-19 06:55:30,683 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-06 11:30:00 (4 days).
2026-06-19 06:55:30,789 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 440 - after: 632 - 43.64%
2026-06-19 06:55:30,790 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-08 11:45:00 (6 days).
2026-06-19 06:55:30,923 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 528 - after: 720 - 36.36%
2026-06-19 06:55:30,924 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-09 09:45:00 (7 days).
2026-06-19 06:55:31,091 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 700 - after: 1084 - 54.86%
2026-06-19 06:55:31,092 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-13 04:45:00 (11 days).
2026-06-19 06:55:31,344 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 841 - after: 1225 - 45.66%
2026-06-19 06:55:31,345 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-14 16:00:00 (12 days).
2026-06-19 06:55:31,560 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1216 - after: 1792 - 47.37%
2026-06-19 06:55:31,561 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-20 13:45:00 (18 days).
2026-06-19 06:55:31,872 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1287 - after: 1863 - 44.76%
2026-06-19 06:55:31,873 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-21 07:30:00 (19 days).
2026-06-19 06:55:32,141 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1578 - after: 2154 - 36.50%
2026-06-19 06:55:32,142 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-24 08:15:00 (22 days).
2026-06-19 06:55:32,487 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1773 - after: 2541 - 43.32%
2026-06-19 06:55:32,488 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-28 09:00:00 (26 days).
2026-06-19 06:55:32,805 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2114 - after: 3074 - 45.41%
2026-06-19 06:55:32,807 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-02 22:15:00 (32 days).
2026-06-19 06:55:33,203 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2254 - after: 3214 - 42.59%
2026-06-19 06:55:33,204 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-04 09:15:00 (33 days).
2026-06-19 06:55:33,528 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2374 - after: 3334 - 40.44%
2026-06-19 06:55:33,529 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-05 15:15:00 (34 days).
2026-06-19 06:55:33,802 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2760 - after: 3912 - 41.74%
2026-06-19 06:55:33,803 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-11 15:45:00 (40 days).
2026-06-19 06:55:34,150 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2955 - after: 4107 - 38.98%
2026-06-19 06:55:34,151 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-13 16:30:00 (42 days).
2026-06-19 06:55:34,606 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 3015 - after: 4167 - 38.21%
2026-06-19 06:55:34,607 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-14 07:30:00 (43 days).
2026-06-19 06:55:34,937 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4019 - after: 5555 - 38.22%
2026-06-19 06:55:34,938 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-28 18:30:00 (57 days).
2026-06-19 06:55:35,524 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4103 - after: 5831 - 42.12%
2026-06-19 06:55:35,525 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-03 15:30:00 (60 days).
2026-06-19 06:55:36,064 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4214 - after: 5942 - 41.01%
2026-06-19 06:55:36,065 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-04 19:15:00 (61 days).
2026-06-19 06:55:36,445 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4264 - after: 5992 - 40.53%
2026-06-19 06:55:36,445 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-05 07:45:00 (62 days).
2026-06-19 06:55:36,825 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4292 - after: 6020 - 40.26%
2026-06-19 06:55:36,826 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-05 14:45:00 (62 days).
2026-06-19 06:55:37,192 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4515 - after: 6431 - 42.44%
2026-06-19 06:55:37,192 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-09 21:30:00 (66 days).
2026-06-19 06:55:37,562 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4694 - after: 6610 - 40.82%
2026-06-19 06:55:37,563 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-11 18:15:00 (68 days).
2026-06-19 06:55:38,024 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4735 - after: 6651 - 40.46%
2026-06-19 06:55:38,025 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-12 04:30:00 (69 days).
2026-06-19 06:55:38,399 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 5552 - after: 7852 - 41.43%
2026-06-19 06:55:38,400 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-24 16:45:00 (81 days).
2026-06-19 06:55:39,105 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 5626 - after: 7926 - 40.88%
2026-06-19 06:55:39,106 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-25 11:15:00 (82 days).
2026-06-19 06:55:39,602 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6275 - after: 8767 - 39.71%
2026-06-19 06:55:39,603 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 05:30:00 (91 days).
2026-06-19 06:55:40,277 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6334 - after: 8826 - 39.34%
2026-06-19 06:55:40,278 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 20:15:00 (91 days).
2026-06-19 06:55:40,958 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6434 - after: 9118 - 41.72%
2026-06-19 06:55:40,959 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-06 21:15:00 (94 days).
2026-06-19 06:55:41,495 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6470 - after: 9154 - 41.48%
2026-06-19 06:55:41,496 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-07 06:15:00 (95 days).
2026-06-19 06:55:42,063 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6506 - after: 9190 - 41.25%
2026-06-19 06:55:42,063 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-07 15:15:00 (95 days).
2026-06-19 06:55:42,606 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6569 - after: 9253 - 40.86%
2026-06-19 06:55:42,607 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-08 07:00:00 (96 days).
2026-06-19 06:55:43,283 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6783 - after: 9467 - 39.57%
2026-06-19 06:55:43,284 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 12:30:00 (98 days).
2026-06-19 06:55:43,850 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6796 - after: 9480 - 39.49%
2026-06-19 06:55:43,851 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 15:45:00 (98 days).
2026-06-19 06:55:44,406 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6832 - after: 9516 - 39.29%
2026-06-19 06:55:44,407 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 00:45:00 (99 days).
2026-06-19 06:55:45,198 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6857 - after: 9541 - 39.14%
2026-06-19 06:55:45,199 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 07:00:00 (99 days).
2026-06-19 06:55:45,774 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6862 - after: 9546 - 39.11%
2026-06-19 06:55:45,776 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 08:15:00 (99 days).
2026-06-19 06:55:46,396 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7119 - after: 9995 - 40.40%
2026-06-19 06:55:46,397 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-16 00:30:00 (104 days).
2026-06-19 06:55:46,904 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7398 - after: 10466 - 41.47%
2026-06-19 06:55:46,905 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-20 22:15:00 (109 days).
2026-06-19 06:55:47,490 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7524 - after: 10592 - 40.78%
2026-06-19 06:55:47,491 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-22 05:45:00 (110 days).
2026-06-19 06:55:48,034 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7570 - after: 10638 - 40.53%
2026-06-19 06:55:48,035 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-22 17:15:00 (110 days).
2026-06-19 06:55:48,673 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7726 - after: 10794 - 39.71%
2026-06-19 06:55:48,673 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-24 08:15:00 (112 days).
2026-06-19 06:55:49,545 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8237 - after: 11497 - 39.58%
2026-06-19 06:55:49,545 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-01 16:00:00 (119 days).
2026-06-19 06:55:50,204 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8399 - after: 11851 - 41.10%
2026-06-19 06:55:50,205 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-05 08:30:00 (123 days).
2026-06-19 06:55:50,878 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8731 - after: 12183 - 39.54%
2026-06-19 06:55:50,879 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-08 19:30:00 (126 days).
2026-06-19 06:55:51,554 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8773 - after: 12225 - 39.35%
2026-06-19 06:55:51,556 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-09 06:00:00 (127 days).
2026-06-19 06:55:52,171 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8875 - after: 12519 - 41.06%
2026-06-19 06:55:52,172 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-12 07:30:00 (130 days).
2026-06-19 06:55:52,955 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8921 - after: 12565 - 40.85%
2026-06-19 06:55:52,956 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-12 19:00:00 (130 days).
2026-06-19 06:55:53,920 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9020 - after: 12664 - 40.40%
2026-06-19 06:55:53,921 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-13 19:45:00 (131 days).
2026-06-19 06:55:54,673 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9024 - after: 12668 - 40.38%
2026-06-19 06:55:54,674 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-13 20:45:00 (131 days).
2026-06-19 06:55:55,392 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9526 - after: 13362 - 40.27%
2026-06-19 06:55:55,393 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-21 02:15:00 (139 days).
2026-06-19 06:55:56,189 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9611 - after: 13447 - 39.91%
2026-06-19 06:55:56,190 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-21 23:30:00 (140 days).
2026-06-19 06:55:56,864 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10317 - after: 14537 - 40.90%
2026-06-19 06:55:56,865 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-02 08:00:00 (151 days).
2026-06-19 06:55:57,662 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10406 - after: 14626 - 40.55%
2026-06-19 06:55:57,663 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-03 06:15:00 (152 days).
2026-06-19 06:55:58,451 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11087 - after: 15499 - 39.79%
2026-06-19 06:55:58,452 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-12 08:30:00 (161 days).
2026-06-19 06:55:59,388 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11094 - after: 15506 - 39.77%
2026-06-19 06:55:59,389 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-12 10:15:00 (161 days).
2026-06-19 06:56:00,243 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11541 - after: 16145 - 39.89%
2026-06-19 06:56:00,244 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-19 02:00:00 (168 days).
2026-06-19 06:56:01,188 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11545 - after: 16149 - 39.88%
2026-06-19 06:56:01,189 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-19 03:00:00 (168 days).
2026-06-19 06:56:02,029 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11797 - after: 16593 - 40.65%
2026-06-19 06:56:02,029 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-23 18:00:00 (172 days).
2026-06-19 06:56:02,959 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11815 - after: 16611 - 40.59%
2026-06-19 06:56:02,960 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-23 22:30:00 (173 days).
2026-06-19 06:56:03,906 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 12026 - after: 16822 - 39.88%
2026-06-19 06:56:03,907 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-26 03:15:00 (175 days).
2026-06-19 06:56:04,898 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 12049 - after: 16845 - 39.80%
2026-06-19 06:56:04,899 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-26 09:00:00 (175 days).
2026-06-19 06:56:05,807 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13320 - after: 18692 - 40.33%
2026-06-19 06:56:05,808 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-15 14:45:00 (194 days).
2026-06-19 06:56:06,890 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13461 - after: 18833 - 39.91%
2026-06-19 06:56:06,891 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-17 02:00:00 (196 days).
2026-06-19 06:56:07,850 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13803 - after: 19367 - 40.31%
2026-06-19 06:56:07,851 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-22 15:30:00 (201 days).
2026-06-19 06:56:09,056 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13902 - after: 19466 - 40.02%
2026-06-19 06:56:09,057 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-23 16:15:00 (202 days).
2026-06-19 06:56:10,151 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14181 - after: 19937 - 40.59%
2026-06-19 06:56:10,152 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-28 14:00:00 (207 days).
2026-06-19 06:56:11,292 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14561 - after: 20317 - 39.53%
2026-06-19 06:56:11,294 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-01 13:00:00 (211 days).
2026-06-19 06:56:12,374 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14859 - after: 20807 - 40.03%
2026-06-19 06:56:12,375 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-06 15:30:00 (216 days).
2026-06-19 06:56:13,777 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14862 - after: 20810 - 40.02%
2026-06-19 06:56:13,778 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-06 16:15:00 (216 days).
2026-06-19 06:56:15,078 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17082 - after: 23990 - 40.44%
2026-06-19 06:56:15,079 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-08 19:15:00 (249 days).
2026-06-19 06:56:16,684 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17205 - after: 24113 - 40.15%
2026-06-19 06:56:16,685 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-10 02:00:00 (251 days).
2026-06-19 06:56:17,915 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17620 - after: 24720 - 40.30%
2026-06-19 06:56:17,916 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-16 09:45:00 (257 days).
2026-06-19 06:56:19,634 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17651 - after: 24751 - 40.22%
2026-06-19 06:56:19,636 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-16 17:30:00 (257 days).
2026-06-19 06:56:20,970 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17828 - after: 24928 - 39.82%
2026-06-19 06:56:20,971 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-18 13:45:00 (259 days).
2026-06-19 06:56:22,353 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17895 - after: 24995 - 39.68%
2026-06-19 06:56:22,354 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-19 06:30:00 (260 days).
2026-06-19 06:56:23,665 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 18323 - after: 25615 - 39.80%
2026-06-19 06:56:23,666 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-25 17:30:00 (266 days).
2026-06-19 06:56:25,334 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 18409 - after: 25701 - 39.61%
2026-06-19 06:56:25,336 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-26 15:00:00 (267 days).
2026-06-19 06:56:26,798 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19271 - after: 26947 - 39.83%
2026-06-19 06:56:26,800 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-09 14:30:00 (280 days).
2026-06-19 06:56:28,310 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19359 - after: 27035 - 39.65%
2026-06-19 06:56:28,311 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-10 12:30:00 (281 days).
2026-06-19 06:56:30,213 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19762 - after: 27630 - 39.81%
2026-06-19 06:56:30,214 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-16 17:15:00 (287 days).
2026-06-19 06:56:31,758 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19792 - after: 27660 - 39.75%
2026-06-19 06:56:31,759 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-17 00:45:00 (288 days).
2026-06-19 06:56:33,173 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20120 - after: 28180 - 40.06%
2026-06-19 06:56:33,174 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-22 10:45:00 (293 days).
2026-06-19 06:56:34,788 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20127 - after: 28187 - 40.05%
2026-06-19 06:56:34,789 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-22 12:30:00 (293 days).
2026-06-19 06:56:36,902 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20996 - after: 29444 - 40.24%
2026-06-19 06:56:36,903 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-04 14:45:00 (306 days).
2026-06-19 06:56:38,515 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 21040 - after: 29488 - 40.15%
2026-06-19 06:56:38,516 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-05 01:45:00 (307 days).
2026-06-19 06:56:40,574 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 21473 - after: 30113 - 40.24%
2026-06-19 06:56:40,575 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-11 14:00:00 (313 days).
2026-06-19 06:56:42,355 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 21507 - after: 30147 - 40.17%
2026-06-19 06:56:42,357 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-11 22:30:00 (314 days).
2026-06-19 06:56:43,898 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 23514 - after: 32922 - 40.01%
2026-06-19 06:56:43,899 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-10 20:15:00 (342 days).
2026-06-19 06:56:46,147 - freqtrade.optimize.analysis.lookahead - INFO - found force-exit in pair: EUR/USDT, timerange:2025-12-11 00:15:00+00:00-2025-12-31 21:45:00+00:00, idx: 46, skipping this one 
to avoid a false-positive.
2026-06-19 06:56:46,148 - freqtrade.loggers.set_log_levels - INFO - Restoring log verbosity.
2026-06-19 06:56:46,149 - freqtrade.optimize.analysis.lookahead - INFO - LIB_STR053: no bias detected
2026-06-19 06:56:46,149 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Checking look ahead bias via backtests of LIB_STR053.py took 81 seconds.

```


**رمز الخروج:** 0
