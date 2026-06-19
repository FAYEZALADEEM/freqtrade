# تقرير Lookahead Analysis: LIB_STR056

**التاريخ:** 2026-06-19 06:55
**الأمر:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade lookahead-analysis --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --config <(echo '{"entry_pricing": {"price_side": "other"}, "exit_pricing": {"price_side": "other"}}') --strategy LIB_STR056 --timeframe 15m --timerange 20250101-20260101 --fee 0 --targeted-trade-amount 100 -p EUR/USDT
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
│ LIB_STR056.py │ LIB_STR056 │       No │            10 │                    0 │                   0 │                   │
└───────────────┴────────────┴──────────┴───────────────┴──────────────────────┴─────────────────────┴───────────────────┘

2026-06-19 06:55:23,716 - freqtrade - INFO - freqtrade 2026.6-dev-a29762684
2026-06-19 06:55:24,084 - numexpr.utils - INFO - NumExpr defaulting to 8 threads.
2026-06-19 06:55:25,012 - freqtrade.configuration.load_config - INFO - Using config: user_data/config.json ...
2026-06-19 06:55:25,012 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/63 ...
2026-06-19 06:55:25,013 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/62 ...
2026-06-19 06:55:25,015 - freqtrade.loggers - INFO - Enabling colorized output.
2026-06-19 06:55:25,015 - freqtrade.loggers - INFO - Logfile configured
2026-06-19 06:55:25,016 - freqtrade.loggers - INFO - Verbosity set to 0
2026-06-19 06:55:25,016 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2026-06-19 06:55:25,016 - freqtrade.configuration.configuration - INFO - Parameter --fee detected, setting fee to: 0.0 ...
2026-06-19 06:55:25,017 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20250101-20260101 ...
2026-06-19 06:55:25,017 - freqtrade.configuration.configuration - INFO - Using user-data directory: /home/fayez/freqtrade/user_data ...
2026-06-19 06:55:25,018 - freqtrade.configuration.configuration - INFO - Using data directory: /home/fayez/freqtrade/user_data/data/binance ...
2026-06-19 06:55:25,018 - freqtrade.configuration.configuration - INFO - Using pairs ['EUR/USDT']
2026-06-19 06:55:25,018 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20250101-20260101
2026-06-19 06:55:25,018 - freqtrade.configuration.configuration - INFO - Targeted Trade amount: 100
2026-06-19 06:55:25,019 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2026-06-19 06:55:25,030 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2026-06-19 06:55:25,031 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2026-06-19 06:55:25,034 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Forced order_types to market orders.
2026-06-19 06:55:25,035 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Forced max_open_trades to -1 (same amount as there are pairs)
2026-06-19 06:55:25,035 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Dry run wallet was not set to 1 billion, pushing it up there just to avoid false positives
2026-06-19 06:55:25,036 - freqtrade.optimize.analysis.lookahead_helpers - INFO - fixing stake_amount to 10k
2026-06-19 06:55:25,046 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR072.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR072.py, line 34)'
2026-06-19 06:55:25,047 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR069.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR069.py, line 34)'
2026-06-19 06:55:25,052 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR061.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR061.py, line 34)'
2026-06-19 06:55:25,052 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR062.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR062.py, line 34)'
2026-06-19 06:55:25,054 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR060.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR060.py, line 34)'
2026-06-19 06:55:25,055 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR074.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR074.py, line 34)'
2026-06-19 06:55:25,056 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR068.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR068.py, line 34)'
2026-06-19 06:55:25,060 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR073.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR073.py, line 34)'
2026-06-19 06:55:25,064 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR071.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR071.py, line 34)'
2026-06-19 06:55:25,069 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR065.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR065.py, line 34)'
2026-06-19 06:55:25,069 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Bias test of LIB_STR056.py started.
2026-06-19 06:55:25,071 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2026-06-19 06:55:25,071 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.58
2026-06-19 06:55:25,089 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2026-06-19 06:55:26,444 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2026-06-19 06:55:26,448 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy LIB_STR056 from '/home/fayez/freqtrade/user_data/strategies/LIB_STR056.py'...
2026-06-19 06:55:26,449 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2026-06-19 06:55:26,449 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value from the configuration: 15m.
2026-06-19 06:55:26,450 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'order_types' with value from the configuration: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 
'stoploss_on_exchange': False}.
2026-06-19 06:55:26,450 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value from the configuration: USDT.
2026-06-19 06:55:26,450 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value from the configuration: 10000.
2026-06-19 06:55:26,451 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value from the configuration: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 
'unit': 'minutes'}.
2026-06-19 06:55:26,451 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value from the configuration: -1.
2026-06-19 06:55:26,451 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.01}
2026-06-19 06:55:26,451 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2026-06-19 06:55:26,452 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.01
2026-06-19 06:55:26,452 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2026-06-19 06:55:26,452 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2026-06-19 06:55:26,452 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2026-06-19 06:55:26,453 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: False
2026-06-19 06:55:26,453 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2026-06-19 06:55:26,453 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 'stoploss_on_exchange': False}
2026-06-19 06:55:26,453 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2026-06-19 06:55:26,454 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2026-06-19 06:55:26,454 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: 10000
2026-06-19 06:55:26,454 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2026-06-19 06:55:26,454 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2026-06-19 06:55:26,455 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2026-06-19 06:55:26,455 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2026-06-19 06:55:26,455 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2026-06-19 06:55:26,455 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2026-06-19 06:55:26,455 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2026-06-19 06:55:26,456 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2026-06-19 06:55:26,456 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2026-06-19 06:55:26,456 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2026-06-19 06:55:26,456 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: -1
2026-06-19 06:55:26,457 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2026-06-19 06:55:26,460 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/home/fayez/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2026-06-19 06:55:26,473 - freqtrade.optimize.backtesting - INFO - Using fee 0.0000% from config.
2026-06-19 06:55:26,515 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 24900 - after: 34944 - 40.34%
2026-06-19 06:55:26,516 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-31 21:45:00 (363 days).
2026-06-19 06:55:27,506 - freqtrade.loggers.set_log_levels - INFO - Reducing verbosity for bias tester.
2026-06-19 06:55:27,507 - freqtrade.optimize.analysis.lookahead - INFO - Only found 12 trades. Calculating all available trades.
2026-06-19 06:55:27,552 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 675 - after: 1059 - 56.89%
2026-06-19 06:55:27,553 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-12 22:30:00 (11 days).
2026-06-19 06:55:27,656 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 928 - after: 1312 - 41.38%
2026-06-19 06:55:27,657 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-15 13:45:00 (13 days).
2026-06-19 06:55:27,801 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4515 - after: 6431 - 42.44%
2026-06-19 06:55:27,802 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-09 21:30:00 (66 days).
2026-06-19 06:55:27,983 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4694 - after: 6610 - 40.82%
2026-06-19 06:55:27,984 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-11 18:15:00 (68 days).
2026-06-19 06:55:28,230 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4995 - after: 7103 - 42.20%
2026-06-19 06:55:28,232 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-16 21:30:00 (73 days).
2026-06-19 06:55:28,449 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 5732 - after: 8032 - 40.13%
2026-06-19 06:55:28,450 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-26 13:45:00 (83 days).
2026-06-19 06:55:28,759 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 5955 - after: 8447 - 41.85%
2026-06-19 06:55:28,759 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-30 21:30:00 (87 days).
2026-06-19 06:55:29,041 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6275 - after: 8767 - 39.71%
2026-06-19 06:55:29,042 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 05:30:00 (91 days).
2026-06-19 06:55:29,410 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9798 - after: 13826 - 41.11%
2026-06-19 06:55:29,411 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-25 22:15:00 (144 days).
2026-06-19 06:55:29,786 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10092 - after: 14120 - 39.91%
2026-06-19 06:55:29,787 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-28 23:45:00 (147 days).
2026-06-19 06:55:30,367 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10275 - after: 14495 - 41.07%
2026-06-19 06:55:30,367 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-01 21:30:00 (150 days).
2026-06-19 06:55:30,955 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10626 - after: 14846 - 39.71%
2026-06-19 06:55:30,956 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-05 13:15:00 (154 days).
2026-06-19 06:55:31,513 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 15521 - after: 21661 - 39.56%
2026-06-19 06:55:31,514 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-15 13:00:00 (225 days).
2026-06-19 06:55:32,075 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 16272 - after: 22796 - 40.09%
2026-06-19 06:55:32,076 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-27 08:45:00 (237 days).
2026-06-19 06:55:33,000 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 16995 - after: 23903 - 40.65%
2026-06-19 06:55:33,001 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-07 21:30:00 (248 days).
2026-06-19 06:55:33,865 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17638 - after: 24738 - 40.25%
2026-06-19 06:55:33,866 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-16 14:15:00 (257 days).
2026-06-19 06:55:34,983 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 18435 - after: 25919 - 40.60%
2026-06-19 06:55:34,984 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-28 21:30:00 (269 days).
2026-06-19 06:55:35,703 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19271 - after: 26947 - 39.83%
2026-06-19 06:55:35,704 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-09 14:30:00 (280 days).
2026-06-19 06:55:36,569 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 21795 - after: 30627 - 40.52%
2026-06-19 06:55:36,570 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-16 22:30:00 (319 days).
2026-06-19 06:55:37,432 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 22144 - after: 30976 - 39.88%
2026-06-19 06:55:37,433 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-20 13:45:00 (322 days).
2026-06-19 06:55:38,867 - freqtrade.optimize.analysis.lookahead - INFO - found force-exit in pair: EUR/USDT, timerange:2025-12-28 22:15:00+00:00-2025-12-31 21:45:00+00:00, idx: 10, skipping this one 
to avoid a false-positive.
2026-06-19 06:55:38,867 - freqtrade.loggers.set_log_levels - INFO - Restoring log verbosity.
2026-06-19 06:55:38,868 - freqtrade.optimize.analysis.lookahead - INFO - LIB_STR056: no bias detected
2026-06-19 06:55:38,868 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Checking look ahead bias via backtests of LIB_STR056.py took 14 seconds.

```


**رمز الخروج:** 0
