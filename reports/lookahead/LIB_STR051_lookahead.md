# تقرير Lookahead Analysis: LIB_STR051

**التاريخ:** 2026-06-19 06:50
**الأمر:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade lookahead-analysis --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --config <(echo '{"entry_pricing": {"price_side": "other"}, "exit_pricing": {"price_side": "other"}}') --strategy LIB_STR051 --timeframe 15m --timerange 20250101-20260101 --fee 0 --targeted-trade-amount 100 -p EUR/USDT
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
│ LIB_STR051.py │ LIB_STR051 │       No │            46 │                    0 │                   0 │                   │
└───────────────┴────────────┴──────────┴───────────────┴──────────────────────┴─────────────────────┴───────────────────┘

2026-06-19 06:48:50,723 - freqtrade - INFO - freqtrade 2026.6-dev-a29762684
2026-06-19 06:48:51,022 - numexpr.utils - INFO - NumExpr defaulting to 8 threads.
2026-06-19 06:48:52,219 - freqtrade.configuration.load_config - INFO - Using config: user_data/config.json ...
2026-06-19 06:48:52,219 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/63 ...
2026-06-19 06:48:52,220 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/62 ...
2026-06-19 06:48:52,222 - freqtrade.loggers - INFO - Enabling colorized output.
2026-06-19 06:48:52,222 - freqtrade.loggers - INFO - Logfile configured
2026-06-19 06:48:52,223 - freqtrade.loggers - INFO - Verbosity set to 0
2026-06-19 06:48:52,223 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2026-06-19 06:48:52,223 - freqtrade.configuration.configuration - INFO - Parameter --fee detected, setting fee to: 0.0 ...
2026-06-19 06:48:52,223 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20250101-20260101 ...
2026-06-19 06:48:52,224 - freqtrade.configuration.configuration - INFO - Using user-data directory: /home/fayez/freqtrade/user_data ...
2026-06-19 06:48:52,224 - freqtrade.configuration.configuration - INFO - Using data directory: /home/fayez/freqtrade/user_data/data/binance ...
2026-06-19 06:48:52,224 - freqtrade.configuration.configuration - INFO - Using pairs ['EUR/USDT']
2026-06-19 06:48:52,225 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20250101-20260101
2026-06-19 06:48:52,225 - freqtrade.configuration.configuration - INFO - Targeted Trade amount: 100
2026-06-19 06:48:52,225 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2026-06-19 06:48:52,234 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2026-06-19 06:48:52,235 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2026-06-19 06:48:52,239 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Forced order_types to market orders.
2026-06-19 06:48:52,239 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Forced max_open_trades to -1 (same amount as there are pairs)
2026-06-19 06:48:52,240 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Dry run wallet was not set to 1 billion, pushing it up there just to avoid false positives
2026-06-19 06:48:52,240 - freqtrade.optimize.analysis.lookahead_helpers - INFO - fixing stake_amount to 10k
2026-06-19 06:48:52,251 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR072.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR072.py, line 34)'
2026-06-19 06:48:52,251 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR069.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR069.py, line 34)'
2026-06-19 06:48:52,255 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR061.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR061.py, line 34)'
2026-06-19 06:48:52,256 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR062.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR062.py, line 34)'
2026-06-19 06:48:52,258 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR060.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR060.py, line 34)'
2026-06-19 06:48:52,259 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR074.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR074.py, line 34)'
2026-06-19 06:48:52,260 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR068.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR068.py, line 34)'
2026-06-19 06:48:52,262 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR073.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR073.py, line 34)'
2026-06-19 06:48:52,267 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR071.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR071.py, line 34)'
2026-06-19 06:48:52,271 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR065.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR065.py, line 34)'
2026-06-19 06:48:52,271 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Bias test of LIB_STR051.py started.
2026-06-19 06:48:52,273 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2026-06-19 06:48:52,273 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.58
2026-06-19 06:48:52,285 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2026-06-19 06:48:53,714 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2026-06-19 06:48:53,718 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy LIB_STR051 from '/home/fayez/freqtrade/user_data/strategies/LIB_STR051.py'...
2026-06-19 06:48:53,718 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2026-06-19 06:48:53,719 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value from the configuration: 15m.
2026-06-19 06:48:53,719 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'order_types' with value from the configuration: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 
'stoploss_on_exchange': False}.
2026-06-19 06:48:53,720 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value from the configuration: USDT.
2026-06-19 06:48:53,720 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value from the configuration: 10000.
2026-06-19 06:48:53,720 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value from the configuration: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 
'unit': 'minutes'}.
2026-06-19 06:48:53,720 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value from the configuration: -1.
2026-06-19 06:48:53,721 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.01}
2026-06-19 06:48:53,721 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2026-06-19 06:48:53,721 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.01
2026-06-19 06:48:53,721 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2026-06-19 06:48:53,722 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2026-06-19 06:48:53,722 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2026-06-19 06:48:53,722 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: False
2026-06-19 06:48:53,722 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2026-06-19 06:48:53,723 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 'stoploss_on_exchange': False}
2026-06-19 06:48:53,723 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2026-06-19 06:48:53,723 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2026-06-19 06:48:53,723 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: 10000
2026-06-19 06:48:53,724 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2026-06-19 06:48:53,724 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2026-06-19 06:48:53,724 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2026-06-19 06:48:53,724 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2026-06-19 06:48:53,725 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2026-06-19 06:48:53,725 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2026-06-19 06:48:53,725 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2026-06-19 06:48:53,725 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2026-06-19 06:48:53,725 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2026-06-19 06:48:53,726 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2026-06-19 06:48:53,726 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: -1
2026-06-19 06:48:53,726 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2026-06-19 06:48:53,730 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/home/fayez/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2026-06-19 06:48:53,742 - freqtrade.optimize.backtesting - INFO - Using fee 0.0000% from config.
2026-06-19 06:48:53,782 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 24900 - after: 34944 - 40.34%
2026-06-19 06:48:53,783 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-31 21:45:00 (363 days).
2026-06-19 06:48:55,642 - freqtrade.loggers.set_log_levels - INFO - Reducing verbosity for bias tester.
2026-06-19 06:48:55,643 - freqtrade.optimize.analysis.lookahead - INFO - Only found 48 trades. Calculating all available trades.
2026-06-19 06:48:55,693 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-02 09:00:00 (0 days).
2026-06-19 06:48:55,773 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-02 16:15:00 (0 days).
2026-06-19 06:48:55,905 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-03 05:45:00 (1 days).
2026-06-19 06:48:56,016 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 246 - after: 438 - 78.05%
2026-06-19 06:48:56,017 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-06 11:15:00 (4 days).
2026-06-19 06:48:56,169 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 247 - after: 439 - 77.73%
2026-06-19 06:48:56,170 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-06 11:30:00 (4 days).
2026-06-19 06:48:56,348 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 440 - after: 632 - 43.64%
2026-06-19 06:48:56,349 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-08 11:45:00 (6 days).
2026-06-19 06:48:56,532 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 528 - after: 720 - 36.36%
2026-06-19 06:48:56,533 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-09 09:45:00 (7 days).
2026-06-19 06:48:56,702 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 700 - after: 1084 - 54.86%
2026-06-19 06:48:56,703 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-13 04:45:00 (11 days).
2026-06-19 06:48:56,947 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 841 - after: 1225 - 45.66%
2026-06-19 06:48:56,948 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-14 16:00:00 (12 days).
2026-06-19 06:48:57,122 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1216 - after: 1792 - 47.37%
2026-06-19 06:48:57,123 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-20 13:45:00 (18 days).
2026-06-19 06:48:57,407 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1287 - after: 1863 - 44.76%
2026-06-19 06:48:57,407 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-21 07:30:00 (19 days).
2026-06-19 06:48:57,592 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1578 - after: 2154 - 36.50%
2026-06-19 06:48:57,593 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-24 08:15:00 (22 days).
2026-06-19 06:48:57,822 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1773 - after: 2541 - 43.32%
2026-06-19 06:48:57,823 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-28 09:00:00 (26 days).
2026-06-19 06:48:58,029 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2114 - after: 3074 - 45.41%
2026-06-19 06:48:58,030 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-02 22:15:00 (32 days).
2026-06-19 06:48:58,280 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2254 - after: 3214 - 42.59%
2026-06-19 06:48:58,281 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-04 09:15:00 (33 days).
2026-06-19 06:48:58,527 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2374 - after: 3334 - 40.44%
2026-06-19 06:48:58,528 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-05 15:15:00 (34 days).
2026-06-19 06:48:58,784 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2760 - after: 3912 - 41.74%
2026-06-19 06:48:58,785 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-11 15:45:00 (40 days).
2026-06-19 06:48:59,123 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2955 - after: 4107 - 38.98%
2026-06-19 06:48:59,124 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-13 16:30:00 (42 days).
2026-06-19 06:48:59,437 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 3015 - after: 4167 - 38.21%
2026-06-19 06:48:59,438 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-14 07:30:00 (43 days).
2026-06-19 06:48:59,698 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4019 - after: 5555 - 38.22%
2026-06-19 06:48:59,699 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-28 18:30:00 (57 days).
2026-06-19 06:49:00,076 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4103 - after: 5831 - 42.12%
2026-06-19 06:49:00,077 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-03 15:30:00 (60 days).
2026-06-19 06:49:00,415 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4214 - after: 5942 - 41.01%
2026-06-19 06:49:00,416 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-04 19:15:00 (61 days).
2026-06-19 06:49:00,819 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4264 - after: 5992 - 40.53%
2026-06-19 06:49:00,820 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-05 07:45:00 (62 days).
2026-06-19 06:49:01,292 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4292 - after: 6020 - 40.26%
2026-06-19 06:49:01,293 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-05 14:45:00 (62 days).
2026-06-19 06:49:01,839 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4515 - after: 6431 - 42.44%
2026-06-19 06:49:01,840 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-09 21:30:00 (66 days).
2026-06-19 06:49:02,376 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4694 - after: 6610 - 40.82%
2026-06-19 06:49:02,377 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-11 18:15:00 (68 days).
2026-06-19 06:49:03,036 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4735 - after: 6651 - 40.46%
2026-06-19 06:49:03,037 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-12 04:30:00 (69 days).
2026-06-19 06:49:03,600 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 5552 - after: 7852 - 41.43%
2026-06-19 06:49:03,601 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-24 16:45:00 (81 days).
2026-06-19 06:49:04,130 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 5626 - after: 7926 - 40.88%
2026-06-19 06:49:04,131 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-25 11:15:00 (82 days).
2026-06-19 06:49:04,548 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6275 - after: 8767 - 39.71%
2026-06-19 06:49:04,549 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 05:30:00 (91 days).
2026-06-19 06:49:05,059 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6334 - after: 8826 - 39.34%
2026-06-19 06:49:05,060 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 20:15:00 (91 days).
2026-06-19 06:49:05,512 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6434 - after: 9118 - 41.72%
2026-06-19 06:49:05,512 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-06 21:15:00 (94 days).
2026-06-19 06:49:06,054 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6470 - after: 9154 - 41.48%
2026-06-19 06:49:06,055 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-07 06:15:00 (95 days).
2026-06-19 06:49:06,548 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6506 - after: 9190 - 41.25%
2026-06-19 06:49:06,548 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-07 15:15:00 (95 days).
2026-06-19 06:49:07,162 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6569 - after: 9253 - 40.86%
2026-06-19 06:49:07,163 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-08 07:00:00 (96 days).
2026-06-19 06:49:08,007 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6783 - after: 9467 - 39.57%
2026-06-19 06:49:08,008 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 12:30:00 (98 days).
2026-06-19 06:49:08,581 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6796 - after: 9480 - 39.49%
2026-06-19 06:49:08,581 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 15:45:00 (98 days).
2026-06-19 06:49:09,129 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6832 - after: 9516 - 39.29%
2026-06-19 06:49:09,130 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 00:45:00 (99 days).
2026-06-19 06:49:09,697 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6857 - after: 9541 - 39.14%
2026-06-19 06:49:09,698 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 07:00:00 (99 days).
2026-06-19 06:49:10,222 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6862 - after: 9546 - 39.11%
2026-06-19 06:49:10,223 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 08:15:00 (99 days).
2026-06-19 06:49:10,760 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7119 - after: 9995 - 40.40%
2026-06-19 06:49:10,761 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-16 00:30:00 (104 days).
2026-06-19 06:49:11,330 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7398 - after: 10466 - 41.47%
2026-06-19 06:49:11,331 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-20 22:15:00 (109 days).
2026-06-19 06:49:11,956 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7524 - after: 10592 - 40.78%
2026-06-19 06:49:11,957 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-22 05:45:00 (110 days).
2026-06-19 06:49:12,563 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7570 - after: 10638 - 40.53%
2026-06-19 06:49:12,564 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-22 17:15:00 (110 days).
2026-06-19 06:49:13,159 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7726 - after: 10794 - 39.71%
2026-06-19 06:49:13,160 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-24 08:15:00 (112 days).
2026-06-19 06:49:13,758 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8237 - after: 11497 - 39.58%
2026-06-19 06:49:13,759 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-01 16:00:00 (119 days).
2026-06-19 06:49:14,438 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8399 - after: 11851 - 41.10%
2026-06-19 06:49:14,439 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-05 08:30:00 (123 days).
2026-06-19 06:49:15,021 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8731 - after: 12183 - 39.54%
2026-06-19 06:49:15,022 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-08 19:30:00 (126 days).
2026-06-19 06:49:15,941 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8773 - after: 12225 - 39.35%
2026-06-19 06:49:15,942 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-09 06:00:00 (127 days).
2026-06-19 06:49:16,989 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8875 - after: 12519 - 41.06%
2026-06-19 06:49:16,990 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-12 07:30:00 (130 days).
2026-06-19 06:49:17,838 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8921 - after: 12565 - 40.85%
2026-06-19 06:49:17,840 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-12 19:00:00 (130 days).
2026-06-19 06:49:18,507 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9020 - after: 12664 - 40.40%
2026-06-19 06:49:18,508 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-13 19:45:00 (131 days).
2026-06-19 06:49:19,195 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9024 - after: 12668 - 40.38%
2026-06-19 06:49:19,196 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-13 20:45:00 (131 days).
2026-06-19 06:49:19,862 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9526 - after: 13362 - 40.27%
2026-06-19 06:49:19,863 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-21 02:15:00 (139 days).
2026-06-19 06:49:20,844 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9611 - after: 13447 - 39.91%
2026-06-19 06:49:20,845 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-21 23:30:00 (140 days).
2026-06-19 06:49:21,779 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10317 - after: 14537 - 40.90%
2026-06-19 06:49:21,780 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-02 08:00:00 (151 days).
2026-06-19 06:49:23,025 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10406 - after: 14626 - 40.55%
2026-06-19 06:49:23,026 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-03 06:15:00 (152 days).
2026-06-19 06:49:23,794 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11087 - after: 15499 - 39.79%
2026-06-19 06:49:23,795 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-12 08:30:00 (161 days).
2026-06-19 06:49:24,658 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11094 - after: 15506 - 39.77%
2026-06-19 06:49:24,659 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-12 10:15:00 (161 days).
2026-06-19 06:49:25,449 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11541 - after: 16145 - 39.89%
2026-06-19 06:49:25,451 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-19 02:00:00 (168 days).
2026-06-19 06:49:26,567 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11545 - after: 16149 - 39.88%
2026-06-19 06:49:26,568 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-19 03:00:00 (168 days).
2026-06-19 06:49:27,447 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11797 - after: 16593 - 40.65%
2026-06-19 06:49:27,447 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-23 18:00:00 (172 days).
2026-06-19 06:49:28,487 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11815 - after: 16611 - 40.59%
2026-06-19 06:49:28,488 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-23 22:30:00 (173 days).
2026-06-19 06:49:29,623 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 12026 - after: 16822 - 39.88%
2026-06-19 06:49:29,624 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-26 03:15:00 (175 days).
2026-06-19 06:49:30,534 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 12049 - after: 16845 - 39.80%
2026-06-19 06:49:30,535 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-26 09:00:00 (175 days).
2026-06-19 06:49:31,437 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13320 - after: 18692 - 40.33%
2026-06-19 06:49:31,438 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-15 14:45:00 (194 days).
2026-06-19 06:49:32,567 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13461 - after: 18833 - 39.91%
2026-06-19 06:49:32,568 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-17 02:00:00 (196 days).
2026-06-19 06:49:33,779 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13803 - after: 19367 - 40.31%
2026-06-19 06:49:33,780 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-22 15:30:00 (201 days).
2026-06-19 06:49:35,025 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13902 - after: 19466 - 40.02%
2026-06-19 06:49:35,026 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-23 16:15:00 (202 days).
2026-06-19 06:49:36,039 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14181 - after: 19937 - 40.59%
2026-06-19 06:49:36,040 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-28 14:00:00 (207 days).
2026-06-19 06:49:37,319 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14561 - after: 20317 - 39.53%
2026-06-19 06:49:37,320 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-01 13:00:00 (211 days).
2026-06-19 06:49:38,702 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14859 - after: 20807 - 40.03%
2026-06-19 06:49:38,703 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-06 15:30:00 (216 days).
2026-06-19 06:49:39,887 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14862 - after: 20810 - 40.02%
2026-06-19 06:49:39,888 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-06 16:15:00 (216 days).
2026-06-19 06:49:40,958 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17082 - after: 23990 - 40.44%
2026-06-19 06:49:40,958 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-08 19:15:00 (249 days).
2026-06-19 06:49:42,270 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17205 - after: 24113 - 40.15%
2026-06-19 06:49:42,271 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-10 02:00:00 (251 days).
2026-06-19 06:49:43,604 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17620 - after: 24720 - 40.30%
2026-06-19 06:49:43,605 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-16 09:45:00 (257 days).
2026-06-19 06:49:45,705 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17651 - after: 24751 - 40.22%
2026-06-19 06:49:45,706 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-16 17:30:00 (257 days).
2026-06-19 06:49:46,990 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17828 - after: 24928 - 39.82%
2026-06-19 06:49:46,991 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-18 13:45:00 (259 days).
2026-06-19 06:49:48,992 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17895 - after: 24995 - 39.68%
2026-06-19 06:49:48,993 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-19 06:30:00 (260 days).
2026-06-19 06:49:50,442 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 18323 - after: 25615 - 39.80%
2026-06-19 06:49:50,443 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-25 17:30:00 (266 days).
2026-06-19 06:49:51,872 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 18409 - after: 25701 - 39.61%
2026-06-19 06:49:51,873 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-26 15:00:00 (267 days).
2026-06-19 06:49:53,252 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19271 - after: 26947 - 39.83%
2026-06-19 06:49:53,253 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-09 14:30:00 (280 days).
2026-06-19 06:49:54,949 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19359 - after: 27035 - 39.65%
2026-06-19 06:49:54,950 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-10 12:30:00 (281 days).
2026-06-19 06:49:56,738 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19762 - after: 27630 - 39.81%
2026-06-19 06:49:56,739 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-16 17:15:00 (287 days).
2026-06-19 06:49:58,259 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19792 - after: 27660 - 39.75%
2026-06-19 06:49:58,259 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-17 00:45:00 (288 days).
2026-06-19 06:49:59,889 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20120 - after: 28180 - 40.06%
2026-06-19 06:49:59,890 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-22 10:45:00 (293 days).
2026-06-19 06:50:01,686 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20127 - after: 28187 - 40.05%
2026-06-19 06:50:01,687 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-22 12:30:00 (293 days).
2026-06-19 06:50:03,173 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20996 - after: 29444 - 40.24%
2026-06-19 06:50:03,174 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-04 14:45:00 (306 days).
2026-06-19 06:50:05,127 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 21040 - after: 29488 - 40.15%
2026-06-19 06:50:05,128 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-05 01:45:00 (307 days).
2026-06-19 06:50:06,701 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 21473 - after: 30113 - 40.24%
2026-06-19 06:50:06,702 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-11 14:00:00 (313 days).
2026-06-19 06:50:08,341 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 21507 - after: 30147 - 40.17%
2026-06-19 06:50:08,342 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-11 22:30:00 (314 days).
2026-06-19 06:50:09,936 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 23514 - after: 32922 - 40.01%
2026-06-19 06:50:09,937 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-10 20:15:00 (342 days).
2026-06-19 06:50:11,744 - freqtrade.optimize.analysis.lookahead - INFO - found force-exit in pair: EUR/USDT, timerange:2025-12-11 00:15:00+00:00-2025-12-31 21:45:00+00:00, idx: 46, skipping this one 
to avoid a false-positive.
2026-06-19 06:50:11,744 - freqtrade.loggers.set_log_levels - INFO - Restoring log verbosity.
2026-06-19 06:50:11,744 - freqtrade.optimize.analysis.lookahead - INFO - LIB_STR051: no bias detected
2026-06-19 06:50:11,745 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Checking look ahead bias via backtests of LIB_STR051.py took 79 seconds.

```


**رمز الخروج:** 0
