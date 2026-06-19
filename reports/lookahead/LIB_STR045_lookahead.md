# تقرير Lookahead Analysis: LIB_STR045

**التاريخ:** 2026-06-19 06:47
**الأمر:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade lookahead-analysis --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --config <(echo '{"entry_pricing": {"price_side": "other"}, "exit_pricing": {"price_side": "other"}}') --strategy LIB_STR045 --timeframe 15m --timerange 20250101-20260101 --fee 0 --targeted-trade-amount 100 -p EUR/USDT
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
│ LIB_STR045.py │ LIB_STR045 │       No │            55 │                    0 │                   0 │                   │
└───────────────┴────────────┴──────────┴───────────────┴──────────────────────┴─────────────────────┴───────────────────┘

2026-06-19 06:45:44,279 - freqtrade - INFO - freqtrade 2026.6-dev-a29762684
2026-06-19 06:45:44,509 - numexpr.utils - INFO - NumExpr defaulting to 8 threads.
2026-06-19 06:45:45,381 - freqtrade.configuration.load_config - INFO - Using config: user_data/config.json ...
2026-06-19 06:45:45,383 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/63 ...
2026-06-19 06:45:45,383 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/62 ...
2026-06-19 06:45:45,388 - freqtrade.loggers - INFO - Enabling colorized output.
2026-06-19 06:45:45,388 - freqtrade.loggers - INFO - Logfile configured
2026-06-19 06:45:45,389 - freqtrade.loggers - INFO - Verbosity set to 0
2026-06-19 06:45:45,389 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2026-06-19 06:45:45,390 - freqtrade.configuration.configuration - INFO - Parameter --fee detected, setting fee to: 0.0 ...
2026-06-19 06:45:45,390 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20250101-20260101 ...
2026-06-19 06:45:45,391 - freqtrade.configuration.configuration - INFO - Using user-data directory: /home/fayez/freqtrade/user_data ...
2026-06-19 06:45:45,391 - freqtrade.configuration.configuration - INFO - Using data directory: /home/fayez/freqtrade/user_data/data/binance ...
2026-06-19 06:45:45,392 - freqtrade.configuration.configuration - INFO - Using pairs ['EUR/USDT']
2026-06-19 06:45:45,392 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20250101-20260101
2026-06-19 06:45:45,393 - freqtrade.configuration.configuration - INFO - Targeted Trade amount: 100
2026-06-19 06:45:45,393 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2026-06-19 06:45:45,401 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2026-06-19 06:45:45,401 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2026-06-19 06:45:45,403 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Forced order_types to market orders.
2026-06-19 06:45:45,404 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Forced max_open_trades to -1 (same amount as there are pairs)
2026-06-19 06:45:45,404 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Dry run wallet was not set to 1 billion, pushing it up there just to avoid false positives
2026-06-19 06:45:45,404 - freqtrade.optimize.analysis.lookahead_helpers - INFO - fixing stake_amount to 10k
2026-06-19 06:45:45,414 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR072.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR072.py, line 34)'
2026-06-19 06:45:45,414 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR069.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR069.py, line 34)'
2026-06-19 06:45:45,419 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR061.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR061.py, line 34)'
2026-06-19 06:45:45,420 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR062.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR062.py, line 34)'
2026-06-19 06:45:45,422 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR060.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR060.py, line 34)'
2026-06-19 06:45:45,423 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR074.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR074.py, line 34)'
2026-06-19 06:45:45,424 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR068.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR068.py, line 34)'
2026-06-19 06:45:45,427 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR073.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR073.py, line 34)'
2026-06-19 06:45:45,432 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR071.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR071.py, line 34)'
2026-06-19 06:45:45,436 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR065.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR065.py, line 34)'
2026-06-19 06:45:45,437 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Bias test of LIB_STR045.py started.
2026-06-19 06:45:45,440 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2026-06-19 06:45:45,440 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.58
2026-06-19 06:45:45,452 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2026-06-19 06:45:46,768 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2026-06-19 06:45:46,772 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy LIB_STR045 from '/home/fayez/freqtrade/user_data/strategies/LIB_STR045.py'...
2026-06-19 06:45:46,772 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2026-06-19 06:45:46,773 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value from the configuration: 15m.
2026-06-19 06:45:46,773 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'order_types' with value from the configuration: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 
'stoploss_on_exchange': False}.
2026-06-19 06:45:46,773 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value from the configuration: USDT.
2026-06-19 06:45:46,774 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value from the configuration: 10000.
2026-06-19 06:45:46,774 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value from the configuration: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 
'unit': 'minutes'}.
2026-06-19 06:45:46,774 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value from the configuration: -1.
2026-06-19 06:45:46,774 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.01}
2026-06-19 06:45:46,775 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2026-06-19 06:45:46,775 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.01
2026-06-19 06:45:46,775 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2026-06-19 06:45:46,775 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2026-06-19 06:45:46,776 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2026-06-19 06:45:46,776 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: False
2026-06-19 06:45:46,776 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2026-06-19 06:45:46,776 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 'stoploss_on_exchange': False}
2026-06-19 06:45:46,777 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2026-06-19 06:45:46,777 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2026-06-19 06:45:46,777 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: 10000
2026-06-19 06:45:46,777 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2026-06-19 06:45:46,778 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2026-06-19 06:45:46,778 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2026-06-19 06:45:46,778 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2026-06-19 06:45:46,778 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2026-06-19 06:45:46,778 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2026-06-19 06:45:46,779 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2026-06-19 06:45:46,779 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2026-06-19 06:45:46,779 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2026-06-19 06:45:46,779 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2026-06-19 06:45:46,780 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: -1
2026-06-19 06:45:46,780 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2026-06-19 06:45:46,784 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/home/fayez/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2026-06-19 06:45:46,796 - freqtrade.optimize.backtesting - INFO - Using fee 0.0000% from config.
2026-06-19 06:45:46,835 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 24900 - after: 34944 - 40.34%
2026-06-19 06:45:46,836 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-31 21:45:00 (363 days).
2026-06-19 06:45:48,814 - freqtrade.loggers.set_log_levels - INFO - Reducing verbosity for bias tester.
2026-06-19 06:45:48,815 - freqtrade.optimize.analysis.lookahead - INFO - Only found 57 trades. Calculating all available trades.
2026-06-19 06:45:48,868 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-02 07:00:00 (0 days).
2026-06-19 06:45:48,949 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-02 16:15:00 (0 days).
2026-06-19 06:45:49,066 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-02 17:15:00 (0 days).
2026-06-19 06:45:49,154 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 238 - after: 430 - 80.67%
2026-06-19 06:45:49,155 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-06 09:15:00 (4 days).
2026-06-19 06:45:49,276 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 239 - after: 431 - 80.33%
2026-06-19 06:45:49,277 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-06 09:30:00 (4 days).
2026-06-19 06:45:49,379 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 640 - after: 832 - 30.00%
2026-06-19 06:45:49,380 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-10 13:45:00 (8 days).
2026-06-19 06:45:49,551 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 654 - after: 846 - 29.36%
2026-06-19 06:45:49,552 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-10 17:15:00 (8 days).
2026-06-19 06:45:49,710 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 928 - after: 1312 - 41.38%
2026-06-19 06:45:49,711 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-15 13:45:00 (13 days).
2026-06-19 06:45:49,925 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 929 - after: 1313 - 41.33%
2026-06-19 06:45:49,926 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-15 14:00:00 (13 days).
2026-06-19 06:45:50,104 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1242 - after: 1818 - 46.38%
2026-06-19 06:45:50,105 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-20 20:15:00 (18 days).
2026-06-19 06:45:50,308 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1250 - after: 1826 - 46.08%
2026-06-19 06:45:50,309 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-20 22:15:00 (19 days).
2026-06-19 06:45:50,486 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1609 - after: 2185 - 35.80%
2026-06-19 06:45:50,487 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-24 16:00:00 (22 days).
2026-06-19 06:45:50,757 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1610 - after: 2186 - 35.78%
2026-06-19 06:45:50,758 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-24 16:15:00 (22 days).
2026-06-19 06:45:50,969 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1870 - after: 2638 - 41.07%
2026-06-19 06:45:50,970 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-29 09:15:00 (27 days).
2026-06-19 06:45:51,238 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1876 - after: 2644 - 40.94%
2026-06-19 06:45:51,239 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-29 10:45:00 (27 days).
2026-06-19 06:45:51,483 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2114 - after: 3074 - 45.41%
2026-06-19 06:45:51,484 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-02 22:15:00 (32 days).
2026-06-19 06:45:51,813 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2123 - after: 3083 - 45.22%
2026-06-19 06:45:51,813 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-03 00:30:00 (32 days).
2026-06-19 06:45:52,071 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2275 - after: 3235 - 42.20%
2026-06-19 06:45:52,072 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-04 14:30:00 (33 days).
2026-06-19 06:45:52,343 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2278 - after: 3238 - 42.14%
2026-06-19 06:45:52,343 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-04 15:15:00 (33 days).
2026-06-19 06:45:52,632 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2973 - after: 4125 - 38.75%
2026-06-19 06:45:52,633 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-13 21:00:00 (42 days).
2026-06-19 06:45:53,047 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2974 - after: 4126 - 38.74%
2026-06-19 06:45:53,048 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-13 21:15:00 (42 days).
2026-06-19 06:45:53,459 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4210 - after: 5938 - 41.05%
2026-06-19 06:45:53,460 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-04 18:15:00 (61 days).
2026-06-19 06:45:54,233 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4211 - after: 5939 - 41.04%
2026-06-19 06:45:54,234 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-04 18:30:00 (61 days).
2026-06-19 06:45:54,879 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4265 - after: 5993 - 40.52%
2026-06-19 06:45:54,881 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-05 08:00:00 (62 days).
2026-06-19 06:45:55,332 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4266 - after: 5994 - 40.51%
2026-06-19 06:45:55,333 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-05 08:15:00 (62 days).
2026-06-19 06:45:55,758 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4298 - after: 6026 - 40.20%
2026-06-19 06:45:55,759 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-05 16:15:00 (62 days).
2026-06-19 06:45:56,215 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4299 - after: 6027 - 40.20%
2026-06-19 06:45:56,216 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-05 16:30:00 (62 days).
2026-06-19 06:45:56,617 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4480 - after: 6208 - 38.57%
2026-06-19 06:45:56,618 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-07 13:45:00 (64 days).
2026-06-19 06:45:57,104 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4490 - after: 6218 - 38.49%
2026-06-19 06:45:57,105 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-07 16:15:00 (64 days).
2026-06-19 06:45:57,527 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 5747 - after: 8047 - 40.02%
2026-06-19 06:45:57,528 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-26 17:30:00 (83 days).
2026-06-19 06:45:58,272 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 5761 - after: 8061 - 39.92%
2026-06-19 06:45:58,273 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-26 21:00:00 (83 days).
2026-06-19 06:45:59,109 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6217 - after: 8709 - 40.08%
2026-06-19 06:45:59,110 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-02 15:00:00 (90 days).
2026-06-19 06:46:00,168 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6218 - after: 8710 - 40.08%
2026-06-19 06:46:00,169 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-02 15:15:00 (90 days).
2026-06-19 06:46:00,944 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6280 - after: 8772 - 39.68%
2026-06-19 06:46:00,946 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 06:45:00 (91 days).
2026-06-19 06:46:01,652 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6281 - after: 8773 - 39.68%
2026-06-19 06:46:01,653 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 07:00:00 (91 days).
2026-06-19 06:46:02,213 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6294 - after: 8786 - 39.59%
2026-06-19 06:46:02,214 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 10:15:00 (91 days).
2026-06-19 06:46:02,874 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6295 - after: 8787 - 39.59%
2026-06-19 06:46:02,875 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 10:30:00 (91 days).
2026-06-19 06:46:03,893 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6382 - after: 8874 - 39.05%
2026-06-19 06:46:03,894 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-04 08:15:00 (92 days).
2026-06-19 06:46:04,684 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6390 - after: 8882 - 39.00%
2026-06-19 06:46:04,685 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-04 10:15:00 (92 days).
2026-06-19 06:46:05,252 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6688 - after: 9372 - 40.13%
2026-06-19 06:46:05,253 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-09 12:45:00 (97 days).
2026-06-19 06:46:06,272 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6689 - after: 9373 - 40.13%
2026-06-19 06:46:06,273 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-09 13:00:00 (97 days).
2026-06-19 06:46:07,078 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6707 - after: 9391 - 40.02%
2026-06-19 06:46:07,079 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-09 17:30:00 (97 days).
2026-06-19 06:46:08,165 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6709 - after: 9393 - 40.01%
2026-06-19 06:46:08,166 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-09 18:00:00 (97 days).
2026-06-19 06:46:09,025 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6784 - after: 9468 - 39.56%
2026-06-19 06:46:09,026 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 12:45:00 (98 days).
2026-06-19 06:46:09,850 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6785 - after: 9469 - 39.56%
2026-06-19 06:46:09,850 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 13:00:00 (98 days).
2026-06-19 06:46:10,606 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6796 - after: 9480 - 39.49%
2026-06-19 06:46:10,607 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 15:45:00 (98 days).
2026-06-19 06:46:11,393 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6797 - after: 9481 - 39.49%
2026-06-19 06:46:11,394 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 16:00:00 (98 days).
2026-06-19 06:46:11,990 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6832 - after: 9516 - 39.29%
2026-06-19 06:46:11,990 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 00:45:00 (99 days).
2026-06-19 06:46:12,701 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6833 - after: 9517 - 39.28%
2026-06-19 06:46:12,701 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 01:00:00 (99 days).
2026-06-19 06:46:13,788 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6864 - after: 9548 - 39.10%
2026-06-19 06:46:13,789 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 08:45:00 (99 days).
2026-06-19 06:46:14,853 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6865 - after: 9549 - 39.10%
2026-06-19 06:46:14,854 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 09:00:00 (99 days).
2026-06-19 06:46:15,621 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6894 - after: 9578 - 38.93%
2026-06-19 06:46:15,622 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 16:15:00 (99 days).
2026-06-19 06:46:16,407 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6897 - after: 9581 - 38.92%
2026-06-19 06:46:16,408 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-11 17:00:00 (99 days).
2026-06-19 06:46:17,054 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6932 - after: 9808 - 41.49%
2026-06-19 06:46:17,056 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-14 01:45:00 (102 days).
2026-06-19 06:46:18,106 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6935 - after: 9811 - 41.47%
2026-06-19 06:46:18,107 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-14 02:30:00 (102 days).
2026-06-19 06:46:18,806 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7078 - after: 9954 - 40.63%
2026-06-19 06:46:18,807 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-15 14:15:00 (103 days).
2026-06-19 06:46:19,829 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7096 - after: 9972 - 40.53%
2026-06-19 06:46:19,830 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-15 18:45:00 (103 days).
2026-06-19 06:46:20,813 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7147 - after: 10023 - 40.24%
2026-06-19 06:46:20,813 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-16 07:30:00 (104 days).
2026-06-19 06:46:21,533 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7148 - after: 10024 - 40.24%
2026-06-19 06:46:21,533 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-16 07:45:00 (104 days).
2026-06-19 06:46:22,195 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7415 - after: 10483 - 41.38%
2026-06-19 06:46:22,196 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-21 02:30:00 (109 days).
2026-06-19 06:46:23,226 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7416 - after: 10484 - 41.37%
2026-06-19 06:46:23,227 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-21 02:45:00 (109 days).
2026-06-19 06:46:24,180 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7588 - after: 10656 - 40.43%
2026-06-19 06:46:24,181 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-22 21:45:00 (110 days).
2026-06-19 06:46:25,451 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7660 - after: 10728 - 40.05%
2026-06-19 06:46:25,452 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-23 15:45:00 (111 days).
2026-06-19 06:46:26,313 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8237 - after: 11497 - 39.58%
2026-06-19 06:46:26,314 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-01 16:00:00 (119 days).
2026-06-19 06:46:27,449 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8246 - after: 11506 - 39.53%
2026-06-19 06:46:27,450 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-01 18:15:00 (119 days).
2026-06-19 06:46:28,220 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8874 - after: 12518 - 41.06%
2026-06-19 06:46:28,221 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-12 07:15:00 (130 days).
2026-06-19 06:46:29,307 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8921 - after: 12565 - 40.85%
2026-06-19 06:46:29,308 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-12 19:00:00 (130 days).
2026-06-19 06:46:30,395 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9020 - after: 12664 - 40.40%
2026-06-19 06:46:30,396 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-13 19:45:00 (131 days).
2026-06-19 06:46:31,514 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9021 - after: 12665 - 40.39%
2026-06-19 06:46:31,515 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-13 20:00:00 (131 days).
2026-06-19 06:46:32,355 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9520 - after: 13356 - 40.29%
2026-06-19 06:46:32,356 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-21 00:45:00 (139 days).
2026-06-19 06:46:33,249 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9525 - after: 13361 - 40.27%
2026-06-19 06:46:33,250 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-21 02:00:00 (139 days).
2026-06-19 06:46:34,136 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9813 - after: 13841 - 41.05%
2026-06-19 06:46:34,137 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-26 02:00:00 (144 days).
2026-06-19 06:46:35,197 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9814 - after: 13842 - 41.04%
2026-06-19 06:46:35,198 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-26 02:15:00 (144 days).
2026-06-19 06:46:36,460 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10019 - after: 14047 - 40.20%
2026-06-19 06:46:36,461 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-28 05:30:00 (146 days).
2026-06-19 06:46:37,850 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10022 - after: 14050 - 40.19%
2026-06-19 06:46:37,851 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-28 06:15:00 (146 days).
2026-06-19 06:46:38,742 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10317 - after: 14537 - 40.90%
2026-06-19 06:46:38,743 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-02 08:00:00 (151 days).
2026-06-19 06:46:39,713 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10318 - after: 14538 - 40.90%
2026-06-19 06:46:39,714 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-02 08:15:00 (151 days).
2026-06-19 06:46:40,780 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11087 - after: 15499 - 39.79%
2026-06-19 06:46:40,781 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-12 08:30:00 (161 days).
2026-06-19 06:46:42,061 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11088 - after: 15500 - 39.79%
2026-06-19 06:46:42,062 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-12 08:45:00 (161 days).
2026-06-19 06:46:43,219 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11992 - after: 16788 - 39.99%
2026-06-19 06:46:43,219 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-25 18:45:00 (174 days).
2026-06-19 06:46:44,603 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11993 - after: 16789 - 39.99%
2026-06-19 06:46:44,604 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-25 19:00:00 (174 days).
2026-06-19 06:46:46,318 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 12279 - after: 17267 - 40.62%
2026-06-19 06:46:46,319 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-30 18:30:00 (179 days).
2026-06-19 06:46:48,093 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 12280 - after: 17268 - 40.62%
2026-06-19 06:46:48,095 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-30 18:45:00 (179 days).
2026-06-19 06:46:49,246 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13191 - after: 18563 - 40.72%
2026-06-19 06:46:49,247 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-14 06:30:00 (193 days).
2026-06-19 06:46:51,094 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13195 - after: 18567 - 40.71%
2026-06-19 06:46:51,095 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-14 07:30:00 (193 days).
2026-06-19 06:46:52,961 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14248 - after: 20004 - 40.40%
2026-06-19 06:46:52,962 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-29 06:45:00 (208 days).
2026-06-19 06:46:54,274 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14252 - after: 20008 - 40.39%
2026-06-19 06:46:54,275 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-29 07:45:00 (208 days).
2026-06-19 06:46:56,298 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14394 - after: 20150 - 39.99%
2026-06-19 06:46:56,299 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-30 19:15:00 (209 days).
2026-06-19 06:46:58,037 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14404 - after: 20160 - 39.96%
2026-06-19 06:46:58,038 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-30 21:45:00 (209 days).
2026-06-19 06:46:59,460 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14560 - after: 20316 - 39.53%
2026-06-19 06:46:59,462 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-01 12:45:00 (211 days).
2026-06-19 06:47:00,824 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14561 - after: 20317 - 39.53%
2026-06-19 06:47:00,825 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-01 13:00:00 (211 days).
2026-06-19 06:47:02,175 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14859 - after: 20807 - 40.03%
2026-06-19 06:47:02,176 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-06 15:30:00 (216 days).
2026-06-19 06:47:03,945 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14862 - after: 20810 - 40.02%
2026-06-19 06:47:03,945 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-06 16:15:00 (216 days).
2026-06-19 06:47:05,206 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17082 - after: 23990 - 40.44%
2026-06-19 06:47:05,207 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-08 19:15:00 (249 days).
2026-06-19 06:47:07,024 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17083 - after: 23991 - 40.44%
2026-06-19 06:47:07,025 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-08 19:30:00 (249 days).
2026-06-19 06:47:08,512 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17750 - after: 24850 - 40.00%
2026-06-19 06:47:08,514 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-17 18:15:00 (258 days).
2026-06-19 06:47:10,299 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17751 - after: 24851 - 40.00%
2026-06-19 06:47:10,300 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-17 18:30:00 (258 days).
2026-06-19 06:47:12,206 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17828 - after: 24928 - 39.82%
2026-06-19 06:47:12,207 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-18 13:45:00 (259 days).
2026-06-19 06:47:14,159 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17867 - after: 24967 - 39.74%
2026-06-19 06:47:14,159 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-18 23:30:00 (260 days).
2026-06-19 06:47:16,449 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 18314 - after: 25606 - 39.82%
2026-06-19 06:47:16,450 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-25 15:15:00 (266 days).
2026-06-19 06:47:18,595 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 18319 - after: 25611 - 39.81%
2026-06-19 06:47:18,596 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-25 16:30:00 (266 days).
2026-06-19 06:47:20,300 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19274 - after: 26950 - 39.83%
2026-06-19 06:47:20,301 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-09 15:15:00 (280 days).
2026-06-19 06:47:22,177 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19278 - after: 26954 - 39.82%
2026-06-19 06:47:22,179 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-09 16:15:00 (280 days).
2026-06-19 06:47:24,340 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19701 - after: 27569 - 39.94%
2026-06-19 06:47:24,340 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-16 02:00:00 (287 days).
2026-06-19 06:47:26,403 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19716 - after: 27584 - 39.91%
2026-06-19 06:47:26,404 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-16 05:45:00 (287 days).
2026-06-19 06:47:28,343 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20804 - after: 29056 - 39.67%
2026-06-19 06:47:28,344 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-31 13:45:00 (302 days).
2026-06-19 06:47:30,649 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20814 - after: 29066 - 39.65%
2026-06-19 06:47:30,650 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-31 16:15:00 (302 days).
2026-06-19 06:47:32,696 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 22995 - after: 32211 - 40.08%
2026-06-19 06:47:32,697 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-03 10:30:00 (335 days).
2026-06-19 06:47:34,772 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 22996 - after: 32212 - 40.08%
2026-06-19 06:47:34,773 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-03 10:45:00 (335 days).
2026-06-19 06:47:37,204 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 23869 - after: 33469 - 40.22%
2026-06-19 06:47:37,206 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-16 13:00:00 (348 days).
2026-06-19 06:47:39,370 - freqtrade.optimize.analysis.lookahead - INFO - found force-exit in pair: EUR/USDT, timerange:2025-12-16 13:00:00+00:00-2025-12-31 21:45:00+00:00, idx: 55, skipping this one 
to avoid a false-positive.
2026-06-19 06:47:39,370 - freqtrade.loggers.set_log_levels - INFO - Restoring log verbosity.
2026-06-19 06:47:39,371 - freqtrade.optimize.analysis.lookahead - INFO - LIB_STR045: no bias detected
2026-06-19 06:47:39,371 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Checking look ahead bias via backtests of LIB_STR045.py took 114 seconds.

```


**رمز الخروج:** 0
