# تقرير Lookahead Analysis: LIB_STR048

**التاريخ:** 2026-06-19 06:50
**الأمر:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade lookahead-analysis --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --config <(echo '{"entry_pricing": {"price_side": "other"}, "exit_pricing": {"price_side": "other"}}') --strategy LIB_STR048 --timeframe 15m --timerange 20250101-20260101 --fee 0 --targeted-trade-amount 100 -p EUR/USDT
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
│ LIB_STR048.py │ LIB_STR048 │      Yes │            59 │                    1 │                   0 │                   │
└───────────────┴────────────┴──────────┴───────────────┴──────────────────────┴─────────────────────┴───────────────────┘

2026-06-19 06:48:50,746 - freqtrade - INFO - freqtrade 2026.6-dev-a29762684
2026-06-19 06:48:51,037 - numexpr.utils - INFO - NumExpr defaulting to 8 threads.
2026-06-19 06:48:51,931 - freqtrade.configuration.load_config - INFO - Using config: user_data/config.json ...
2026-06-19 06:48:51,932 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/63 ...
2026-06-19 06:48:51,932 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/62 ...
2026-06-19 06:48:51,934 - freqtrade.loggers - INFO - Enabling colorized output.
2026-06-19 06:48:51,935 - freqtrade.loggers - INFO - Logfile configured
2026-06-19 06:48:51,935 - freqtrade.loggers - INFO - Verbosity set to 0
2026-06-19 06:48:51,935 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2026-06-19 06:48:51,936 - freqtrade.configuration.configuration - INFO - Parameter --fee detected, setting fee to: 0.0 ...
2026-06-19 06:48:51,936 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20250101-20260101 ...
2026-06-19 06:48:51,936 - freqtrade.configuration.configuration - INFO - Using user-data directory: /home/fayez/freqtrade/user_data ...
2026-06-19 06:48:51,937 - freqtrade.configuration.configuration - INFO - Using data directory: /home/fayez/freqtrade/user_data/data/binance ...
2026-06-19 06:48:51,937 - freqtrade.configuration.configuration - INFO - Using pairs ['EUR/USDT']
2026-06-19 06:48:51,937 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20250101-20260101
2026-06-19 06:48:51,938 - freqtrade.configuration.configuration - INFO - Targeted Trade amount: 100
2026-06-19 06:48:51,938 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2026-06-19 06:48:51,945 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2026-06-19 06:48:51,945 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2026-06-19 06:48:51,947 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Forced order_types to market orders.
2026-06-19 06:48:51,947 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Forced max_open_trades to -1 (same amount as there are pairs)
2026-06-19 06:48:51,948 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Dry run wallet was not set to 1 billion, pushing it up there just to avoid false positives
2026-06-19 06:48:51,948 - freqtrade.optimize.analysis.lookahead_helpers - INFO - fixing stake_amount to 10k
2026-06-19 06:48:51,958 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR072.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR072.py, line 34)'
2026-06-19 06:48:51,959 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR069.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR069.py, line 34)'
2026-06-19 06:48:51,964 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR061.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR061.py, line 34)'
2026-06-19 06:48:51,965 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR062.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR062.py, line 34)'
2026-06-19 06:48:51,967 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR060.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR060.py, line 34)'
2026-06-19 06:48:51,968 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR074.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR074.py, line 34)'
2026-06-19 06:48:51,969 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR068.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR068.py, line 34)'
2026-06-19 06:48:51,973 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR073.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR073.py, line 34)'
2026-06-19 06:48:51,979 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR071.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR071.py, line 34)'
2026-06-19 06:48:51,985 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR065.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR065.py, line 34)'
2026-06-19 06:48:51,986 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Bias test of LIB_STR048.py started.
2026-06-19 06:48:51,988 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2026-06-19 06:48:51,988 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.58
2026-06-19 06:48:52,010 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2026-06-19 06:48:53,448 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2026-06-19 06:48:53,452 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy LIB_STR048 from '/home/fayez/freqtrade/user_data/strategies/LIB_STR048.py'...
2026-06-19 06:48:53,452 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2026-06-19 06:48:53,453 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value from the configuration: 15m.
2026-06-19 06:48:53,453 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'order_types' with value from the configuration: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 
'stoploss_on_exchange': False}.
2026-06-19 06:48:53,453 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value from the configuration: USDT.
2026-06-19 06:48:53,454 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value from the configuration: 10000.
2026-06-19 06:48:53,454 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value from the configuration: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 
'unit': 'minutes'}.
2026-06-19 06:48:53,454 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value from the configuration: -1.
2026-06-19 06:48:53,455 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.01}
2026-06-19 06:48:53,455 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2026-06-19 06:48:53,455 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.01
2026-06-19 06:48:53,455 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2026-06-19 06:48:53,456 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2026-06-19 06:48:53,456 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2026-06-19 06:48:53,456 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: False
2026-06-19 06:48:53,457 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2026-06-19 06:48:53,457 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 'stoploss_on_exchange': False}
2026-06-19 06:48:53,457 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2026-06-19 06:48:53,457 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2026-06-19 06:48:53,458 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: 10000
2026-06-19 06:48:53,458 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2026-06-19 06:48:53,458 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2026-06-19 06:48:53,458 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2026-06-19 06:48:53,459 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2026-06-19 06:48:53,459 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2026-06-19 06:48:53,459 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2026-06-19 06:48:53,460 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2026-06-19 06:48:53,460 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2026-06-19 06:48:53,460 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2026-06-19 06:48:53,460 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2026-06-19 06:48:53,461 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: -1
2026-06-19 06:48:53,461 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2026-06-19 06:48:53,465 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/home/fayez/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2026-06-19 06:48:53,481 - freqtrade.optimize.backtesting - INFO - Using fee 0.0000% from config.
2026-06-19 06:48:53,520 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 24900 - after: 34944 - 40.34%
2026-06-19 06:48:53,521 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-31 21:45:00 (363 days).
2026-06-19 06:48:55,413 - freqtrade.loggers.set_log_levels - INFO - Reducing verbosity for bias tester.
2026-06-19 06:48:55,414 - freqtrade.optimize.analysis.lookahead - INFO - Only found 61 trades. Calculating all available trades.
2026-06-19 06:48:55,453 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-02 03:30:00 (0 days).
2026-06-19 06:48:55,529 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-02 16:15:00 (0 days).
2026-06-19 06:48:55,668 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-03 01:15:00 (1 days).
2026-06-19 06:48:55,744 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 246 - after: 438 - 78.05%
2026-06-19 06:48:55,745 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-06 11:15:00 (4 days).
2026-06-19 06:48:55,892 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 247 - after: 439 - 77.73%
2026-06-19 06:48:55,893 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-06 11:30:00 (4 days).
2026-06-19 06:48:56,030 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 440 - after: 632 - 43.64%
2026-06-19 06:48:56,031 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-08 11:45:00 (6 days).
2026-06-19 06:48:56,251 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 462 - after: 654 - 41.56%
2026-06-19 06:48:56,262 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-08 17:15:00 (6 days).
2026-06-19 06:48:56,443 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 700 - after: 1084 - 54.86%
2026-06-19 06:48:56,444 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-13 04:45:00 (11 days).
2026-06-19 06:48:56,617 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 768 - after: 1152 - 50.00%
2026-06-19 06:48:56,617 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-13 21:45:00 (11 days).
2026-06-19 06:48:56,746 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 928 - after: 1312 - 41.38%
2026-06-19 06:48:56,747 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-15 13:45:00 (13 days).
2026-06-19 06:48:56,907 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 929 - after: 1313 - 41.33%
2026-06-19 06:48:56,908 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-15 14:00:00 (13 days).
2026-06-19 06:48:57,044 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1242 - after: 1818 - 46.38%
2026-06-19 06:48:57,045 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-20 20:15:00 (18 days).
2026-06-19 06:48:57,237 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1313 - after: 1889 - 43.87%
2026-06-19 06:48:57,238 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-21 14:00:00 (19 days).
2026-06-19 06:48:57,426 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1578 - after: 2154 - 36.50%
2026-06-19 06:48:57,427 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-24 08:15:00 (22 days).
2026-06-19 06:48:57,634 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1579 - after: 2155 - 36.48%
2026-06-19 06:48:57,635 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-24 08:30:00 (22 days).
2026-06-19 06:48:57,829 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2062 - after: 2830 - 37.25%
2026-06-19 06:48:57,830 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-31 09:15:00 (29 days).
2026-06-19 06:48:58,087 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2090 - after: 2858 - 36.75%
2026-06-19 06:48:58,088 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-31 16:15:00 (29 days).
2026-06-19 06:48:58,304 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2114 - after: 3074 - 45.41%
2026-06-19 06:48:58,305 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-02 22:15:00 (32 days).
2026-06-19 06:48:58,631 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2172 - after: 3132 - 44.20%
2026-06-19 06:48:58,632 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-03 12:45:00 (32 days).
2026-06-19 06:48:58,930 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2278 - after: 3238 - 42.14%
2026-06-19 06:48:58,931 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-04 15:15:00 (33 days).
2026-06-19 06:48:59,212 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2281 - after: 3241 - 42.09%
2026-06-19 06:48:59,213 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-04 16:00:00 (33 days).
2026-06-19 06:48:59,457 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 3020 - after: 4172 - 38.15%
2026-06-19 06:48:59,458 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-14 08:45:00 (43 days).
2026-06-19 06:48:59,762 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 3021 - after: 4173 - 38.13%
2026-06-19 06:48:59,763 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-14 09:00:00 (43 days).
2026-06-19 06:49:00,045 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 3955 - after: 5491 - 38.84%
2026-06-19 06:49:00,046 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-28 02:30:00 (57 days).
2026-06-19 06:49:00,414 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 3977 - after: 5513 - 38.62%
2026-06-19 06:49:00,415 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-28 08:00:00 (57 days).
2026-06-19 06:49:00,771 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4102 - after: 5830 - 42.13%
2026-06-19 06:49:00,772 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-03 15:15:00 (60 days).
2026-06-19 06:49:01,479 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4103 - after: 5831 - 42.12%
2026-06-19 06:49:01,480 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-03 15:30:00 (60 days).
2026-06-19 06:49:01,975 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4214 - after: 5942 - 41.01%
2026-06-19 06:49:01,976 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-04 19:15:00 (61 days).
2026-06-19 06:49:02,551 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4218 - after: 5946 - 40.97%
2026-06-19 06:49:02,552 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-04 20:15:00 (61 days).
2026-06-19 06:49:02,965 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4270 - after: 5998 - 40.47%
2026-06-19 06:49:02,966 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-05 09:15:00 (62 days).
2026-06-19 06:49:03,429 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4291 - after: 6019 - 40.27%
2026-06-19 06:49:03,430 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-05 14:30:00 (62 days).
2026-06-19 06:49:03,990 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4383 - after: 6111 - 39.43%
2026-06-19 06:49:03,991 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-06 13:30:00 (63 days).
2026-06-19 06:49:04,437 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4438 - after: 6166 - 38.94%
2026-06-19 06:49:04,438 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-07 03:15:00 (64 days).
2026-06-19 06:49:04,855 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4657 - after: 6573 - 41.14%
2026-06-19 06:49:04,856 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-11 09:00:00 (68 days).
2026-06-19 06:49:05,326 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4658 - after: 6574 - 41.13%
2026-06-19 06:49:05,327 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-11 09:15:00 (68 days).
2026-06-19 06:49:05,736 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 5453 - after: 7561 - 38.66%
2026-06-19 06:49:05,737 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-21 16:00:00 (78 days).
2026-06-19 06:49:06,267 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 5475 - after: 7775 - 42.01%
2026-06-19 06:49:06,268 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-23 21:30:00 (80 days).
2026-06-19 06:49:06,741 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6239 - after: 8731 - 39.94%
2026-06-19 06:49:06,742 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-02 20:30:00 (90 days).
2026-06-19 06:49:07,349 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6261 - after: 8753 - 39.80%
2026-06-19 06:49:07,350 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 02:00:00 (91 days).
2026-06-19 06:49:07,915 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6290 - after: 8782 - 39.62%
2026-06-19 06:49:07,916 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 09:15:00 (91 days).
2026-06-19 06:49:08,552 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6291 - after: 8783 - 39.61%
2026-06-19 06:49:08,553 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 09:30:00 (91 days).
2026-06-19 06:49:09,116 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6294 - after: 8786 - 39.59%
2026-06-19 06:49:09,116 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 10:15:00 (91 days).
2026-06-19 06:49:09,732 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6295 - after: 8787 - 39.59%
2026-06-19 06:49:09,733 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 10:30:00 (91 days).
2026-06-19 06:49:10,307 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6382 - after: 8874 - 39.05%
2026-06-19 06:49:10,308 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-04 08:15:00 (92 days).
2026-06-19 06:49:10,860 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6400 - after: 8892 - 38.94%
2026-06-19 06:49:10,861 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-04 12:45:00 (92 days).
2026-06-19 06:49:11,506 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6408 - after: 8900 - 38.89%
2026-06-19 06:49:11,507 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-04 14:45:00 (92 days).
2026-06-19 06:49:12,467 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6440 - after: 9124 - 41.68%
2026-06-19 06:49:12,468 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-06 22:45:00 (95 days).
2026-06-19 06:49:13,391 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6688 - after: 9372 - 40.13%
2026-06-19 06:49:13,392 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-09 12:45:00 (97 days).
2026-06-19 06:49:14,245 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6689 - after: 9373 - 40.13%
2026-06-19 06:49:14,246 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-09 13:00:00 (97 days).
2026-06-19 06:49:14,815 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6707 - after: 9391 - 40.02%
2026-06-19 06:49:14,816 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-09 17:30:00 (97 days).
2026-06-19 06:49:15,455 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6737 - after: 9421 - 39.84%
2026-06-19 06:49:15,456 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 01:00:00 (98 days).
2026-06-19 06:49:16,006 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6778 - after: 9462 - 39.60%
2026-06-19 06:49:16,007 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 11:15:00 (98 days).
2026-06-19 06:49:16,670 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6783 - after: 9467 - 39.57%
2026-06-19 06:49:16,672 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 12:30:00 (98 days).
2026-06-19 06:49:17,288 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6796 - after: 9480 - 39.49%
2026-06-19 06:49:17,289 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 15:45:00 (98 days).
2026-06-19 06:49:17,954 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6797 - after: 9481 - 39.49%
2026-06-19 06:49:17,955 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 16:00:00 (98 days).
2026-06-19 06:49:18,547 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6832 - after: 9516 - 39.29%
2026-06-19 06:49:18,548 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 00:45:00 (99 days).
2026-06-19 06:49:19,131 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6833 - after: 9517 - 39.28%
2026-06-19 06:49:19,132 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 01:00:00 (99 days).
2026-06-19 06:49:19,732 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6864 - after: 9548 - 39.10%
2026-06-19 06:49:19,732 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 08:45:00 (99 days).
2026-06-19 06:49:20,346 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6865 - after: 9549 - 39.10%
2026-06-19 06:49:20,347 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 09:00:00 (99 days).
2026-06-19 06:49:20,930 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6894 - after: 9578 - 38.93%
2026-06-19 06:49:20,931 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 16:15:00 (99 days).
2026-06-19 06:49:21,549 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6912 - after: 9596 - 38.83%
2026-06-19 06:49:21,550 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 20:45:00 (99 days).
2026-06-19 06:49:22,412 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7406 - after: 10474 - 41.43%
2026-06-19 06:49:22,413 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-21 00:15:00 (109 days).
2026-06-19 06:49:23,200 - freqtrade.optimize.analysis.lookahead - INFO - found lookahead-bias in trade pair: EUR/USDT, timerange:2025-04-11 21:00:00+00:00 - 2025-04-21 00:00:00+00:00, idx: 30
2026-06-19 06:49:23,268 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7407 - after: 10475 - 41.42%
2026-06-19 06:49:23,270 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-21 00:30:00 (109 days).
2026-06-19 06:49:23,952 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7590 - after: 10658 - 40.42%
2026-06-19 06:49:23,953 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-22 22:15:00 (111 days).
2026-06-19 06:49:24,606 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7634 - after: 10702 - 40.19%
2026-06-19 06:49:24,608 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-23 09:15:00 (111 days).
2026-06-19 06:49:25,242 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8194 - after: 11454 - 39.79%
2026-06-19 06:49:25,243 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-01 05:15:00 (119 days).
2026-06-19 06:49:25,983 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8207 - after: 11467 - 39.72%
2026-06-19 06:49:25,983 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-01 08:30:00 (119 days).
2026-06-19 06:49:26,661 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8758 - after: 12210 - 39.42%
2026-06-19 06:49:26,662 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-09 02:15:00 (127 days).
2026-06-19 06:49:27,693 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8773 - after: 12225 - 39.35%
2026-06-19 06:49:27,694 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-09 06:00:00 (127 days).
2026-06-19 06:49:28,718 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8875 - after: 12519 - 41.06%
2026-06-19 06:49:28,719 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-12 07:30:00 (130 days).
2026-06-19 06:49:29,505 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8941 - after: 12585 - 40.76%
2026-06-19 06:49:29,506 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-13 00:00:00 (131 days).
2026-06-19 06:49:30,247 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9068 - after: 12712 - 40.19%
2026-06-19 06:49:30,248 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-14 07:45:00 (132 days).
2026-06-19 06:49:31,021 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9069 - after: 12713 - 40.18%
2026-06-19 06:49:31,022 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-14 08:00:00 (132 days).
2026-06-19 06:49:32,259 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9526 - after: 13362 - 40.27%
2026-06-19 06:49:32,260 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-21 02:15:00 (139 days).
2026-06-19 06:49:33,268 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9527 - after: 13363 - 40.26%
2026-06-19 06:49:33,269 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-21 02:30:00 (139 days).
2026-06-19 06:49:34,092 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10317 - after: 14537 - 40.90%
2026-06-19 06:49:34,093 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-02 08:00:00 (151 days).
2026-06-19 06:49:35,127 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10318 - after: 14538 - 40.90%
2026-06-19 06:49:35,128 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-02 08:15:00 (151 days).
2026-06-19 06:49:36,006 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11087 - after: 15499 - 39.79%
2026-06-19 06:49:36,007 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-12 08:30:00 (161 days).
2026-06-19 06:49:36,950 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11088 - after: 15500 - 39.79%
2026-06-19 06:49:36,951 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-12 08:45:00 (161 days).
2026-06-19 06:49:37,899 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11992 - after: 16788 - 39.99%
2026-06-19 06:49:37,900 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-25 18:45:00 (174 days).
2026-06-19 06:49:39,020 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11993 - after: 16789 - 39.99%
2026-06-19 06:49:39,021 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-25 19:00:00 (174 days).
2026-06-19 06:49:40,020 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 12279 - after: 17267 - 40.62%
2026-06-19 06:49:40,021 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-30 18:30:00 (179 days).
2026-06-19 06:49:41,074 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 12280 - after: 17268 - 40.62%
2026-06-19 06:49:41,075 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-30 18:45:00 (179 days).
2026-06-19 06:49:42,097 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13191 - after: 18563 - 40.72%
2026-06-19 06:49:42,097 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-14 06:30:00 (193 days).
2026-06-19 06:49:43,556 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13198 - after: 18570 - 40.70%
2026-06-19 06:49:43,557 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-14 08:15:00 (193 days).
2026-06-19 06:49:45,381 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13413 - after: 18785 - 40.05%
2026-06-19 06:49:45,382 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-16 14:00:00 (195 days).
2026-06-19 06:49:46,593 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13420 - after: 18792 - 40.03%
2026-06-19 06:49:46,594 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-16 15:45:00 (195 days).
2026-06-19 06:49:47,703 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13504 - after: 18876 - 39.78%
2026-06-19 06:49:47,704 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-17 12:45:00 (196 days).
2026-06-19 06:49:48,885 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13543 - after: 18915 - 39.67%
2026-06-19 06:49:48,886 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-17 22:30:00 (197 days).
2026-06-19 06:49:50,295 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13801 - after: 19365 - 40.32%
2026-06-19 06:49:50,296 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-22 15:00:00 (201 days).
2026-06-19 06:49:51,741 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13802 - after: 19366 - 40.31%
2026-06-19 06:49:51,742 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-22 15:15:00 (201 days).
2026-06-19 06:49:52,829 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14190 - after: 19946 - 40.56%
2026-06-19 06:49:52,830 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-28 16:15:00 (207 days).
2026-06-19 06:49:54,562 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14222 - after: 19978 - 40.47%
2026-06-19 06:49:54,563 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-29 00:15:00 (208 days).
2026-06-19 06:49:56,054 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14369 - after: 20125 - 40.06%
2026-06-19 06:49:56,055 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-30 13:00:00 (209 days).
2026-06-19 06:49:57,256 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14391 - after: 20147 - 40.00%
2026-06-19 06:49:57,257 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-30 18:30:00 (209 days).
2026-06-19 06:49:58,701 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14838 - after: 20786 - 40.09%
2026-06-19 06:49:58,702 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-06 10:15:00 (216 days).
2026-06-19 06:50:00,295 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14839 - after: 20787 - 40.08%
2026-06-19 06:50:00,296 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-06 10:30:00 (216 days).
2026-06-19 06:50:01,536 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 15311 - after: 21451 - 40.10%
2026-06-19 06:50:01,537 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-13 08:30:00 (223 days).
2026-06-19 06:50:02,821 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 15312 - after: 21452 - 40.10%
2026-06-19 06:50:02,822 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-13 08:45:00 (223 days).
2026-06-19 06:50:04,063 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 15964 - after: 22296 - 39.66%
2026-06-19 06:50:04,064 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-22 03:45:00 (232 days).
2026-06-19 06:50:05,479 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 15986 - after: 22318 - 39.61%
2026-06-19 06:50:05,480 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-22 09:15:00 (232 days).
2026-06-19 06:50:06,774 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 16009 - after: 22341 - 39.55%
2026-06-19 06:50:06,775 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-22 15:00:00 (232 days).
2026-06-19 06:50:08,066 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 16010 - after: 22342 - 39.55%
2026-06-19 06:50:08,067 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-22 15:15:00 (232 days).
2026-06-19 06:50:09,473 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 16268 - after: 22792 - 40.10%
2026-06-19 06:50:09,474 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-27 07:45:00 (237 days).
2026-06-19 06:50:10,866 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 16299 - after: 22823 - 40.03%
2026-06-19 06:50:10,866 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-27 15:30:00 (237 days).
2026-06-19 06:50:12,139 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 16550 - after: 23266 - 40.58%
2026-06-19 06:50:12,140 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-01 06:15:00 (242 days).
2026-06-19 06:50:13,614 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 16551 - after: 23267 - 40.58%
2026-06-19 06:50:13,615 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-01 06:30:00 (242 days).
2026-06-19 06:50:14,932 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17639 - after: 24739 - 40.25%
2026-06-19 06:50:14,932 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-16 14:30:00 (257 days).
2026-06-19 06:50:16,304 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17640 - after: 24740 - 40.25%
2026-06-19 06:50:16,305 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-16 14:45:00 (257 days).
2026-06-19 06:50:17,710 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 18304 - after: 25596 - 39.84%
2026-06-19 06:50:17,711 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-25 12:45:00 (266 days).
2026-06-19 06:50:19,192 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 18354 - after: 25646 - 39.73%
2026-06-19 06:50:19,193 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-26 01:15:00 (267 days).
2026-06-19 06:50:20,573 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19276 - after: 26952 - 39.82%
2026-06-19 06:50:20,573 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-09 15:45:00 (280 days).
2026-06-19 06:50:22,118 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19314 - after: 26990 - 39.74%
2026-06-19 06:50:22,119 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-10 01:15:00 (281 days).
2026-06-19 06:50:23,565 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19762 - after: 27630 - 39.81%
2026-06-19 06:50:23,566 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-16 17:15:00 (287 days).
2026-06-19 06:50:25,090 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19763 - after: 27631 - 39.81%
2026-06-19 06:50:25,091 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-16 17:30:00 (287 days).
2026-06-19 06:50:26,647 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20704 - after: 28956 - 39.86%
2026-06-19 06:50:26,649 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-30 12:45:00 (301 days).
2026-06-19 06:50:28,289 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20787 - after: 29039 - 39.70%
2026-06-19 06:50:28,290 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-31 09:30:00 (302 days).
2026-06-19 06:50:29,868 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 23514 - after: 32922 - 40.01%
2026-06-19 06:50:29,869 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-10 20:15:00 (342 days).
2026-06-19 06:50:31,690 - freqtrade.optimize.analysis.lookahead - INFO - found force-exit in pair: EUR/USDT, timerange:2025-12-10 20:15:00+00:00-2025-12-31 21:45:00+00:00, idx: 59, skipping this one 
to avoid a false-positive.
2026-06-19 06:50:31,690 - freqtrade.loggers.set_log_levels - INFO - Restoring log verbosity.
2026-06-19 06:50:31,691 - freqtrade.optimize.analysis.lookahead - INFO -  => LIB_STR048 : bias detected!
2026-06-19 06:50:31,691 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Checking look ahead bias via backtests of LIB_STR048.py took 100 seconds.

```


**رمز الخروج:** 0
