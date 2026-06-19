# تقرير Lookahead Analysis: LIB_STR058

**التاريخ:** 2026-06-19 06:56
**الأمر:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade lookahead-analysis --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --config <(echo '{"entry_pricing": {"price_side": "other"}, "exit_pricing": {"price_side": "other"}}') --strategy LIB_STR058 --timeframe 15m --timerange 20250101-20260101 --fee 0 --targeted-trade-amount 100 -p EUR/USDT
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
│ LIB_STR058.py │ LIB_STR058 │       No │            48 │                    0 │                   0 │                   │
└───────────────┴────────────┴──────────┴───────────────┴──────────────────────┴─────────────────────┴───────────────────┘

2026-06-19 06:55:23,716 - freqtrade - INFO - freqtrade 2026.6-dev-a29762684
2026-06-19 06:55:24,116 - numexpr.utils - INFO - NumExpr defaulting to 8 threads.
2026-06-19 06:55:25,142 - freqtrade.configuration.load_config - INFO - Using config: user_data/config.json ...
2026-06-19 06:55:25,143 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/63 ...
2026-06-19 06:55:25,143 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/62 ...
2026-06-19 06:55:25,145 - freqtrade.loggers - INFO - Enabling colorized output.
2026-06-19 06:55:25,146 - freqtrade.loggers - INFO - Logfile configured
2026-06-19 06:55:25,146 - freqtrade.loggers - INFO - Verbosity set to 0
2026-06-19 06:55:25,146 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 15m ...
2026-06-19 06:55:25,147 - freqtrade.configuration.configuration - INFO - Parameter --fee detected, setting fee to: 0.0 ...
2026-06-19 06:55:25,147 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20250101-20260101 ...
2026-06-19 06:55:25,148 - freqtrade.configuration.configuration - INFO - Using user-data directory: /home/fayez/freqtrade/user_data ...
2026-06-19 06:55:25,148 - freqtrade.configuration.configuration - INFO - Using data directory: /home/fayez/freqtrade/user_data/data/binance ...
2026-06-19 06:55:25,148 - freqtrade.configuration.configuration - INFO - Using pairs ['EUR/USDT']
2026-06-19 06:55:25,149 - freqtrade.configuration.configuration - INFO - Filter trades by timerange: 20250101-20260101
2026-06-19 06:55:25,149 - freqtrade.configuration.configuration - INFO - Targeted Trade amount: 100
2026-06-19 06:55:25,149 - freqtrade.exchange.check_exchange - INFO - Checking exchange...
2026-06-19 06:55:25,157 - freqtrade.exchange.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2026-06-19 06:55:25,158 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2026-06-19 06:55:25,160 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Forced order_types to market orders.
2026-06-19 06:55:25,160 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Forced max_open_trades to -1 (same amount as there are pairs)
2026-06-19 06:55:25,160 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Dry run wallet was not set to 1 billion, pushing it up there just to avoid false positives
2026-06-19 06:55:25,161 - freqtrade.optimize.analysis.lookahead_helpers - INFO - fixing stake_amount to 10k
2026-06-19 06:55:25,171 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR072.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR072.py, line 34)'
2026-06-19 06:55:25,172 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR069.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR069.py, line 34)'
2026-06-19 06:55:25,176 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR061.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR061.py, line 34)'
2026-06-19 06:55:25,177 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR062.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR062.py, line 34)'
2026-06-19 06:55:25,179 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR060.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR060.py, line 34)'
2026-06-19 06:55:25,180 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR074.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR074.py, line 34)'
2026-06-19 06:55:25,181 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR068.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR068.py, line 34)'
2026-06-19 06:55:25,184 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR073.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR073.py, line 34)'
2026-06-19 06:55:25,189 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR071.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR071.py, line 34)'
2026-06-19 06:55:25,193 - freqtrade.resolvers.iresolver - WARNING - Could not import /home/fayez/freqtrade/user_data/strategies/LIB_STR065.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR065.py, line 34)'
2026-06-19 06:55:25,194 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Bias test of LIB_STR058.py started.
2026-06-19 06:55:25,195 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2026-06-19 06:55:25,196 - freqtrade.exchange.exchange - INFO - Using CCXT 4.5.58
2026-06-19 06:55:25,210 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2026-06-19 06:55:26,605 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2026-06-19 06:55:26,609 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy LIB_STR058 from '/home/fayez/freqtrade/user_data/strategies/LIB_STR058.py'...
2026-06-19 06:55:26,610 - freqtrade.strategy.hyper - INFO - Found no parameter file.
2026-06-19 06:55:26,610 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value from the configuration: 15m.
2026-06-19 06:55:26,611 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'order_types' with value from the configuration: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 
'stoploss_on_exchange': False}.
2026-06-19 06:55:26,611 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value from the configuration: USDT.
2026-06-19 06:55:26,612 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value from the configuration: 10000.
2026-06-19 06:55:26,612 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value from the configuration: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 
'unit': 'minutes'}.
2026-06-19 06:55:26,612 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'max_open_trades' with value from the configuration: -1.
2026-06-19 06:55:26,612 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.01}
2026-06-19 06:55:26,613 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 15m
2026-06-19 06:55:26,613 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.01
2026-06-19 06:55:26,613 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2026-06-19 06:55:26,613 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2026-06-19 06:55:26,614 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2026-06-19 06:55:26,614 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: False
2026-06-19 06:55:26,614 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: True
2026-06-19 06:55:26,614 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 'stoploss_on_exchange': False}
2026-06-19 06:55:26,615 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2026-06-19 06:55:26,615 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2026-06-19 06:55:26,615 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: 10000
2026-06-19 06:55:26,615 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 0
2026-06-19 06:55:26,616 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2026-06-19 06:55:26,616 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_exit_signal: True
2026-06-19 06:55:26,616 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_only: False
2026-06-19 06:55:26,616 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_entry_signal: False
2026-06-19 06:55:26,617 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using exit_profit_offset: 0.0
2026-06-19 06:55:26,617 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2026-06-19 06:55:26,617 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2026-06-19 06:55:26,617 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using position_adjustment_enable: False
2026-06-19 06:55:26,618 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_entry_position_adjustment: -1
2026-06-19 06:55:26,618 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using max_open_trades: -1
2026-06-19 06:55:26,618 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2026-06-19 06:55:26,622 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/home/fayez/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2026-06-19 06:55:26,640 - freqtrade.optimize.backtesting - INFO - Using fee 0.0000% from config.
2026-06-19 06:55:26,694 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 24900 - after: 34944 - 40.34%
2026-06-19 06:55:26,695 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-31 21:45:00 (363 days).
2026-06-19 06:55:28,659 - freqtrade.loggers.set_log_levels - INFO - Reducing verbosity for bias tester.
2026-06-19 06:55:28,660 - freqtrade.optimize.analysis.lookahead - INFO - Only found 50 trades. Calculating all available trades.
2026-06-19 06:55:28,703 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-03 08:00:00 (1 days).
2026-06-19 06:55:28,797 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 246 - after: 438 - 78.05%
2026-06-19 06:55:28,797 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-06 11:15:00 (4 days).
2026-06-19 06:55:28,918 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 247 - after: 439 - 77.73%
2026-06-19 06:55:28,919 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-06 11:30:00 (4 days).
2026-06-19 06:55:29,035 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 440 - after: 632 - 43.64%
2026-06-19 06:55:29,035 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-08 11:45:00 (6 days).
2026-06-19 06:55:29,183 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 675 - after: 1059 - 56.89%
2026-06-19 06:55:29,184 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-12 22:30:00 (11 days).
2026-06-19 06:55:29,365 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 928 - after: 1312 - 41.38%
2026-06-19 06:55:29,366 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-15 13:45:00 (13 days).
2026-06-19 06:55:29,631 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 929 - after: 1313 - 41.33%
2026-06-19 06:55:29,632 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-15 14:00:00 (13 days).
2026-06-19 06:55:29,835 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1242 - after: 1818 - 46.38%
2026-06-19 06:55:29,836 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-20 20:15:00 (18 days).
2026-06-19 06:55:30,121 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1314 - after: 1890 - 43.84%
2026-06-19 06:55:30,122 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-21 14:15:00 (19 days).
2026-06-19 06:55:30,291 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1578 - after: 2154 - 36.50%
2026-06-19 06:55:30,291 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-24 08:15:00 (22 days).
2026-06-19 06:55:30,532 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 1677 - after: 2445 - 45.80%
2026-06-19 06:55:30,533 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-27 09:00:00 (25 days).
2026-06-19 06:55:30,719 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2062 - after: 2830 - 37.25%
2026-06-19 06:55:30,720 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-31 09:15:00 (29 days).
2026-06-19 06:55:30,961 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2090 - after: 2858 - 36.75%
2026-06-19 06:55:30,962 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-01-31 16:15:00 (29 days).
2026-06-19 06:55:31,169 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2114 - after: 3074 - 45.41%
2026-06-19 06:55:31,170 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-02 22:15:00 (32 days).
2026-06-19 06:55:31,462 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2184 - after: 3144 - 43.96%
2026-06-19 06:55:31,463 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-03 15:45:00 (32 days).
2026-06-19 06:55:31,814 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2343 - after: 3303 - 40.97%
2026-06-19 06:55:31,815 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-05 07:30:00 (34 days).
2026-06-19 06:55:32,225 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2599 - after: 3751 - 44.32%
2026-06-19 06:55:32,226 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-09 23:30:00 (39 days).
2026-06-19 06:55:32,581 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2862 - after: 4014 - 40.25%
2026-06-19 06:55:32,582 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-12 17:15:00 (41 days).
2026-06-19 06:55:32,929 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 2900 - after: 4052 - 39.72%
2026-06-19 06:55:32,930 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-13 02:45:00 (42 days).
2026-06-19 06:55:33,353 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 3044 - after: 4196 - 37.84%
2026-06-19 06:55:33,355 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-14 14:45:00 (43 days).
2026-06-19 06:55:33,801 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 3079 - after: 4423 - 43.65%
2026-06-19 06:55:33,802 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-16 23:30:00 (46 days).
2026-06-19 06:55:34,110 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 3953 - after: 5489 - 38.86%
2026-06-19 06:55:34,110 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-28 02:00:00 (57 days).
2026-06-19 06:55:34,494 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 3978 - after: 5514 - 38.61%
2026-06-19 06:55:34,495 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-02-28 08:15:00 (57 days).
2026-06-19 06:55:34,989 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4103 - after: 5831 - 42.12%
2026-06-19 06:55:34,990 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-03 15:30:00 (60 days).
2026-06-19 06:55:35,577 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4142 - after: 5870 - 41.72%
2026-06-19 06:55:35,578 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-04 01:15:00 (61 days).
2026-06-19 06:55:35,922 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4214 - after: 5942 - 41.01%
2026-06-19 06:55:35,923 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-04 19:15:00 (61 days).
2026-06-19 06:55:36,338 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4264 - after: 5992 - 40.53%
2026-06-19 06:55:36,339 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-05 07:45:00 (62 days).
2026-06-19 06:55:36,699 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4292 - after: 6020 - 40.26%
2026-06-19 06:55:36,700 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-05 14:45:00 (62 days).
2026-06-19 06:55:37,326 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4365 - after: 6093 - 39.59%
2026-06-19 06:55:37,327 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-06 09:00:00 (63 days).
2026-06-19 06:55:37,874 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4657 - after: 6573 - 41.14%
2026-06-19 06:55:37,875 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-11 09:00:00 (68 days).
2026-06-19 06:55:38,521 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 4848 - after: 6764 - 39.52%
2026-06-19 06:55:38,522 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-13 08:45:00 (70 days).
2026-06-19 06:55:39,000 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 5731 - after: 8031 - 40.13%
2026-06-19 06:55:39,001 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-26 13:30:00 (83 days).
2026-06-19 06:55:39,734 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 5809 - after: 8109 - 39.59%
2026-06-19 06:55:39,735 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-03-27 09:00:00 (84 days).
2026-06-19 06:55:40,210 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6238 - after: 8730 - 39.95%
2026-06-19 06:55:40,211 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-02 20:15:00 (90 days).
2026-06-19 06:55:40,787 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6239 - after: 8731 - 39.94%
2026-06-19 06:55:40,787 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-02 20:30:00 (90 days).
2026-06-19 06:55:41,294 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6287 - after: 8779 - 39.64%
2026-06-19 06:55:41,295 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-03 08:30:00 (91 days).
2026-06-19 06:55:41,847 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6395 - after: 8887 - 38.97%
2026-06-19 06:55:41,848 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-04 11:30:00 (92 days).
2026-06-19 06:55:42,397 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6418 - after: 8910 - 38.83%
2026-06-19 06:55:42,398 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-04 17:15:00 (92 days).
2026-06-19 06:55:42,959 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6475 - after: 9159 - 41.45%
2026-06-19 06:55:42,960 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-07 07:30:00 (95 days).
2026-06-19 06:55:43,495 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6505 - after: 9189 - 41.26%
2026-06-19 06:55:43,496 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-07 15:00:00 (95 days).
2026-06-19 06:55:44,397 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6569 - after: 9253 - 40.86%
2026-06-19 06:55:44,398 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-08 07:00:00 (96 days).
2026-06-19 06:55:44,942 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 6783 - after: 9467 - 39.57%
2026-06-19 06:55:44,943 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-10 12:30:00 (98 days).
2026-06-19 06:55:45,563 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7053 - after: 9929 - 40.78%
2026-06-19 06:55:45,563 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-15 08:00:00 (103 days).
2026-06-19 06:55:46,092 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7406 - after: 10474 - 41.43%
2026-06-19 06:55:46,092 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-21 00:15:00 (109 days).
2026-06-19 06:55:46,703 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 7745 - after: 10813 - 39.61%
2026-06-19 06:55:46,704 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-04-24 13:00:00 (112 days).
2026-06-19 06:55:47,270 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8717 - after: 12169 - 39.60%
2026-06-19 06:55:47,271 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-08 16:00:00 (126 days).
2026-06-19 06:55:47,995 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8781 - after: 12233 - 39.31%
2026-06-19 06:55:47,996 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-09 08:00:00 (127 days).
2026-06-19 06:55:48,808 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8875 - after: 12519 - 41.06%
2026-06-19 06:55:48,809 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-12 07:30:00 (130 days).
2026-06-19 06:55:49,834 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 8943 - after: 12587 - 40.75%
2026-06-19 06:55:49,835 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-13 00:30:00 (131 days).
2026-06-19 06:55:50,800 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9069 - after: 12713 - 40.18%
2026-06-19 06:55:50,801 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-14 08:00:00 (132 days).
2026-06-19 06:55:51,527 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9071 - after: 12715 - 40.17%
2026-06-19 06:55:51,527 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-14 08:30:00 (132 days).
2026-06-19 06:55:52,208 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9533 - after: 13369 - 40.24%
2026-06-19 06:55:52,209 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-21 04:00:00 (139 days).
2026-06-19 06:55:53,005 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 9615 - after: 13451 - 39.90%
2026-06-19 06:55:53,006 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-22 00:30:00 (140 days).
2026-06-19 06:55:53,789 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10092 - after: 14120 - 39.91%
2026-06-19 06:55:53,791 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-28 23:45:00 (147 days).
2026-06-19 06:55:55,124 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10120 - after: 14148 - 39.80%
2026-06-19 06:55:55,125 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-29 06:45:00 (147 days).
2026-06-19 06:55:56,092 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10164 - after: 14192 - 39.63%
2026-06-19 06:55:56,093 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-05-29 17:45:00 (147 days).
2026-06-19 06:55:56,895 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10275 - after: 14495 - 41.07%
2026-06-19 06:55:56,896 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-01 21:30:00 (150 days).
2026-06-19 06:55:57,650 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10626 - after: 14846 - 39.71%
2026-06-19 06:55:57,650 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-05 13:15:00 (154 days).
2026-06-19 06:55:58,516 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 10627 - after: 14847 - 39.71%
2026-06-19 06:55:58,518 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-05 13:30:00 (154 days).
2026-06-19 06:55:59,346 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11093 - after: 15505 - 39.77%
2026-06-19 06:55:59,347 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-12 10:00:00 (161 days).
2026-06-19 06:56:00,282 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11094 - after: 15506 - 39.77%
2026-06-19 06:56:00,283 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-12 10:15:00 (161 days).
2026-06-19 06:56:01,130 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11541 - after: 16145 - 39.89%
2026-06-19 06:56:01,131 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-19 02:00:00 (168 days).
2026-06-19 06:56:02,029 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11564 - after: 16168 - 39.81%
2026-06-19 06:56:02,030 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-19 07:45:00 (168 days).
2026-06-19 06:56:02,953 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11814 - after: 16610 - 40.60%
2026-06-19 06:56:02,955 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-23 22:15:00 (173 days).
2026-06-19 06:56:04,240 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 11815 - after: 16611 - 40.59%
2026-06-19 06:56:04,241 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-23 22:30:00 (173 days).
2026-06-19 06:56:05,141 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 12026 - after: 16822 - 39.88%
2026-06-19 06:56:05,142 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-26 03:15:00 (175 days).
2026-06-19 06:56:06,438 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 12049 - after: 16845 - 39.80%
2026-06-19 06:56:06,439 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-06-26 09:00:00 (175 days).
2026-06-19 06:56:07,308 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13320 - after: 18692 - 40.33%
2026-06-19 06:56:07,309 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-15 14:45:00 (194 days).
2026-06-19 06:56:08,388 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13420 - after: 18792 - 40.03%
2026-06-19 06:56:08,389 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-16 15:45:00 (195 days).
2026-06-19 06:56:09,540 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13504 - after: 18876 - 39.78%
2026-06-19 06:56:09,541 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-17 12:45:00 (196 days).
2026-06-19 06:56:10,699 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13599 - after: 18971 - 39.50%
2026-06-19 06:56:10,699 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-18 12:30:00 (197 days).
2026-06-19 06:56:11,766 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13914 - after: 19478 - 39.99%
2026-06-19 06:56:11,767 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-23 19:15:00 (202 days).
2026-06-19 06:56:13,059 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 13988 - after: 19552 - 39.78%
2026-06-19 06:56:13,060 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-24 13:45:00 (203 days).
2026-06-19 06:56:14,491 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14171 - after: 19927 - 40.62%
2026-06-19 06:56:14,492 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-28 11:30:00 (207 days).
2026-06-19 06:56:15,735 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14442 - after: 20198 - 39.86%
2026-06-19 06:56:15,736 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-07-31 07:15:00 (210 days).
2026-06-19 06:56:16,794 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14564 - after: 20320 - 39.52%
2026-06-19 06:56:16,795 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-01 13:45:00 (211 days).
2026-06-19 06:56:18,127 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14695 - after: 20643 - 40.48%
2026-06-19 06:56:18,128 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-04 22:30:00 (215 days).
2026-06-19 06:56:19,242 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 14926 - after: 20874 - 39.85%
2026-06-19 06:56:19,243 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-07 08:15:00 (217 days).
2026-06-19 06:56:20,436 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 15047 - after: 20995 - 39.53%
2026-06-19 06:56:20,437 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-08-08 14:30:00 (218 days).
2026-06-19 06:56:21,526 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17099 - after: 24007 - 40.40%
2026-06-19 06:56:21,527 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-08 23:30:00 (250 days).
2026-06-19 06:56:22,865 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17205 - after: 24113 - 40.15%
2026-06-19 06:56:22,866 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-10 02:00:00 (251 days).
2026-06-19 06:56:24,777 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17620 - after: 24720 - 40.30%
2026-06-19 06:56:24,778 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-16 09:45:00 (257 days).
2026-06-19 06:56:26,367 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17739 - after: 24839 - 40.02%
2026-06-19 06:56:26,368 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-17 15:30:00 (258 days).
2026-06-19 06:56:27,658 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17919 - after: 25019 - 39.62%
2026-06-19 06:56:27,659 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-19 12:30:00 (260 days).
2026-06-19 06:56:29,560 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 17955 - after: 25247 - 40.61%
2026-06-19 06:56:29,561 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-09-21 21:30:00 (262 days).
2026-06-19 06:56:31,092 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19126 - after: 26802 - 40.13%
2026-06-19 06:56:31,093 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-08 02:15:00 (279 days).
2026-06-19 06:56:32,566 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 19219 - after: 26895 - 39.94%
2026-06-19 06:56:32,567 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-09 01:30:00 (280 days).
2026-06-19 06:56:34,693 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20807 - after: 29059 - 39.66%
2026-06-19 06:56:34,694 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-10-31 14:30:00 (302 days).
2026-06-19 06:56:36,338 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 20906 - after: 29354 - 40.41%
2026-06-19 06:56:36,339 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-03 16:15:00 (305 days).
2026-06-19 06:56:37,945 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 21672 - after: 30312 - 39.87%
2026-06-19 06:56:37,946 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-13 15:45:00 (315 days).
2026-06-19 06:56:39,667 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 21713 - after: 30353 - 39.79%
2026-06-19 06:56:39,668 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-14 02:00:00 (316 days).
2026-06-19 06:56:41,402 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 22070 - after: 30902 - 40.02%
2026-06-19 06:56:41,403 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-19 19:15:00 (321 days).
2026-06-19 06:56:43,100 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 22128 - after: 30960 - 39.91%
2026-06-19 06:56:43,101 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-11-20 09:45:00 (322 days).
2026-06-19 06:56:44,780 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 22813 - after: 32029 - 40.40%
2026-06-19 06:56:44,781 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-01 13:00:00 (333 days).
2026-06-19 06:56:46,604 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 22870 - after: 32086 - 40.30%
2026-06-19 06:56:46,605 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-02 03:15:00 (334 days).
2026-06-19 06:56:48,346 - freqtrade.data.converter.converter - INFO - Missing data fillup for EUR/USDT, 15m: before: 23584 - after: 32992 - 39.89%
2026-06-19 06:56:48,346 - freqtrade.optimize.backtesting - INFO - Loading data from 2025-01-01 22:00:00 up to 2025-12-11 13:45:00 (343 days).
2026-06-19 06:56:50,144 - freqtrade.optimize.analysis.lookahead - INFO - found force-exit in pair: EUR/USDT, timerange:2025-12-12 08:30:00+00:00-2025-12-31 21:45:00+00:00, idx: 48, skipping this one 
to avoid a false-positive.
2026-06-19 06:56:50,145 - freqtrade.loggers.set_log_levels - INFO - Restoring log verbosity.
2026-06-19 06:56:50,145 - freqtrade.optimize.analysis.lookahead - INFO - LIB_STR058: no bias detected
2026-06-19 06:56:50,145 - freqtrade.optimize.analysis.lookahead_helpers - INFO - Checking look ahead bias via backtests of LIB_STR058.py took 85 seconds.

```


**رمز الخروج:** 0
