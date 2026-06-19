# تقرير Lookahead Analysis: LIB_STR054

**التاريخ:** 2026-06-19 06:57
**الأمر:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade lookahead-analysis --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --config <(echo '{"entry_pricing": {"price_side": "other"}, "exit_pricing": {"price_side": "other"}}') --strategy LIB_STR054 --timeframe 15m --timerange 20250101-20260101 --fee 0 --targeted-trade-amount 100 -p EUR/USDT
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
│ LIB_STR054.py │ LIB_STR054 │      Yes │            59 │                    1 │                   0 │                   │
└───────────────┴────────────┴──────────┴───────────────┴──────────────────────┴─────────────────────┴───────────────────┘

2026-06-19 06:55:23,726 - freqtrade - INFO - freqtrade 2026.6-dev-a29762684
2026-06-19 06:55:24,096 - numexpr.utils - INFO - NumExpr defaulting to 8 threads.
2026-06-19 06:55:25,243 - freqtrade.configuration.load_config - INFO - Using config: user_data/config.json ...
2026-06-19 06:55:25,244 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/63 ...
2026-06-19 06:55:25,244 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/62 ...
2026-06-19 06:55:25,246 - freqtrade.loggers - INFO - Enabling colorized output.
2026-06-19 06:55:25,247 - freqtrade.loggers - INFO - Logfile configured
2026-06-19 06:55:25,247 - freqtrade.loggers - INFO - Verbosity set to 0
2026-06-19 06:55:25,247 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2026-06-19 06:55:25,248 - freqtrade.configuration.configuration - INFO - Parameter --fee detected, setting fee to: 0.0 ...
2026-06-19 06:55:25,248 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20250101-20260101 ...
2026-06-19 06:55:25,248 - freqtrade.configuration.configuration - INFO - Using user-data directory: /home/fayez/freqtrade/user_data ...
2026-06-19 06:55:25,249 - freqtrade.configuration.configuration - INFO - Using data directory: /home/fayez/freqtrade/user_data/data/binance ...
2026-06-19 06:55:25,249 - freqtrade.configuration.configuration - INFO - Using pairs ['EUR/USDT']
2026-06-19 06:55:25,249 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20250101-20260101
2026-06-19 06:55:25,250 - freqtrade.configuration.configuration - INFO - Targeted Trade amount: 100
2026-06-19 06:55:25,250 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2026-06-19 06:55:25,257 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2026-06-19 06:55:25,257 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2026-06-19 06:55:25,259 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Forced order_types to market orders.
2026-06-19 06:55:25,260 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Forced max_open_trades to -1 (same amount as there are pairs)
2026-06-19 06:55:25,260 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Dry run wallet was not set to 1 billion, pushing it up there just to avoid false positives
2026-06-19 06:55:25,260 - freqtrade.optimize.analysis.lookahead_helpers - INFO - fixing stake_amount to 10k
2026-06-19 06:55:25,269 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR072.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR072.py, line 34)'
2026-06-19 06:55:25,270 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR069.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR069.py, line 34)'
2026-06-19 06:55:25,274 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR061.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR061.py, line 34)'
2026-06-19 06:55:25,275 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR062.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR062.py, line 34)'
2026-06-19 06:55:25,276 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR060.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR060.py, line 34)'
2026-06-19 06:55:25,278 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR074.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR074.py, line 34)'
2026-06-19 06:55:25,279 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR068.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR068.py, line 34)'
2026-06-19 06:55:25,282 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR073.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR073.py, line 34)'
2026-06-19 06:55:25,287 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR071.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR071.py, line 34)'
2026-06-19 06:55:25,291 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR065.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR065.py, line 34)'
2026-06-19 06:55:25,292 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Bias test of LIB_STR054.py started.
2026-06-19 06:55:25,293 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2026-06-19 06:55:25,293 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.58
2026-06-19 06:55:25,308 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2026-06-19 06:55:26,968 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2026-06-19 06:55:26,973 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy LIB_STR054 from '/home/fayez/freqtrade/user_data/strategies/LIB_STR054.py'...
2026-06-19 06:55:26,974 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2026-06-19 06:55:26,975 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value from the configuration: 15m.
2026-06-19 06:55:26,975 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'order_types' with value from the configuration: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 
'stoploss_on_exchange': False}.
2026-06-19 06:55:26,975 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value from the configuration: USDT.
2026-06-19 06:55:26,976 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value from the configuration: 10000.
2026-06-19 06:55:26,976 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value from the configuration: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 
'unit': 'minutes'}.
2026-06-19 06:55:26,977 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value from the configuration: -1.
2026-06-19 06:55:26,977 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.01}
2026-06-19 06:55:26,978 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2026-06-19 06:55:26,978 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.01
2026-06-19 06:55:26,978 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2026-06-19 06:55:26,979 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2026-06-19 06:55:26,979 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2026-06-19 06:55:26,979 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: False
2026-06-19 06:55:26,980 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2026-06-19 06:55:26,980 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 'stoploss_on_exchange': False}
2026-06-19 06:55:26,981 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2026-06-19 06:55:26,981 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2026-06-19 06:55:26,981 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: 10000
2026-06-19 06:55:26,982 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2026-06-19 06:55:26,982 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2026-06-19 06:55:26,983 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2026-06-19 06:55:26,983 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2026-06-19 06:55:26,983 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2026-06-19 06:55:26,984 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2026-06-19 06:55:26,984 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2026-06-19 06:55:26,984 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2026-06-19 06:55:26,985 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2026-06-19 06:55:26,985 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2026-06-19 06:55:26,986 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: -1
2026-06-19 06:55:26,986 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2026-06-19 06:55:26,992 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/home/fayez/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2026-06-19 06:55:27,015 - freqtrade.optimize.backtesting - INFO - Using fee 0.0000% from config.
2026-06-19 06:55:27,074 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 24900 - after: 34944 - 40.34%
2026-06-19 06:55:27,075 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-31 21:45:00 (363 days).
2026-06-19 06:55:30,032 - freqtrade.loggers.set_log_levels - INFO - Reducing verbosity for bias tester.
2026-06-19 06:55:30,033 - freqtrade.optimize.analysis.lookahead - INFO - Only found 61 trades. Calculating all available trades.
2026-06-19 06:55:30,081 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-02 03:30:00 (0 days).
2026-06-19 06:55:30,199 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-02 16:15:00 (0 days).
2026-06-19 06:55:30,343 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-03 01:15:00 (1 days).
2026-06-19 06:55:30,442 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 246 - after: 438 - 78.05%
2026-06-19 06:55:30,443 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-06 11:15:00 (4 days).
2026-06-19 06:55:30,574 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 247 - after: 439 - 77.73%
2026-06-19 06:55:30,575 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-06 11:30:00 (4 days).
2026-06-19 06:55:30,678 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 440 - after: 632 - 43.64%
2026-06-19 06:55:30,679 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-08 11:45:00 (6 days).
2026-06-19 06:55:30,827 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 462 - after: 654 - 41.56%
2026-06-19 06:55:30,828 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-08 17:15:00 (6 days).
2026-06-19 06:55:30,951 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 700 - after: 1084 - 54.86%
2026-06-19 06:55:30,951 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-13 04:45:00 (11 days).
2026-06-19 06:55:31,119 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 768 - after: 1152 - 50.00%
2026-06-19 06:55:31,120 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-13 21:45:00 (11 days).
2026-06-19 06:55:31,261 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 928 - after: 1312 - 41.38%
2026-06-19 06:55:31,262 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-15 13:45:00 (13 days).
2026-06-19 06:55:31,460 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 929 - after: 1313 - 41.33%
2026-06-19 06:55:31,461 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-15 14:00:00 (13 days).
2026-06-19 06:55:31,630 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1242 - after: 1818 - 46.38%
2026-06-19 06:55:31,630 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-20 20:15:00 (18 days).
2026-06-19 06:55:31,847 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1313 - after: 1889 - 43.87%
2026-06-19 06:55:31,848 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-21 14:00:00 (19 days).
2026-06-19 06:55:32,032 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1578 - after: 2154 - 36.50%
2026-06-19 06:55:32,033 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-24 08:15:00 (22 days).
2026-06-19 06:55:32,278 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1579 - after: 2155 - 36.48%
2026-06-19 06:55:32,279 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-24 08:30:00 (22 days).
2026-06-19 06:55:32,493 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2062 - after: 2830 - 37.25%
2026-06-19 06:55:32,494 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-31 09:15:00 (29 days).
2026-06-19 06:55:32,864 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2090 - after: 2858 - 36.75%
2026-06-19 06:55:32,865 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-31 16:15:00 (29 days).
2026-06-19 06:55:33,140 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2114 - after: 3074 - 45.41%
2026-06-19 06:55:33,141 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-02 22:15:00 (32 days).
2026-06-19 06:55:33,475 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2172 - after: 3132 - 44.20%
2026-06-19 06:55:33,476 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-03 12:45:00 (32 days).
2026-06-19 06:55:33,748 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2278 - after: 3238 - 42.14%
2026-06-19 06:55:33,749 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-04 15:15:00 (33 days).
2026-06-19 06:55:34,117 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2281 - after: 3241 - 42.09%
2026-06-19 06:55:34,118 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-04 16:00:00 (33 days).
2026-06-19 06:55:34,523 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 3020 - after: 4172 - 38.15%
2026-06-19 06:55:34,524 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-14 08:45:00 (43 days).
2026-06-19 06:55:35,050 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 3021 - after: 4173 - 38.13%
2026-06-19 06:55:35,051 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-14 09:00:00 (43 days).
2026-06-19 06:55:35,474 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 3955 - after: 5491 - 38.84%
2026-06-19 06:55:35,475 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-28 02:30:00 (57 days).
2026-06-19 06:55:36,123 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 3977 - after: 5513 - 38.62%
2026-06-19 06:55:36,124 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-28 08:00:00 (57 days).
2026-06-19 06:55:36,732 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4102 - after: 5830 - 42.13%
2026-06-19 06:55:36,733 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-03 15:15:00 (60 days).
2026-06-19 06:55:37,414 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4103 - after: 5831 - 42.12%
2026-06-19 06:55:37,415 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-03 15:30:00 (60 days).
2026-06-19 06:55:37,831 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4214 - after: 5942 - 41.01%
2026-06-19 06:55:37,833 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-04 19:15:00 (61 days).
2026-06-19 06:55:38,439 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4218 - after: 5946 - 40.97%
2026-06-19 06:55:38,440 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-04 20:15:00 (61 days).
2026-06-19 06:55:38,924 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4270 - after: 5998 - 40.47%
2026-06-19 06:55:38,925 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-05 09:15:00 (62 days).
2026-06-19 06:55:39,401 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4291 - after: 6019 - 40.27%
2026-06-19 06:55:39,402 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-05 14:30:00 (62 days).
2026-06-19 06:55:39,945 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4383 - after: 6111 - 39.43%
2026-06-19 06:55:39,946 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-06 13:30:00 (63 days).
2026-06-19 06:55:40,422 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4438 - after: 6166 - 38.94%
2026-06-19 06:55:40,423 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-07 03:15:00 (64 days).
2026-06-19 06:55:40,869 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4657 - after: 6573 - 41.14%
2026-06-19 06:55:40,870 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-11 09:00:00 (68 days).
2026-06-19 06:55:41,388 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4658 - after: 6574 - 41.13%
2026-06-19 06:55:41,389 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-11 09:15:00 (68 days).
2026-06-19 06:55:41,862 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 5453 - after: 7561 - 38.66%
2026-06-19 06:55:41,863 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-21 16:00:00 (78 days).
2026-06-19 06:55:42,431 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 5475 - after: 7775 - 42.01%
2026-06-19 06:55:42,432 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-23 21:30:00 (80 days).
2026-06-19 06:55:42,914 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6239 - after: 8731 - 39.94%
2026-06-19 06:55:42,915 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-02 20:30:00 (90 days).
2026-06-19 06:55:43,556 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6261 - after: 8753 - 39.80%
2026-06-19 06:55:43,557 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 02:00:00 (91 days).
2026-06-19 06:55:44,490 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6290 - after: 8782 - 39.62%
2026-06-19 06:55:44,491 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 09:15:00 (91 days).
2026-06-19 06:55:45,309 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6291 - after: 8783 - 39.61%
2026-06-19 06:55:45,310 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 09:30:00 (91 days).
2026-06-19 06:55:45,929 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6294 - after: 8786 - 39.59%
2026-06-19 06:55:45,930 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 10:15:00 (91 days).
2026-06-19 06:55:46,546 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6295 - after: 8787 - 39.59%
2026-06-19 06:55:46,547 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 10:30:00 (91 days).
2026-06-19 06:55:47,096 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6382 - after: 8874 - 39.05%
2026-06-19 06:55:47,097 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-04 08:15:00 (92 days).
2026-06-19 06:55:47,723 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6400 - after: 8892 - 38.94%
2026-06-19 06:55:47,723 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-04 12:45:00 (92 days).
2026-06-19 06:55:48,279 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6408 - after: 8900 - 38.89%
2026-06-19 06:55:48,280 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-04 14:45:00 (92 days).
2026-06-19 06:55:48,927 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6440 - after: 9124 - 41.68%
2026-06-19 06:55:48,928 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-06 22:45:00 (95 days).
2026-06-19 06:55:49,542 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6688 - after: 9372 - 40.13%
2026-06-19 06:55:49,544 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-09 12:45:00 (97 days).
2026-06-19 06:55:50,361 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6689 - after: 9373 - 40.13%
2026-06-19 06:55:50,362 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-09 13:00:00 (97 days).
2026-06-19 06:55:50,994 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6707 - after: 9391 - 40.02%
2026-06-19 06:55:50,995 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-09 17:30:00 (97 days).
2026-06-19 06:55:51,640 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6737 - after: 9421 - 39.84%
2026-06-19 06:55:51,641 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 01:00:00 (98 days).
2026-06-19 06:55:52,202 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6778 - after: 9462 - 39.60%
2026-06-19 06:55:52,203 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 11:15:00 (98 days).
2026-06-19 06:55:52,836 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6783 - after: 9467 - 39.57%
2026-06-19 06:55:52,836 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 12:30:00 (98 days).
2026-06-19 06:55:53,437 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6796 - after: 9480 - 39.49%
2026-06-19 06:55:53,438 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 15:45:00 (98 days).
2026-06-19 06:55:54,137 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6797 - after: 9481 - 39.49%
2026-06-19 06:55:54,138 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 16:00:00 (98 days).
2026-06-19 06:55:54,724 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6832 - after: 9516 - 39.29%
2026-06-19 06:55:54,725 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 00:45:00 (99 days).
2026-06-19 06:55:55,584 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6833 - after: 9517 - 39.28%
2026-06-19 06:55:55,585 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 01:00:00 (99 days).
2026-06-19 06:55:56,233 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6864 - after: 9548 - 39.10%
2026-06-19 06:55:56,233 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 08:45:00 (99 days).
2026-06-19 06:55:56,858 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6865 - after: 9549 - 39.10%
2026-06-19 06:55:56,859 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 09:00:00 (99 days).
2026-06-19 06:55:57,443 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6894 - after: 9578 - 38.93%
2026-06-19 06:55:57,444 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 16:15:00 (99 days).
2026-06-19 06:55:58,226 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6912 - after: 9596 - 38.83%
2026-06-19 06:55:58,227 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 20:45:00 (99 days).
2026-06-19 06:55:59,230 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7406 - after: 10474 - 41.43%
2026-06-19 06:55:59,231 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-21 00:15:00 (109 days).
2026-06-19 06:55:59,976 - freqtrade.optimize.analysis.lookahead - INFO - found lookahead-bias in trade pair: EUR/USDT, timerange:2025-04-11 21:00:00+00:00 - 2025-04-21 00:00:00+00:00, idx: 30
2026-06-19 06:56:00,110 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7407 - after: 10475 - 41.42%
2026-06-19 06:56:00,111 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-21 00:30:00 (109 days).
2026-06-19 06:56:00,972 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7590 - after: 10658 - 40.42%
2026-06-19 06:56:00,972 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-22 22:15:00 (111 days).
2026-06-19 06:56:01,698 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7634 - after: 10702 - 40.19%
2026-06-19 06:56:01,699 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-23 09:15:00 (111 days).
2026-06-19 06:56:02,363 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8194 - after: 11454 - 39.79%
2026-06-19 06:56:02,364 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-01 05:15:00 (119 days).
2026-06-19 06:56:03,169 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8207 - after: 11467 - 39.72%
2026-06-19 06:56:03,170 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-01 08:30:00 (119 days).
2026-06-19 06:56:04,019 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8758 - after: 12210 - 39.42%
2026-06-19 06:56:04,021 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-09 02:15:00 (127 days).
2026-06-19 06:56:05,153 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8773 - after: 12225 - 39.35%
2026-06-19 06:56:05,154 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-09 06:00:00 (127 days).
2026-06-19 06:56:05,939 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8875 - after: 12519 - 41.06%
2026-06-19 06:56:05,940 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-12 07:30:00 (130 days).
2026-06-19 06:56:06,800 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8941 - after: 12585 - 40.76%
2026-06-19 06:56:06,801 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-13 00:00:00 (131 days).
2026-06-19 06:56:07,564 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9068 - after: 12712 - 40.19%
2026-06-19 06:56:07,565 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-14 07:45:00 (132 days).
2026-06-19 06:56:08,696 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9069 - after: 12713 - 40.18%
2026-06-19 06:56:08,697 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-14 08:00:00 (132 days).
2026-06-19 06:56:09,878 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9526 - after: 13362 - 40.27%
2026-06-19 06:56:09,880 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-21 02:15:00 (139 days).
2026-06-19 06:56:11,139 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9527 - after: 13363 - 40.26%
2026-06-19 06:56:11,140 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-21 02:30:00 (139 days).
2026-06-19 06:56:11,987 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10317 - after: 14537 - 40.90%
2026-06-19 06:56:11,988 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-02 08:00:00 (151 days).
2026-06-19 06:56:12,963 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10318 - after: 14538 - 40.90%
2026-06-19 06:56:12,964 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-02 08:15:00 (151 days).
2026-06-19 06:56:13,887 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11087 - after: 15499 - 39.79%
2026-06-19 06:56:13,888 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-12 08:30:00 (161 days).
2026-06-19 06:56:14,875 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11088 - after: 15500 - 39.79%
2026-06-19 06:56:14,875 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-12 08:45:00 (161 days).
2026-06-19 06:56:15,879 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11992 - after: 16788 - 39.99%
2026-06-19 06:56:15,880 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-25 18:45:00 (174 days).
2026-06-19 06:56:16,981 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11993 - after: 16789 - 39.99%
2026-06-19 06:56:16,982 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-25 19:00:00 (174 days).
2026-06-19 06:56:18,239 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 12279 - after: 17267 - 40.62%
2026-06-19 06:56:18,240 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-30 18:30:00 (179 days).
2026-06-19 06:56:19,774 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 12280 - after: 17268 - 40.62%
2026-06-19 06:56:19,775 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-30 18:45:00 (179 days).
2026-06-19 06:56:21,053 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13191 - after: 18563 - 40.72%
2026-06-19 06:56:21,054 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-14 06:30:00 (193 days).
2026-06-19 06:56:22,190 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13198 - after: 18570 - 40.70%
2026-06-19 06:56:22,191 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-14 08:15:00 (193 days).
2026-06-19 06:56:23,344 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13413 - after: 18785 - 40.05%
2026-06-19 06:56:23,345 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-16 14:00:00 (195 days).
2026-06-19 06:56:24,583 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13420 - after: 18792 - 40.03%
2026-06-19 06:56:24,584 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-16 15:45:00 (195 days).
2026-06-19 06:56:25,826 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13504 - after: 18876 - 39.78%
2026-06-19 06:56:25,827 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-17 12:45:00 (196 days).
2026-06-19 06:56:27,022 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13543 - after: 18915 - 39.67%
2026-06-19 06:56:27,023 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-17 22:30:00 (197 days).
2026-06-19 06:56:28,121 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13801 - after: 19365 - 40.32%
2026-06-19 06:56:28,122 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-22 15:00:00 (201 days).
2026-06-19 06:56:29,460 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13802 - after: 19366 - 40.31%
2026-06-19 06:56:29,462 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-22 15:15:00 (201 days).
2026-06-19 06:56:30,886 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14190 - after: 19946 - 40.56%
2026-06-19 06:56:30,887 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-28 16:15:00 (207 days).
2026-06-19 06:56:32,204 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14222 - after: 19978 - 40.47%
2026-06-19 06:56:32,205 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-29 00:15:00 (208 days).
2026-06-19 06:56:33,369 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14369 - after: 20125 - 40.06%
2026-06-19 06:56:33,370 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-30 13:00:00 (209 days).
2026-06-19 06:56:34,692 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14391 - after: 20147 - 40.00%
2026-06-19 06:56:34,693 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-30 18:30:00 (209 days).
2026-06-19 06:56:35,925 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14838 - after: 20786 - 40.09%
2026-06-19 06:56:35,926 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-06 10:15:00 (216 days).
2026-06-19 06:56:37,346 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14839 - after: 20787 - 40.08%
2026-06-19 06:56:37,347 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-06 10:30:00 (216 days).
2026-06-19 06:56:38,557 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 15311 - after: 21451 - 40.10%
2026-06-19 06:56:38,558 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-13 08:30:00 (223 days).
2026-06-19 06:56:39,957 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 15312 - after: 21452 - 40.10%
2026-06-19 06:56:39,958 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-13 08:45:00 (223 days).
2026-06-19 06:56:41,933 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 15964 - after: 22296 - 39.66%
2026-06-19 06:56:41,934 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-22 03:45:00 (232 days).
2026-06-19 06:56:43,324 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 15986 - after: 22318 - 39.61%
2026-06-19 06:56:43,325 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-22 09:15:00 (232 days).
2026-06-19 06:56:44,631 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 16009 - after: 22341 - 39.55%
2026-06-19 06:56:44,632 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-22 15:00:00 (232 days).
2026-06-19 06:56:46,168 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 16010 - after: 22342 - 39.55%
2026-06-19 06:56:46,169 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-22 15:15:00 (232 days).
2026-06-19 06:56:47,558 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 16268 - after: 22792 - 40.10%
2026-06-19 06:56:47,559 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-27 07:45:00 (237 days).
2026-06-19 06:56:48,933 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 16299 - after: 22823 - 40.03%
2026-06-19 06:56:48,934 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-27 15:30:00 (237 days).
2026-06-19 06:56:50,341 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 16550 - after: 23266 - 40.58%
2026-06-19 06:56:50,342 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-01 06:15:00 (242 days).
2026-06-19 06:56:51,772 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 16551 - after: 23267 - 40.58%
2026-06-19 06:56:51,772 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-01 06:30:00 (242 days).
2026-06-19 06:56:53,035 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17639 - after: 24739 - 40.25%
2026-06-19 06:56:53,036 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-16 14:30:00 (257 days).
2026-06-19 06:56:54,491 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17640 - after: 24740 - 40.25%
2026-06-19 06:56:54,492 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-16 14:45:00 (257 days).
2026-06-19 06:56:55,920 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 18304 - after: 25596 - 39.84%
2026-06-19 06:56:55,921 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-25 12:45:00 (266 days).
2026-06-19 06:56:57,391 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 18354 - after: 25646 - 39.73%
2026-06-19 06:56:57,392 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-26 01:15:00 (267 days).
2026-06-19 06:56:58,803 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19276 - after: 26952 - 39.82%
2026-06-19 06:56:58,803 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-09 15:45:00 (280 days).
2026-06-19 06:57:00,467 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19314 - after: 26990 - 39.74%
2026-06-19 06:57:00,468 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-10 01:15:00 (281 days).
2026-06-19 06:57:01,924 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19762 - after: 27630 - 39.81%
2026-06-19 06:57:01,925 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-16 17:15:00 (287 days).
2026-06-19 06:57:03,566 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19763 - after: 27631 - 39.81%
2026-06-19 06:57:03,567 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-16 17:30:00 (287 days).
2026-06-19 06:57:05,072 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20704 - after: 28956 - 39.86%
2026-06-19 06:57:05,073 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-30 12:45:00 (301 days).
2026-06-19 06:57:06,718 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20787 - after: 29039 - 39.70%
2026-06-19 06:57:06,719 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-31 09:30:00 (302 days).
2026-06-19 06:57:08,331 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 23514 - after: 32922 - 40.01%
2026-06-19 06:57:08,332 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-10 20:15:00 (342 days).
2026-06-19 06:57:10,237 - freqtrade.optimize.analysis.lookahead - INFO - found force-exit in pair: EUR/USDT, timerange:2025-12-10 20:15:00+00:00-2025-12-31 21:45:00+00:00, idx: 59, skipping this one 
to avoid a false-positive.
2026-06-19 06:57:10,238 - freqtrade.loggers.set_log_levels - INFO - Restoring log verbosity.
2026-06-19 06:57:10,238 - freqtrade.optimize.analysis.lookahead - INFO -  => LIB_STR054 : bias detected!
2026-06-19 06:57:10,238 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Checking look ahead bias via backtests of LIB_STR054.py took 105 seconds.

```


**رمز الخروج:** 0
