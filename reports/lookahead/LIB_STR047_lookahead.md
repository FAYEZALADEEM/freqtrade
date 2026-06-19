# تقرير Lookahead Analysis: LIB_STR047

**التاريخ:** 2026-06-19 06:50
**الأمر:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade lookahead-analysis --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --config <(echo '{"entry_pricing": {"price_side": "other"}, "exit_pricing": {"price_side": "other"}}') --strategy LIB_STR047 --timeframe 15m --timerange 20250101-20260101 --fee 0 --targeted-trade-amount 100 -p EUR/USDT
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
│ LIB_STR047.py │ LIB_STR047 │       No │            46 │                    0 │                   0 │                   │
└───────────────┴────────────┴──────────┴───────────────┴──────────────────────┴─────────────────────┴───────────────────┘

2026-06-19 06:48:50,721 - freqtrade - INFO - freqtrade 2026.6-dev-a29762684
2026-06-19 06:48:51,057 - numexpr.utils - INFO - NumExpr defaulting to 8 threads.
2026-06-19 06:48:51,974 - freqtrade.configuration.load_config - INFO - Using config: user_data/config.json ...
2026-06-19 06:48:51,975 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/63 ...
2026-06-19 06:48:51,975 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/62 ...
2026-06-19 06:48:51,979 - freqtrade.loggers - INFO - Enabling colorized output.
2026-06-19 06:48:51,980 - freqtrade.loggers - INFO - Logfile configured
2026-06-19 06:48:51,980 - freqtrade.loggers - INFO - Verbosity set to 0
2026-06-19 06:48:51,981 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2026-06-19 06:48:51,981 - freqtrade.configuration.configuration - INFO - Parameter --fee detected, setting fee to: 0.0 ...
2026-06-19 06:48:51,982 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20250101-20260101 ...
2026-06-19 06:48:51,982 - freqtrade.configuration.configuration - INFO - Using user-data directory: /home/fayez/freqtrade/user_data ...
2026-06-19 06:48:51,983 - freqtrade.configuration.configuration - INFO - Using data directory: /home/fayez/freqtrade/user_data/data/binance ...
2026-06-19 06:48:51,983 - freqtrade.configuration.configuration - INFO - Using pairs ['EUR/USDT']
2026-06-19 06:48:51,984 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20250101-20260101
2026-06-19 06:48:51,984 - freqtrade.configuration.configuration - INFO - Targeted Trade amount: 100
2026-06-19 06:48:51,985 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2026-06-19 06:48:51,996 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2026-06-19 06:48:51,996 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2026-06-19 06:48:52,000 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Forced order_types to market orders.
2026-06-19 06:48:52,000 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Forced max_open_trades to -1 (same amount as there are pairs)
2026-06-19 06:48:52,001 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Dry run wallet was not set to 1 billion, pushing it up there just to avoid false positives
2026-06-19 06:48:52,001 - freqtrade.optimize.analysis.lookahead_helpers - INFO - fixing stake_amount to 10k
2026-06-19 06:48:52,012 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR072.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR072.py, line 34)'
2026-06-19 06:48:52,012 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR069.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR069.py, line 34)'
2026-06-19 06:48:52,016 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR061.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR061.py, line 34)'
2026-06-19 06:48:52,017 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR062.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR062.py, line 34)'
2026-06-19 06:48:52,019 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR060.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR060.py, line 34)'
2026-06-19 06:48:52,020 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR074.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR074.py, line 34)'
2026-06-19 06:48:52,021 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR068.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR068.py, line 34)'
2026-06-19 06:48:52,024 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR073.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR073.py, line 34)'
2026-06-19 06:48:52,028 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR071.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR071.py, line 34)'
2026-06-19 06:48:52,032 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR065.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR065.py, line 34)'
2026-06-19 06:48:52,033 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Bias test of LIB_STR047.py started.
2026-06-19 06:48:52,034 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2026-06-19 06:48:52,035 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.58
2026-06-19 06:48:52,048 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2026-06-19 06:48:53,465 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2026-06-19 06:48:53,468 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy LIB_STR047 from '/home/fayez/freqtrade/user_data/strategies/LIB_STR047.py'...
2026-06-19 06:48:53,468 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2026-06-19 06:48:53,469 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value from the configuration: 15m.
2026-06-19 06:48:53,469 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'order_types' with value from the configuration: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 
'stoploss_on_exchange': False}.
2026-06-19 06:48:53,469 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value from the configuration: USDT.
2026-06-19 06:48:53,470 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value from the configuration: 10000.
2026-06-19 06:48:53,470 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value from the configuration: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 
'unit': 'minutes'}.
2026-06-19 06:48:53,470 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value from the configuration: -1.
2026-06-19 06:48:53,470 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.01}
2026-06-19 06:48:53,471 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2026-06-19 06:48:53,471 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.01
2026-06-19 06:48:53,471 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2026-06-19 06:48:53,471 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2026-06-19 06:48:53,472 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2026-06-19 06:48:53,472 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: False
2026-06-19 06:48:53,472 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2026-06-19 06:48:53,472 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 'stoploss_on_exchange': False}
2026-06-19 06:48:53,473 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2026-06-19 06:48:53,473 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2026-06-19 06:48:53,473 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: 10000
2026-06-19 06:48:53,473 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2026-06-19 06:48:53,474 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2026-06-19 06:48:53,474 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2026-06-19 06:48:53,474 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2026-06-19 06:48:53,474 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2026-06-19 06:48:53,475 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2026-06-19 06:48:53,475 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2026-06-19 06:48:53,475 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2026-06-19 06:48:53,475 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2026-06-19 06:48:53,476 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2026-06-19 06:48:53,476 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: -1
2026-06-19 06:48:53,476 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2026-06-19 06:48:53,479 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/home/fayez/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2026-06-19 06:48:53,492 - freqtrade.optimize.backtesting - INFO - Using fee 0.0000% from config.
2026-06-19 06:48:53,541 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 24900 - after: 34944 - 40.34%
2026-06-19 06:48:53,542 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-31 21:45:00 (363 days).
2026-06-19 06:48:55,474 - freqtrade.loggers.set_log_levels - INFO - Reducing verbosity for bias tester.
2026-06-19 06:48:55,474 - freqtrade.optimize.analysis.lookahead - INFO - Only found 48 trades. Calculating all available trades.
2026-06-19 06:48:55,533 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-02 09:00:00 (0 days).
2026-06-19 06:48:55,646 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-02 16:15:00 (0 days).
2026-06-19 06:48:55,798 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-03 05:45:00 (1 days).
2026-06-19 06:48:55,886 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 246 - after: 438 - 78.05%
2026-06-19 06:48:55,887 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-06 11:15:00 (4 days).
2026-06-19 06:48:56,073 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 247 - after: 439 - 77.73%
2026-06-19 06:48:56,074 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-06 11:30:00 (4 days).
2026-06-19 06:48:56,223 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 440 - after: 632 - 43.64%
2026-06-19 06:48:56,224 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-08 11:45:00 (6 days).
2026-06-19 06:48:56,433 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 528 - after: 720 - 36.36%
2026-06-19 06:48:56,434 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-09 09:45:00 (7 days).
2026-06-19 06:48:56,586 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 700 - after: 1084 - 54.86%
2026-06-19 06:48:56,588 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-13 04:45:00 (11 days).
2026-06-19 06:48:56,771 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 841 - after: 1225 - 45.66%
2026-06-19 06:48:56,772 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-14 16:00:00 (12 days).
2026-06-19 06:48:56,928 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1216 - after: 1792 - 47.37%
2026-06-19 06:48:56,929 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-20 13:45:00 (18 days).
2026-06-19 06:48:57,138 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1287 - after: 1863 - 44.76%
2026-06-19 06:48:57,139 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-21 07:30:00 (19 days).
2026-06-19 06:48:57,329 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1578 - after: 2154 - 36.50%
2026-06-19 06:48:57,330 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-24 08:15:00 (22 days).
2026-06-19 06:48:57,655 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1773 - after: 2541 - 43.32%
2026-06-19 06:48:57,656 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-28 09:00:00 (26 days).
2026-06-19 06:48:57,943 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2114 - after: 3074 - 45.41%
2026-06-19 06:48:57,944 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-02 22:15:00 (32 days).
2026-06-19 06:48:58,318 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2254 - after: 3214 - 42.59%
2026-06-19 06:48:58,320 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-04 09:15:00 (33 days).
2026-06-19 06:48:58,569 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2374 - after: 3334 - 40.44%
2026-06-19 06:48:58,569 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-05 15:15:00 (34 days).
2026-06-19 06:48:58,875 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2760 - after: 3912 - 41.74%
2026-06-19 06:48:58,875 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-11 15:45:00 (40 days).
2026-06-19 06:48:59,150 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2955 - after: 4107 - 38.98%
2026-06-19 06:48:59,151 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-13 16:30:00 (42 days).
2026-06-19 06:48:59,433 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 3015 - after: 4167 - 38.21%
2026-06-19 06:48:59,434 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-14 07:30:00 (43 days).
2026-06-19 06:48:59,694 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4019 - after: 5555 - 38.22%
2026-06-19 06:48:59,695 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-28 18:30:00 (57 days).
2026-06-19 06:49:00,044 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4103 - after: 5831 - 42.12%
2026-06-19 06:49:00,045 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-03 15:30:00 (60 days).
2026-06-19 06:49:00,358 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4214 - after: 5942 - 41.01%
2026-06-19 06:49:00,358 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-04 19:15:00 (61 days).
2026-06-19 06:49:00,736 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4264 - after: 5992 - 40.53%
2026-06-19 06:49:00,737 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-05 07:45:00 (62 days).
2026-06-19 06:49:01,089 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4292 - after: 6020 - 40.26%
2026-06-19 06:49:01,091 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-05 14:45:00 (62 days).
2026-06-19 06:49:01,644 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4515 - after: 6431 - 42.44%
2026-06-19 06:49:01,645 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-09 21:30:00 (66 days).
2026-06-19 06:49:02,234 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4694 - after: 6610 - 40.82%
2026-06-19 06:49:02,235 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-11 18:15:00 (68 days).
2026-06-19 06:49:02,671 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4735 - after: 6651 - 40.46%
2026-06-19 06:49:02,672 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-12 04:30:00 (69 days).
2026-06-19 06:49:03,068 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 5552 - after: 7852 - 41.43%
2026-06-19 06:49:03,069 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-24 16:45:00 (81 days).
2026-06-19 06:49:03,544 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 5626 - after: 7926 - 40.88%
2026-06-19 06:49:03,545 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-25 11:15:00 (82 days).
2026-06-19 06:49:04,018 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6275 - after: 8767 - 39.71%
2026-06-19 06:49:04,019 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 05:30:00 (91 days).
2026-06-19 06:49:04,548 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6334 - after: 8826 - 39.34%
2026-06-19 06:49:04,549 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 20:15:00 (91 days).
2026-06-19 06:49:05,031 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6434 - after: 9118 - 41.72%
2026-06-19 06:49:05,032 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-06 21:15:00 (94 days).
2026-06-19 06:49:05,567 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6470 - after: 9154 - 41.48%
2026-06-19 06:49:05,568 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-07 06:15:00 (95 days).
2026-06-19 06:49:06,069 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6506 - after: 9190 - 41.25%
2026-06-19 06:49:06,070 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-07 15:15:00 (95 days).
2026-06-19 06:49:06,995 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6569 - after: 9253 - 40.86%
2026-06-19 06:49:06,996 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-08 07:00:00 (96 days).
2026-06-19 06:49:07,588 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6783 - after: 9467 - 39.57%
2026-06-19 06:49:07,589 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 12:30:00 (98 days).
2026-06-19 06:49:08,208 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6796 - after: 9480 - 39.49%
2026-06-19 06:49:08,209 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 15:45:00 (98 days).
2026-06-19 06:49:09,010 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6832 - after: 9516 - 39.29%
2026-06-19 06:49:09,011 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 00:45:00 (99 days).
2026-06-19 06:49:09,732 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6857 - after: 9541 - 39.14%
2026-06-19 06:49:09,733 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 07:00:00 (99 days).
2026-06-19 06:49:10,243 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6862 - after: 9546 - 39.11%
2026-06-19 06:49:10,244 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 08:15:00 (99 days).
2026-06-19 06:49:10,784 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7119 - after: 9995 - 40.40%
2026-06-19 06:49:10,785 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-16 00:30:00 (104 days).
2026-06-19 06:49:11,342 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7398 - after: 10466 - 41.47%
2026-06-19 06:49:11,343 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-20 22:15:00 (109 days).
2026-06-19 06:49:12,336 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7524 - after: 10592 - 40.78%
2026-06-19 06:49:12,337 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-22 05:45:00 (110 days).
2026-06-19 06:49:13,267 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7570 - after: 10638 - 40.53%
2026-06-19 06:49:13,269 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-22 17:15:00 (110 days).
2026-06-19 06:49:14,139 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7726 - after: 10794 - 39.71%
2026-06-19 06:49:14,140 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-24 08:15:00 (112 days).
2026-06-19 06:49:14,714 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8237 - after: 11497 - 39.58%
2026-06-19 06:49:14,715 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-01 16:00:00 (119 days).
2026-06-19 06:49:15,454 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8399 - after: 11851 - 41.10%
2026-06-19 06:49:15,455 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-05 08:30:00 (123 days).
2026-06-19 06:49:16,472 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8731 - after: 12183 - 39.54%
2026-06-19 06:49:16,473 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-08 19:30:00 (126 days).
2026-06-19 06:49:17,536 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8773 - after: 12225 - 39.35%
2026-06-19 06:49:17,537 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-09 06:00:00 (127 days).
2026-06-19 06:49:18,501 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8875 - after: 12519 - 41.06%
2026-06-19 06:49:18,502 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-12 07:30:00 (130 days).
2026-06-19 06:49:19,197 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8921 - after: 12565 - 40.85%
2026-06-19 06:49:19,198 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-12 19:00:00 (130 days).
2026-06-19 06:49:19,854 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9020 - after: 12664 - 40.40%
2026-06-19 06:49:19,855 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-13 19:45:00 (131 days).
2026-06-19 06:49:20,549 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9024 - after: 12668 - 40.38%
2026-06-19 06:49:20,549 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-13 20:45:00 (131 days).
2026-06-19 06:49:21,224 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9526 - after: 13362 - 40.27%
2026-06-19 06:49:21,225 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-21 02:15:00 (139 days).
2026-06-19 06:49:22,224 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9611 - after: 13447 - 39.91%
2026-06-19 06:49:22,226 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-21 23:30:00 (140 days).
2026-06-19 06:49:23,027 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10317 - after: 14537 - 40.90%
2026-06-19 06:49:23,027 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-02 08:00:00 (151 days).
2026-06-19 06:49:23,873 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10406 - after: 14626 - 40.55%
2026-06-19 06:49:23,875 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-03 06:15:00 (152 days).
2026-06-19 06:49:24,640 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11087 - after: 15499 - 39.79%
2026-06-19 06:49:24,641 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-12 08:30:00 (161 days).
2026-06-19 06:49:25,486 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11094 - after: 15506 - 39.77%
2026-06-19 06:49:25,487 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-12 10:15:00 (161 days).
2026-06-19 06:49:26,285 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11541 - after: 16145 - 39.89%
2026-06-19 06:49:26,286 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-19 02:00:00 (168 days).
2026-06-19 06:49:27,218 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11545 - after: 16149 - 39.88%
2026-06-19 06:49:27,219 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-19 03:00:00 (168 days).
2026-06-19 06:49:28,135 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11797 - after: 16593 - 40.65%
2026-06-19 06:49:28,136 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-23 18:00:00 (172 days).
2026-06-19 06:49:29,118 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11815 - after: 16611 - 40.59%
2026-06-19 06:49:29,119 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-23 22:30:00 (173 days).
2026-06-19 06:49:29,991 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 12026 - after: 16822 - 39.88%
2026-06-19 06:49:29,991 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-26 03:15:00 (175 days).
2026-06-19 06:49:30,911 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 12049 - after: 16845 - 39.80%
2026-06-19 06:49:30,912 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-26 09:00:00 (175 days).
2026-06-19 06:49:31,837 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13320 - after: 18692 - 40.33%
2026-06-19 06:49:31,839 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-15 14:45:00 (194 days).
2026-06-19 06:49:33,124 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13461 - after: 18833 - 39.91%
2026-06-19 06:49:33,125 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-17 02:00:00 (196 days).
2026-06-19 06:49:34,535 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13803 - after: 19367 - 40.31%
2026-06-19 06:49:34,536 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-22 15:30:00 (201 days).
2026-06-19 06:49:35,646 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13902 - after: 19466 - 40.02%
2026-06-19 06:49:35,647 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-23 16:15:00 (202 days).
2026-06-19 06:49:36,647 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14181 - after: 19937 - 40.59%
2026-06-19 06:49:36,648 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-28 14:00:00 (207 days).
2026-06-19 06:49:37,752 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14561 - after: 20317 - 39.53%
2026-06-19 06:49:37,753 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-01 13:00:00 (211 days).
2026-06-19 06:49:39,011 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14859 - after: 20807 - 40.03%
2026-06-19 06:49:39,012 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-06 15:30:00 (216 days).
2026-06-19 06:49:40,225 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14862 - after: 20810 - 40.02%
2026-06-19 06:49:40,226 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-06 16:15:00 (216 days).
2026-06-19 06:49:41,318 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17082 - after: 23990 - 40.44%
2026-06-19 06:49:41,318 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-08 19:15:00 (249 days).
2026-06-19 06:49:42,635 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17205 - after: 24113 - 40.15%
2026-06-19 06:49:42,636 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-10 02:00:00 (251 days).
2026-06-19 06:49:43,892 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17620 - after: 24720 - 40.30%
2026-06-19 06:49:43,893 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-16 09:45:00 (257 days).
2026-06-19 06:49:45,352 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17651 - after: 24751 - 40.22%
2026-06-19 06:49:45,353 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-16 17:30:00 (257 days).
2026-06-19 06:49:46,651 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17828 - after: 24928 - 39.82%
2026-06-19 06:49:46,652 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-18 13:45:00 (259 days).
2026-06-19 06:49:48,000 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17895 - after: 24995 - 39.68%
2026-06-19 06:49:48,001 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-19 06:30:00 (260 days).
2026-06-19 06:49:49,562 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 18323 - after: 25615 - 39.80%
2026-06-19 06:49:49,563 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-25 17:30:00 (266 days).
2026-06-19 06:49:51,239 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 18409 - after: 25701 - 39.61%
2026-06-19 06:49:51,240 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-26 15:00:00 (267 days).
2026-06-19 06:49:52,586 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19271 - after: 26947 - 39.83%
2026-06-19 06:49:52,587 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-09 14:30:00 (280 days).
2026-06-19 06:49:54,089 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19359 - after: 27035 - 39.65%
2026-06-19 06:49:54,089 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-10 12:30:00 (281 days).
2026-06-19 06:49:55,559 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19762 - after: 27630 - 39.81%
2026-06-19 06:49:55,560 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-16 17:15:00 (287 days).
2026-06-19 06:49:57,135 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19792 - after: 27660 - 39.75%
2026-06-19 06:49:57,135 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-17 00:45:00 (288 days).
2026-06-19 06:49:58,582 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20120 - after: 28180 - 40.06%
2026-06-19 06:49:58,582 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-22 10:45:00 (293 days).
2026-06-19 06:50:00,511 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20127 - after: 28187 - 40.05%
2026-06-19 06:50:00,512 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-22 12:30:00 (293 days).
2026-06-19 06:50:02,067 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20996 - after: 29444 - 40.24%
2026-06-19 06:50:02,068 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-04 14:45:00 (306 days).
2026-06-19 06:50:03,650 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 21040 - after: 29488 - 40.15%
2026-06-19 06:50:03,651 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-05 01:45:00 (307 days).
2026-06-19 06:50:05,284 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 21473 - after: 30113 - 40.24%
2026-06-19 06:50:05,285 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-11 14:00:00 (313 days).
2026-06-19 06:50:06,957 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 21507 - after: 30147 - 40.17%
2026-06-19 06:50:06,958 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-11 22:30:00 (314 days).
2026-06-19 06:50:08,530 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 23514 - after: 32922 - 40.01%
2026-06-19 06:50:08,531 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-10 20:15:00 (342 days).
2026-06-19 06:50:10,352 - freqtrade.optimize.analysis.lookahead - INFO - found force-exit in pair: EUR/USDT, timerange:2025-12-11 00:15:00+00:00-2025-12-31 21:45:00+00:00, idx: 46, skipping this one 
to avoid a false-positive.
2026-06-19 06:50:10,352 - freqtrade.loggers.set_log_levels - INFO - Restoring log verbosity.
2026-06-19 06:50:10,352 - freqtrade.optimize.analysis.lookahead - INFO - LIB_STR047: no bias detected
2026-06-19 06:50:10,353 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Checking look ahead bias via backtests of LIB_STR047.py took 78 seconds.

```


**رمز الخروج:** 0
