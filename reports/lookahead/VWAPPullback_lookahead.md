# تقرير Lookahead Analysis: VWAPPullback

**التاريخ:** 2026-06-19 06:46
**الأمر:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade lookahead-analysis --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --config <(echo '{"entry_pricing": {"price_side": "other"}, "exit_pricing": {"price_side": "other"}}') --strategy VWAPPullback --timeframe 15m --timerange 20250101-20260101 --fee 0 --targeted-trade-amount 100 -p EUR/USDT
```

## قاعدة التحقق المطبقة

- `targeted_trade_amount = 100` (ثابت حسب القاعدة الدائمة)
- يتم فحص حتى 100 إشارة. إذا كان عدد الإشارات أقل، يتم التوضيح.

## النتائج

```
[3m                                                      Lookahead Analysis                                                      [0m
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃[1m [0m[1m       filename[0m[1m [0m┃[1m [0m[1m    strategy[0m[1m [0m┃[1m [0m[1mhas_bias[0m[1m [0m┃[1m [0m[1mtotal_signals[0m[1m [0m┃[1m [0m[1mbiased_entry_signals[0m[1m [0m┃[1m [0m[1mbiased_exit_signals[0m[1m [0m┃[1m [0m[1mbiased_indicators[0m[1m [0m┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ VWAPPullback.py │ VWAPPullback │ [1;32m      No[0m │            20 │                    0 │                   0 │                   │
└─────────────────┴──────────────┴──────────┴───────────────┴──────────────────────┴─────────────────────┴───────────────────┘

2026-06-19 06:46:12,937 - freqtrade - INFO - freqtrade 2026.6-dev-a29762684
2026-06-19 06:46:13,256 - numexpr.utils - INFO - NumExpr defaulting to 8 threads.
2026-06-19 06:46:14,521 - freqtrade.configuration.load_config - INFO - Using config: user_data/config.json ...
2026-06-19 06:46:14,522 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/63 ...
2026-06-19 06:46:14,523 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/62 ...
2026-06-19 06:46:14,527 - freqtrade.loggers - INFO - Enabling colorized output.
2026-06-19 06:46:14,527[38;5;243m - [0m[38;5;177mfreqtrade.loggers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLogfile configured
2026-06-19 06:46:14,528[38;5;243m - [0m[38;5;177mfreqtrade.loggers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mVerbosity set to 0
2026-06-19 06:46:14,528[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter -i/--timeframe detected ... Using timeframe: 15m ...
2026-06-19 06:46:14,529[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter --fee detected, setting fee to: 0.0 ...
2026-06-19 06:46:14,529[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter --timerange detected: 20250101-20260101 ...
2026-06-19 06:46:14,530[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing user-data directory: /home/fayez/freqtrade/user_data ...
2026-06-19 06:46:14,530[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing data directory: /home/fayez/freqtrade/user_data/data/binance ...
2026-06-19 06:46:14,531[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing pairs ['EUR/USDT']
2026-06-19 06:46:14,531[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mFilter trades by timerange: 20250101-20260101
2026-06-19 06:46:14,531[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mTargeted Trade amount: 100
2026-06-19 06:46:14,532[38;5;243m - [0m[38;5;177mfreqtrade.exchange.check_exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mChecking exchange...
2026-06-19 06:46:14,543[38;5;243m - [0m[38;5;177mfreqtrade.exchange.check_exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mExchange "binance" is officially supported by the Freqtrade development team.
2026-06-19 06:46:14,543[38;5;243m - [0m[38;5;177mfreqtrade.configuration.config_validation[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mValidating configuration ...
2026-06-19 06:46:14,547[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mForced order_types to market orders.
2026-06-19 06:46:14,547[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mForced max_open_trades to -1 (same amount as there are pairs)
2026-06-19 06:46:14,548[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mDry run wallet was not set to 1 billion, pushing it up there just to avoid false positives
2026-06-19 06:46:14,548[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mfixing stake_amount to 10k
2026-06-19 06:46:14,564[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR072.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR072.py, line 34)'
2026-06-19 06:46:14,565[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR069.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR069.py, line 34)'
2026-06-19 06:46:14,571[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR061.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR061.py, line 34)'
2026-06-19 06:46:14,573[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR062.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR062.py, line 34)'
2026-06-19 06:46:14,575[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR060.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR060.py, line 34)'
2026-06-19 06:46:14,577[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR074.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR074.py, line 34)'
2026-06-19 06:46:14,578[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR068.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR068.py, line 34)'
2026-06-19 06:46:14,583[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR073.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR073.py, line 34)'
2026-06-19 06:46:14,590[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR071.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR071.py, line 34)'
2026-06-19 06:46:14,595[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR065.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR065.py, line 34)'
2026-06-19 06:46:14,596[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mBias test of VWAPPullback.py started.
2026-06-19 06:46:14,598[38;5;243m - [0m[38;5;177mfreqtrade.exchange.exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mInstance is running with dry_run enabled
2026-06-19 06:46:14,599[38;5;243m - [0m[38;5;177mfreqtrade.exchange.exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing CCXT 4.5.58
2026-06-19 06:46:14,619[38;5;243m - [0m[38;5;177mfreqtrade.exchange.exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing Exchange "Binance"
2026-06-19 06:46:16,225[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.exchange_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing resolved exchange 'Binance'...
2026-06-19 06:46:16,234[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing resolved strategy VWAPPullback from '/home/fayez/freqtrade/user_data/strategies/VWAPPullback.py'...
2026-06-19 06:46:16,235[38;5;243m - [0m[38;5;177mfreqtrade.strategy.hyper[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mFound no parameter file.
2026-06-19 06:46:16,235[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'timeframe' with value from the configuration: 15m.
2026-06-19 06:46:16,236[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'order_types' with value from the configuration: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 
'stoploss_on_exchange': False}.
2026-06-19 06:46:16,236[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'stake_currency' with value from the configuration: USDT.
2026-06-19 06:46:16,237[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'stake_amount' with value from the configuration: 10000.
2026-06-19 06:46:16,237[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'unfilledtimeout' with value from the configuration: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 
'unit': 'minutes'}.
2026-06-19 06:46:16,238[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'max_open_trades' with value from the configuration: -1.
2026-06-19 06:46:16,238[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using minimal_roi: {'0': 0.015}
2026-06-19 06:46:16,238[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using timeframe: 15m
2026-06-19 06:46:16,239[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using stoploss: -0.015
2026-06-19 06:46:16,239[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using trailing_stop: False
2026-06-19 06:46:16,240[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using trailing_stop_positive_offset: 0.0
2026-06-19 06:46:16,240[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using trailing_only_offset_is_reached: False
2026-06-19 06:46:16,241[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using use_custom_stoploss: False
2026-06-19 06:46:16,241[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using process_only_new_candles: True
2026-06-19 06:46:16,241[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using order_types: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 'stoploss_on_exchange': False}
2026-06-19 06:46:16,242[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2026-06-19 06:46:16,242[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using stake_currency: USDT
2026-06-19 06:46:16,243[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using stake_amount: 10000
2026-06-19 06:46:16,243[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using startup_candle_count: 0
2026-06-19 06:46:16,244[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2026-06-19 06:46:16,244[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using use_exit_signal: True
2026-06-19 06:46:16,245[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using exit_profit_only: False
2026-06-19 06:46:16,245[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using ignore_roi_if_entry_signal: False
2026-06-19 06:46:16,245[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using exit_profit_offset: 0.0
2026-06-19 06:46:16,246[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using disable_dataframe_checks: False
2026-06-19 06:46:16,246[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using ignore_buying_expired_candle_after: 0
2026-06-19 06:46:16,247[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using position_adjustment_enable: False
2026-06-19 06:46:16,247[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using max_entry_position_adjustment: -1
2026-06-19 06:46:16,247[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using max_open_trades: -1
2026-06-19 06:46:16,248[38;5;243m - [0m[38;5;177mfreqtrade.configuration.config_validation[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mValidating configuration ...
2026-06-19 06:46:16,254[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing resolved pairlist StaticPairList from '/home/fayez/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2026-06-19 06:46:16,277[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing fee 0.0000% from config.
2026-06-19 06:46:16,339[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 24900 - after: 34944 - 40.34%
2026-06-19 06:46:16,340[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-31 21:45:00 (363 days).
2026-06-19 06:46:19,275[38;5;243m - [0m[38;5;177mfreqtrade.loggers.set_log_levels[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mReducing verbosity for bias tester.
2026-06-19 06:46:19,276[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOnly found 22 trades. Calculating all available trades.
2026-06-19 06:46:19,343[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 718 - after: 1102 - 53.48%
2026-06-19 06:46:19,344[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-13 09:15:00 (11 days).
2026-06-19 06:46:19,496[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 1216 - after: 1792 - 47.37%
2026-06-19 06:46:19,497[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-20 13:45:00 (18 days).
2026-06-19 06:46:19,733[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 1257 - after: 1833 - 45.82%
2026-06-19 06:46:19,734[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-21 00:00:00 (19 days).
2026-06-19 06:46:19,924[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 2114 - after: 3074 - 45.41%
2026-06-19 06:46:19,925[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-02 22:15:00 (32 days).
2026-06-19 06:46:20,264[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 2473 - after: 3433 - 38.82%
2026-06-19 06:46:20,266[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-06 16:00:00 (35 days).
2026-06-19 06:46:20,595[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 3570 - after: 5106 - 43.03%
2026-06-19 06:46:20,597[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-24 02:15:00 (53 days).
2026-06-19 06:46:21,109[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 3723 - after: 5259 - 41.26%
2026-06-19 06:46:21,110[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-25 16:30:00 (54 days).
2026-06-19 06:46:21,432[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4264 - after: 5992 - 40.53%
2026-06-19 06:46:21,433[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-05 07:45:00 (62 days).
2026-06-19 06:46:21,803[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4365 - after: 6093 - 39.59%
2026-06-19 06:46:21,804[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-06 09:00:00 (63 days).
2026-06-19 06:46:22,130[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6280 - after: 8772 - 39.68%
2026-06-19 06:46:22,131[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-03 06:45:00 (91 days).
2026-06-19 06:46:22,690[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6363 - after: 8855 - 39.16%
2026-06-19 06:46:22,691[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-04 03:30:00 (92 days).
2026-06-19 06:46:23,261[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6434 - after: 9118 - 41.72%
2026-06-19 06:46:23,262[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-06 21:15:00 (94 days).
2026-06-19 06:46:23,892[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6452 - after: 9136 - 41.60%
2026-06-19 06:46:23,894[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-07 01:45:00 (95 days).
2026-06-19 06:46:24,530[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6789 - after: 9473 - 39.53%
2026-06-19 06:46:24,531[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-10 14:00:00 (98 days).
2026-06-19 06:46:25,125[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6951 - after: 9827 - 41.38%
2026-06-19 06:46:25,126[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-14 06:30:00 (102 days).
2026-06-19 06:46:25,707[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 7437 - after: 10505 - 41.25%
2026-06-19 06:46:25,709[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-21 08:00:00 (109 days).
2026-06-19 06:46:26,357[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 7514 - after: 10582 - 40.83%
2026-06-19 06:46:26,358[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-22 03:15:00 (110 days).
2026-06-19 06:46:26,944[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 7590 - after: 10658 - 40.42%
2026-06-19 06:46:26,944[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-22 22:15:00 (111 days).
2026-06-19 06:46:27,542[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 7628 - after: 10696 - 40.22%
2026-06-19 06:46:27,543[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-23 07:45:00 (111 days).
2026-06-19 06:46:28,136[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8718 - after: 12170 - 39.60%
2026-06-19 06:46:28,137[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-08 16:15:00 (126 days).
2026-06-19 06:46:28,905[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8765 - after: 12217 - 39.38%
2026-06-19 06:46:28,906[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-09 04:00:00 (127 days).
2026-06-19 06:46:29,900[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 9807 - after: 13835 - 41.07%
2026-06-19 06:46:29,902[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-26 00:30:00 (144 days).
2026-06-19 06:46:30,810[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 9911 - after: 13939 - 40.64%
2026-06-19 06:46:30,811[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-27 02:30:00 (145 days).
2026-06-19 06:46:32,048[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 10092 - after: 14120 - 39.91%
2026-06-19 06:46:32,049[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-28 23:45:00 (147 days).
2026-06-19 06:46:33,357[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 10442 - after: 14662 - 40.41%
2026-06-19 06:46:33,358[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-03 15:15:00 (152 days).
2026-06-19 06:46:34,628[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 11091 - after: 15503 - 39.78%
2026-06-19 06:46:34,630[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-12 09:30:00 (161 days).
2026-06-19 06:46:35,898[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 11490 - after: 16094 - 40.07%
2026-06-19 06:46:35,899[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-18 13:15:00 (167 days).
2026-06-19 06:46:36,756[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 12012 - after: 16808 - 39.93%
2026-06-19 06:46:36,757[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-25 23:45:00 (175 days).
2026-06-19 06:46:37,706[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 12150 - after: 16946 - 39.47%
2026-06-19 06:46:37,707[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-27 10:15:00 (176 days).
2026-06-19 06:46:38,624[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 14249 - after: 20005 - 40.40%
2026-06-19 06:46:38,625[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-29 07:00:00 (208 days).
2026-06-19 06:46:39,759[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 14334 - after: 20090 - 40.16%
2026-06-19 06:46:39,760[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-30 04:15:00 (209 days).
2026-06-19 06:46:41,161[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 16019 - after: 22351 - 39.53%
2026-06-19 06:46:41,162[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-22 17:30:00 (232 days).
2026-06-19 06:46:42,431[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 16195 - after: 22719 - 40.28%
2026-06-19 06:46:42,431[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-26 13:30:00 (236 days).
2026-06-19 06:46:43,699[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 17635 - after: 24735 - 40.26%
2026-06-19 06:46:43,700[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-16 13:30:00 (257 days).
2026-06-19 06:46:45,075[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 17778 - after: 24878 - 39.94%
2026-06-19 06:46:45,076[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-18 01:15:00 (259 days).
2026-06-19 06:46:47,239[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 18326 - after: 25618 - 39.79%
2026-06-19 06:46:47,241[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-25 18:15:00 (266 days).
2026-06-19 06:46:49,442[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 18401 - after: 25693 - 39.63%
2026-06-19 06:46:49,443[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-26 13:00:00 (267 days).
2026-06-19 06:46:51,698[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 20943 - after: 29391 - 40.34%
2026-06-19 06:46:51,699[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-11-04 01:30:00 (306 days).
2026-06-19 06:46:53,852[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 21171 - after: 29619 - 39.90%
2026-06-19 06:46:53,853[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-11-06 10:30:00 (308 days).
2026-06-19 06:46:55,420[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 23514 - after: 32922 - 40.01%
2026-06-19 06:46:55,421[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-10 20:15:00 (342 days).
2026-06-19 06:46:57,695[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mfound force-exit in pair: EUR/USDT, timerange:2025-12-16 14:00:00+00:00-2025-12-31 21:45:00+00:00, idx: 20, skipping this one 
to avoid a false-positive.
2026-06-19 06:46:57,695[38;5;243m - [0m[38;5;177mfreqtrade.loggers.set_log_levels[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mRestoring log verbosity.
2026-06-19 06:46:57,696[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mVWAPPullback: no bias detected
2026-06-19 06:46:57,696[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mChecking look ahead bias via backtests of VWAPPullback.py took 43 seconds.

```


**رمز الخروج:** 0
