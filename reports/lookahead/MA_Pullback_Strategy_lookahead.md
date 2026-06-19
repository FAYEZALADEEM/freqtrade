# تقرير Lookahead Analysis: MA_Pullback_Strategy

**التاريخ:** 2026-06-19 06:47
**الأمر:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade lookahead-analysis --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --config <(echo '{"entry_pricing": {"price_side": "other"}, "exit_pricing": {"price_side": "other"}}') --strategy MA_Pullback_Strategy --timeframe 15m --timerange 20250101-20260101 --fee 0 --targeted-trade-amount 100 -p EUR/USDT
```

## قاعدة التحقق المطبقة

- `targeted_trade_amount = 100` (ثابت حسب القاعدة الدائمة)
- يتم فحص حتى 100 إشارة. إذا كان عدد الإشارات أقل، يتم التوضيح.

## النتائج

```
[3m                                                              Lookahead Analysis                                                              [0m
┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃[1m [0m[1m               filename[0m[1m [0m┃[1m [0m[1m            strategy[0m[1m [0m┃[1m [0m[1mhas_bias[0m[1m [0m┃[1m [0m[1mtotal_signals[0m[1m [0m┃[1m [0m[1mbiased_entry_signals[0m[1m [0m┃[1m [0m[1mbiased_exit_signals[0m[1m [0m┃[1m [0m[1mbiased_indicators[0m[1m [0m┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ MA_Pullback_Strategy.py │ MA_Pullback_Strategy │ [1;32m      No[0m │            86 │                    0 │                   0 │                   │
└─────────────────────────┴──────────────────────┴──────────┴───────────────┴──────────────────────┴─────────────────────┴───────────────────┘

2026-06-19 06:45:13,601 - freqtrade - INFO - freqtrade 2026.6-dev-a29762684
2026-06-19 06:45:13,832 - numexpr.utils - INFO - NumExpr defaulting to 8 threads.
2026-06-19 06:45:14,748 - freqtrade.configuration.load_config - INFO - Using config: user_data/config.json ...
2026-06-19 06:45:14,749 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/63 ...
2026-06-19 06:45:14,749 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/62 ...
2026-06-19 06:45:14,751 - freqtrade.loggers - INFO - Enabling colorized output.
2026-06-19 06:45:14,752[38;5;243m - [0m[38;5;177mfreqtrade.loggers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLogfile configured
2026-06-19 06:45:14,752[38;5;243m - [0m[38;5;177mfreqtrade.loggers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mVerbosity set to 0
2026-06-19 06:45:14,753[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter -i/--timeframe detected ... Using timeframe: 15m ...
2026-06-19 06:45:14,753[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter --fee detected, setting fee to: 0.0 ...
2026-06-19 06:45:14,753[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter --timerange detected: 20250101-20260101 ...
2026-06-19 06:45:14,754[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing user-data directory: /home/fayez/freqtrade/user_data ...
2026-06-19 06:45:14,755[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing data directory: /home/fayez/freqtrade/user_data/data/binance ...
2026-06-19 06:45:14,755[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing pairs ['EUR/USDT']
2026-06-19 06:45:14,756[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mFilter trades by timerange: 20250101-20260101
2026-06-19 06:45:14,756[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mTargeted Trade amount: 100
2026-06-19 06:45:14,757[38;5;243m - [0m[38;5;177mfreqtrade.exchange.check_exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mChecking exchange...
2026-06-19 06:45:14,768[38;5;243m - [0m[38;5;177mfreqtrade.exchange.check_exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mExchange "binance" is officially supported by the Freqtrade development team.
2026-06-19 06:45:14,769[38;5;243m - [0m[38;5;177mfreqtrade.configuration.config_validation[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mValidating configuration ...
2026-06-19 06:45:14,772[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mForced order_types to market orders.
2026-06-19 06:45:14,772[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mForced max_open_trades to -1 (same amount as there are pairs)
2026-06-19 06:45:14,773[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mDry run wallet was not set to 1 billion, pushing it up there just to avoid false positives
2026-06-19 06:45:14,773[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mfixing stake_amount to 10k
2026-06-19 06:45:14,784[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR072.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR072.py, line 34)'
2026-06-19 06:45:14,785[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR069.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR069.py, line 34)'
2026-06-19 06:45:14,789[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR061.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR061.py, line 34)'
2026-06-19 06:45:14,790[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR062.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR062.py, line 34)'
2026-06-19 06:45:14,792[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR060.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR060.py, line 34)'
2026-06-19 06:45:14,793[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR074.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR074.py, line 34)'
2026-06-19 06:45:14,794[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR068.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR068.py, line 34)'
2026-06-19 06:45:14,797[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR073.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR073.py, line 34)'
2026-06-19 06:45:14,802[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR071.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR071.py, line 34)'
2026-06-19 06:45:14,806[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR065.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR065.py, line 34)'
2026-06-19 06:45:14,807[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mBias test of MA_Pullback_Strategy.py started.
2026-06-19 06:45:14,809[38;5;243m - [0m[38;5;177mfreqtrade.exchange.exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mInstance is running with dry_run enabled
2026-06-19 06:45:14,809[38;5;243m - [0m[38;5;177mfreqtrade.exchange.exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing CCXT 4.5.58
2026-06-19 06:45:14,825[38;5;243m - [0m[38;5;177mfreqtrade.exchange.exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing Exchange "Binance"
2026-06-19 06:45:16,168[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.exchange_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing resolved exchange 'Binance'...
2026-06-19 06:45:16,174[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing resolved strategy MA_Pullback_Strategy from '/home/fayez/freqtrade/user_data/strategies/MA_Pullback_Strategy.py'...
2026-06-19 06:45:16,175[38;5;243m - [0m[38;5;177mfreqtrade.strategy.hyper[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mFound no parameter file.
2026-06-19 06:45:16,175[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'timeframe' with value from the configuration: 15m.
2026-06-19 06:45:16,176[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'order_types' with value from the configuration: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 
'stoploss_on_exchange': False}.
2026-06-19 06:45:16,176[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'stake_currency' with value from the configuration: USDT.
2026-06-19 06:45:16,177[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'stake_amount' with value from the configuration: 10000.
2026-06-19 06:45:16,177[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'unfilledtimeout' with value from the configuration: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 
'unit': 'minutes'}.
2026-06-19 06:45:16,178[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'max_open_trades' with value from the configuration: -1.
2026-06-19 06:45:16,178[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using minimal_roi: {'0': 0.008}
2026-06-19 06:45:16,178[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using timeframe: 15m
2026-06-19 06:45:16,178[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using stoploss: -0.002
2026-06-19 06:45:16,179[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using trailing_stop: False
2026-06-19 06:45:16,179[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using trailing_stop_positive_offset: 0.0
2026-06-19 06:45:16,179[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using trailing_only_offset_is_reached: False
2026-06-19 06:45:16,180[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using use_custom_stoploss: False
2026-06-19 06:45:16,180[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using process_only_new_candles: True
2026-06-19 06:45:16,180[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using order_types: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 'stoploss_on_exchange': False}
2026-06-19 06:45:16,180[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2026-06-19 06:45:16,181[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using stake_currency: USDT
2026-06-19 06:45:16,181[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using stake_amount: 10000
2026-06-19 06:45:16,181[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using startup_candle_count: 0
2026-06-19 06:45:16,181[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2026-06-19 06:45:16,182[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using use_exit_signal: True
2026-06-19 06:45:16,182[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using exit_profit_only: False
2026-06-19 06:45:16,182[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using ignore_roi_if_entry_signal: False
2026-06-19 06:45:16,183[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using exit_profit_offset: 0.0
2026-06-19 06:45:16,183[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using disable_dataframe_checks: False
2026-06-19 06:45:16,183[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using ignore_buying_expired_candle_after: 0
2026-06-19 06:45:16,183[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using position_adjustment_enable: False
2026-06-19 06:45:16,184[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using max_entry_position_adjustment: -1
2026-06-19 06:45:16,184[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using max_open_trades: -1
2026-06-19 06:45:16,184[38;5;243m - [0m[38;5;177mfreqtrade.configuration.config_validation[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mValidating configuration ...
2026-06-19 06:45:16,189[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing resolved pairlist StaticPairList from '/home/fayez/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2026-06-19 06:45:16,202[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing fee 0.0000% from config.
2026-06-19 06:45:16,261[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 24900 - after: 34944 - 40.34%
2026-06-19 06:45:16,262[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-31 21:45:00 (363 days).
2026-06-19 06:45:17,880[38;5;243m - [0m[38;5;177mfreqtrade.loggers.set_log_levels[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mReducing verbosity for bias tester.
2026-06-19 06:45:17,880[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOnly found 87 trades. Calculating all available trades.
2026-06-19 06:45:17,923[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 229 - after: 421 - 83.84%
2026-06-19 06:45:17,924[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-06 07:00:00 (4 days).
2026-06-19 06:45:18,007[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 239 - after: 431 - 80.33%
2026-06-19 06:45:18,008[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-06 09:30:00 (4 days).
2026-06-19 06:45:18,106[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 833 - after: 1217 - 46.10%
2026-06-19 06:45:18,107[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-14 14:00:00 (12 days).
2026-06-19 06:45:18,216[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 842 - after: 1226 - 45.61%
2026-06-19 06:45:18,217[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-14 16:15:00 (12 days).
2026-06-19 06:45:18,345[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 1365 - after: 1941 - 42.20%
2026-06-19 06:45:18,346[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-22 03:00:00 (20 days).
2026-06-19 06:45:18,455[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 1396 - after: 1972 - 41.26%
2026-06-19 06:45:18,456[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-22 10:45:00 (20 days).
2026-06-19 06:45:18,600[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 2566 - after: 3526 - 37.41%
2026-06-19 06:45:18,601[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-07 15:15:00 (36 days).
2026-06-19 06:45:18,761[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 2569 - after: 3529 - 37.37%
2026-06-19 06:45:18,761[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-07 16:00:00 (36 days).
2026-06-19 06:45:18,921[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 2927 - after: 4079 - 39.36%
2026-06-19 06:45:18,922[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-13 09:30:00 (42 days).
2026-06-19 06:45:19,105[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 2937 - after: 4089 - 39.22%
2026-06-19 06:45:19,106[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-13 12:00:00 (42 days).
2026-06-19 06:45:19,284[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 3079 - after: 4423 - 43.65%
2026-06-19 06:45:19,285[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-16 23:30:00 (46 days).
2026-06-19 06:45:19,447[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 3116 - after: 4460 - 43.13%
2026-06-19 06:45:19,447[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-17 08:45:00 (46 days).
2026-06-19 06:45:19,644[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 3126 - after: 4470 - 42.99%
2026-06-19 06:45:19,645[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-17 11:15:00 (46 days).
2026-06-19 06:45:19,816[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 3135 - after: 4479 - 42.87%
2026-06-19 06:45:19,816[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-17 13:30:00 (46 days).
2026-06-19 06:45:20,021[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 3495 - after: 4839 - 38.45%
2026-06-19 06:45:20,021[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-21 07:30:00 (50 days).
2026-06-19 06:45:20,204[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 3499 - after: 4843 - 38.41%
2026-06-19 06:45:20,204[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-21 08:30:00 (50 days).
2026-06-19 06:45:20,415[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 3635 - after: 5171 - 42.26%
2026-06-19 06:45:20,416[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-24 18:30:00 (53 days).
2026-06-19 06:45:20,623[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 3690 - after: 5226 - 41.63%
2026-06-19 06:45:20,624[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-25 08:15:00 (54 days).
2026-06-19 06:45:20,868[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 3691 - after: 5227 - 41.61%
2026-06-19 06:45:20,869[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-25 08:30:00 (54 days).
2026-06-19 06:45:21,082[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 3720 - after: 5256 - 41.29%
2026-06-19 06:45:21,083[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-25 15:45:00 (54 days).
2026-06-19 06:45:21,386[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 3816 - after: 5352 - 40.25%
2026-06-19 06:45:21,387[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-26 15:45:00 (55 days).
2026-06-19 06:45:21,626[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 3854 - after: 5390 - 39.85%
2026-06-19 06:45:21,627[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-27 01:15:00 (56 days).
2026-06-19 06:45:21,921[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4142 - after: 5870 - 41.72%
2026-06-19 06:45:21,922[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-04 01:15:00 (61 days).
2026-06-19 06:45:22,228[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4186 - after: 5914 - 41.28%
2026-06-19 06:45:22,229[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-04 12:15:00 (61 days).
2026-06-19 06:45:22,533[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4201 - after: 5929 - 41.13%
2026-06-19 06:45:22,534[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-04 16:00:00 (61 days).
2026-06-19 06:45:22,763[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4211 - after: 5939 - 41.04%
2026-06-19 06:45:22,764[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-04 18:30:00 (61 days).
2026-06-19 06:45:23,019[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4490 - after: 6218 - 38.49%
2026-06-19 06:45:23,020[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-07 16:15:00 (64 days).
2026-06-19 06:45:23,261[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4491 - after: 6219 - 38.48%
2026-06-19 06:45:23,262[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-07 16:30:00 (64 days).
2026-06-19 06:45:23,550[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4508 - after: 6236 - 38.33%
2026-06-19 06:45:23,551[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-07 20:45:00 (64 days).
2026-06-19 06:45:23,788[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4557 - after: 6473 - 42.05%
2026-06-19 06:45:23,788[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-10 08:00:00 (67 days).
2026-06-19 06:45:24,074[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4705 - after: 6621 - 40.72%
2026-06-19 06:45:24,075[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-11 21:00:00 (68 days).
2026-06-19 06:45:24,350[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4738 - after: 6654 - 40.44%
2026-06-19 06:45:24,351[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-12 05:15:00 (69 days).
2026-06-19 06:45:24,660[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4763 - after: 6679 - 40.23%
2026-06-19 06:45:24,661[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-12 11:30:00 (69 days).
2026-06-19 06:45:24,987[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4767 - after: 6683 - 40.19%
2026-06-19 06:45:24,988[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-12 12:30:00 (69 days).
2026-06-19 06:45:25,429[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4975 - after: 6891 - 38.51%
2026-06-19 06:45:25,430[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-14 16:30:00 (71 days).
2026-06-19 06:45:25,770[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 5068 - after: 7176 - 41.59%
2026-06-19 06:45:25,771[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-17 15:45:00 (74 days).
2026-06-19 06:45:26,150[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 5505 - after: 7805 - 41.78%
2026-06-19 06:45:26,151[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-24 05:00:00 (81 days).
2026-06-19 06:45:26,568[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 5541 - after: 7841 - 41.51%
2026-06-19 06:45:26,569[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-24 14:00:00 (81 days).
2026-06-19 06:45:27,076[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 5874 - after: 8174 - 39.16%
2026-06-19 06:45:27,078[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-28 01:15:00 (85 days).
2026-06-19 06:45:27,521[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 5907 - after: 8207 - 38.94%
2026-06-19 06:45:27,522[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-28 09:30:00 (85 days).
2026-06-19 06:45:27,974[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 5965 - after: 8457 - 41.78%
2026-06-19 06:45:27,975[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-31 00:00:00 (88 days).
2026-06-19 06:45:28,373[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6022 - after: 8514 - 41.38%
2026-06-19 06:45:28,374[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-31 14:15:00 (88 days).
2026-06-19 06:45:28,851[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6328 - after: 8820 - 39.38%
2026-06-19 06:45:28,852[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-03 18:45:00 (91 days).
2026-06-19 06:45:29,384[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6359 - after: 8851 - 39.19%
2026-06-19 06:45:29,385[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-04 02:30:00 (92 days).
2026-06-19 06:45:29,873[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6379 - after: 8871 - 39.07%
2026-06-19 06:45:29,874[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-04 07:30:00 (92 days).
2026-06-19 06:45:30,335[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6380 - after: 8872 - 39.06%
2026-06-19 06:45:30,336[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-04 07:45:00 (92 days).
2026-06-19 06:45:30,866[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6395 - after: 8887 - 38.97%
2026-06-19 06:45:30,867[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-04 11:30:00 (92 days).
2026-06-19 06:45:31,335[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6400 - after: 8892 - 38.94%
2026-06-19 06:45:31,335[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-04 12:45:00 (92 days).
2026-06-19 06:45:31,840[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6450 - after: 9134 - 41.61%
2026-06-19 06:45:31,841[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-07 01:15:00 (95 days).
2026-06-19 06:45:32,326[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6455 - after: 9139 - 41.58%
2026-06-19 06:45:32,327[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-07 02:30:00 (95 days).
2026-06-19 06:45:32,880[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6593 - after: 9277 - 40.71%
2026-06-19 06:45:32,881[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-08 13:00:00 (96 days).
2026-06-19 06:45:33,304[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6596 - after: 9280 - 40.69%
2026-06-19 06:45:33,305[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-08 13:45:00 (96 days).
2026-06-19 06:45:33,861[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6672 - after: 9356 - 40.23%
2026-06-19 06:45:33,862[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-09 08:45:00 (97 days).
2026-06-19 06:45:34,425[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6688 - after: 9372 - 40.13%
2026-06-19 06:45:34,426[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-09 12:45:00 (97 days).
2026-06-19 06:45:34,963[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6857 - after: 9541 - 39.14%
2026-06-19 06:45:34,964[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-11 07:00:00 (99 days).
2026-06-19 06:45:35,492[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6859 - after: 9543 - 39.13%
2026-06-19 06:45:35,493[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-11 07:30:00 (99 days).
2026-06-19 06:45:36,031[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6948 - after: 9824 - 41.39%
2026-06-19 06:45:36,032[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-14 05:45:00 (102 days).
2026-06-19 06:45:36,490[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6975 - after: 9851 - 41.23%
2026-06-19 06:45:36,490[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-14 12:30:00 (102 days).
2026-06-19 06:45:36,961[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6988 - after: 9864 - 41.16%
2026-06-19 06:45:36,961[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-14 15:45:00 (102 days).
2026-06-19 06:45:37,392[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6991 - after: 9867 - 41.14%
2026-06-19 06:45:37,393[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-14 16:30:00 (102 days).
2026-06-19 06:45:37,848[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 7225 - after: 10101 - 39.81%
2026-06-19 06:45:37,849[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-17 03:00:00 (105 days).
2026-06-19 06:45:38,289[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 7236 - after: 10112 - 39.75%
2026-06-19 06:45:38,289[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-17 05:45:00 (105 days).
2026-06-19 06:45:38,801[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 7987 - after: 11247 - 40.82%
2026-06-19 06:45:38,802[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-29 01:30:00 (117 days).
2026-06-19 06:45:39,321[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8000 - after: 11260 - 40.75%
2026-06-19 06:45:39,322[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-29 04:45:00 (117 days).
2026-06-19 06:45:39,853[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8040 - after: 11300 - 40.55%
2026-06-19 06:45:39,854[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-29 14:45:00 (117 days).
2026-06-19 06:45:40,338[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8041 - after: 11301 - 40.54%
2026-06-19 06:45:40,339[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-29 15:00:00 (117 days).
2026-06-19 06:45:40,858[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8335 - after: 11595 - 39.11%
2026-06-19 06:45:40,859[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-02 16:30:00 (120 days).
2026-06-19 06:45:41,377[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8338 - after: 11598 - 39.10%
2026-06-19 06:45:41,378[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-02 17:15:00 (120 days).
2026-06-19 06:45:41,903[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8399 - after: 11851 - 41.10%
2026-06-19 06:45:41,903[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-05 08:30:00 (123 days).
2026-06-19 06:45:42,375[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8430 - after: 11882 - 40.95%
2026-06-19 06:45:42,376[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-05 16:15:00 (123 days).
2026-06-19 06:45:42,866[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8478 - after: 11930 - 40.72%
2026-06-19 06:45:42,867[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-06 04:15:00 (124 days).
2026-06-19 06:45:43,361[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8531 - after: 11983 - 40.46%
2026-06-19 06:45:43,362[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-06 17:30:00 (124 days).
2026-06-19 06:45:43,920[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8559 - after: 12011 - 40.33%
2026-06-19 06:45:43,921[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-07 00:30:00 (125 days).
2026-06-19 06:45:44,522[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8559 - after: 12011 - 40.33%
2026-06-19 06:45:44,522[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-07 00:30:00 (125 days).
2026-06-19 06:45:45,079[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 9088 - after: 12732 - 40.10%
2026-06-19 06:45:45,080[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-14 12:45:00 (132 days).
2026-06-19 06:45:45,672[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 9099 - after: 12743 - 40.05%
2026-06-19 06:45:45,673[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-14 15:30:00 (132 days).
2026-06-19 06:45:46,231[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 9138 - after: 12782 - 39.88%
2026-06-19 06:45:46,231[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-15 01:15:00 (133 days).
2026-06-19 06:45:46,754[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 9288 - after: 12932 - 39.23%
2026-06-19 06:45:46,755[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-16 14:45:00 (134 days).
2026-06-19 06:45:47,314[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 9406 - after: 13242 - 40.78%
2026-06-19 06:45:47,315[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-19 20:15:00 (137 days).
2026-06-19 06:45:47,875[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 9501 - after: 13337 - 40.37%
2026-06-19 06:45:47,876[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-20 20:00:00 (138 days).
2026-06-19 06:45:48,484[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 9760 - after: 13596 - 39.30%
2026-06-19 06:45:48,485[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-23 12:45:00 (141 days).
2026-06-19 06:45:49,185[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 9783 - after: 13619 - 39.21%
2026-06-19 06:45:49,185[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-23 18:30:00 (141 days).
2026-06-19 06:45:49,897[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 10302 - after: 14522 - 40.96%
2026-06-19 06:45:49,897[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-02 04:15:00 (151 days).
2026-06-19 06:45:50,611[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 10313 - after: 14533 - 40.92%
2026-06-19 06:45:50,612[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-02 07:00:00 (151 days).
2026-06-19 06:45:51,353[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 10389 - after: 14609 - 40.62%
2026-06-19 06:45:51,354[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-03 02:00:00 (152 days).
2026-06-19 06:45:52,048[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 10414 - after: 14634 - 40.52%
2026-06-19 06:45:52,049[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-03 08:15:00 (152 days).
2026-06-19 06:45:52,743[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 10771 - after: 15183 - 40.96%
2026-06-19 06:45:52,743[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-09 01:30:00 (158 days).
2026-06-19 06:45:53,480[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 10890 - after: 15302 - 40.51%
2026-06-19 06:45:53,481[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-10 07:15:00 (159 days).
2026-06-19 06:45:54,720[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 11222 - after: 15634 - 39.32%
2026-06-19 06:45:54,721[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-13 18:15:00 (162 days).
2026-06-19 06:45:55,477[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 11234 - after: 15838 - 40.98%
2026-06-19 06:45:55,477[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-15 21:15:00 (164 days).
2026-06-19 06:45:56,284[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 11318 - after: 15922 - 40.68%
2026-06-19 06:45:56,286[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-16 18:15:00 (165 days).
2026-06-19 06:45:57,058[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 11325 - after: 15929 - 40.65%
2026-06-19 06:45:57,059[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-16 20:00:00 (165 days).
2026-06-19 06:45:57,844[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 11358 - after: 15962 - 40.54%
2026-06-19 06:45:57,845[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-17 04:15:00 (166 days).
2026-06-19 06:45:59,003[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 11399 - after: 16003 - 40.39%
2026-06-19 06:45:59,004[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-17 14:30:00 (166 days).
2026-06-19 06:46:00,225[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 11678 - after: 16282 - 39.42%
2026-06-19 06:46:00,226[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-20 12:15:00 (169 days).
2026-06-19 06:46:01,148[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 11689 - after: 16293 - 39.39%
2026-06-19 06:46:01,152[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-20 15:00:00 (169 days).
2026-06-19 06:46:01,967[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 12331 - after: 17319 - 40.45%
2026-06-19 06:46:01,967[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-01 07:30:00 (180 days).
2026-06-19 06:46:02,715[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 12444 - after: 17432 - 40.08%
2026-06-19 06:46:02,715[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-02 11:45:00 (181 days).
2026-06-19 06:46:03,641[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 12505 - after: 17493 - 39.89%
2026-06-19 06:46:03,641[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-03 03:00:00 (182 days).
2026-06-19 06:46:04,502[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 12544 - after: 17532 - 39.76%
2026-06-19 06:46:04,503[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-03 12:45:00 (182 days).
2026-06-19 06:46:05,377[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 12623 - after: 17611 - 39.52%
2026-06-19 06:46:05,378[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-04 08:30:00 (183 days).
2026-06-19 06:46:06,537[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 12712 - after: 17892 - 40.75%
2026-06-19 06:46:06,538[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-07 06:45:00 (186 days).
2026-06-19 06:46:07,643[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 13006 - after: 18186 - 39.83%
2026-06-19 06:46:07,645[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-10 08:15:00 (189 days).
2026-06-19 06:46:08,990[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 13021 - after: 18201 - 39.78%
2026-06-19 06:46:08,991[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-10 12:00:00 (189 days).
2026-06-19 06:46:10,329[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 13292 - after: 18664 - 40.42%
2026-06-19 06:46:10,330[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-15 07:45:00 (194 days).
2026-06-19 06:46:11,328[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 13316 - after: 18688 - 40.34%
2026-06-19 06:46:11,329[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-15 13:45:00 (194 days).
2026-06-19 06:46:12,240[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 13651 - after: 19215 - 40.76%
2026-06-19 06:46:12,241[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-21 01:30:00 (200 days).
2026-06-19 06:46:13,652[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 13694 - after: 19258 - 40.63%
2026-06-19 06:46:13,653[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-21 12:15:00 (200 days).
2026-06-19 06:46:14,934[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 13840 - after: 19404 - 40.20%
2026-06-19 06:46:14,936[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-23 00:45:00 (202 days).
2026-06-19 06:46:16,078[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 13890 - after: 19454 - 40.06%
2026-06-19 06:46:16,079[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-23 13:15:00 (202 days).
2026-06-19 06:46:17,147[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 13996 - after: 19560 - 39.75%
2026-06-19 06:46:17,148[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-24 15:45:00 (203 days).
2026-06-19 06:46:18,334[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 14016 - after: 19580 - 39.70%
2026-06-19 06:46:18,335[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-24 20:45:00 (203 days).
2026-06-19 06:46:19,395[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 14619 - after: 20567 - 40.69%
2026-06-19 06:46:19,396[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-04 03:30:00 (214 days).
2026-06-19 06:46:20,575[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 14635 - after: 20583 - 40.64%
2026-06-19 06:46:20,576[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-04 07:30:00 (214 days).
2026-06-19 06:46:21,620[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 14937 - after: 20885 - 39.82%
2026-06-19 06:46:21,621[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-07 11:00:00 (217 days).
2026-06-19 06:46:22,592[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 14940 - after: 20888 - 39.81%
2026-06-19 06:46:22,593[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-07 11:45:00 (217 days).
2026-06-19 06:46:23,691[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 14999 - after: 20947 - 39.66%
2026-06-19 06:46:23,692[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-08 02:30:00 (218 days).
2026-06-19 06:46:25,022[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 15025 - after: 20973 - 39.59%
2026-06-19 06:46:25,023[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-08 09:00:00 (218 days).
2026-06-19 06:46:26,478[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 15332 - after: 21472 - 40.05%
2026-06-19 06:46:26,479[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-13 13:45:00 (223 days).
2026-06-19 06:46:27,471[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 15403 - after: 21543 - 39.86%
2026-06-19 06:46:27,472[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-14 07:30:00 (224 days).
2026-06-19 06:46:28,958[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 15418 - after: 21558 - 39.82%
2026-06-19 06:46:28,959[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-14 11:15:00 (224 days).
2026-06-19 06:46:30,165[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 15424 - after: 21564 - 39.81%
2026-06-19 06:46:30,166[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-14 12:45:00 (224 days).
2026-06-19 06:46:31,713[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 15568 - after: 21900 - 40.67%
2026-06-19 06:46:31,714[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-18 00:45:00 (228 days).
2026-06-19 06:46:32,831[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 15597 - after: 21929 - 40.60%
2026-06-19 06:46:32,832[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-18 08:00:00 (228 days).
2026-06-19 06:46:34,299[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 16427 - after: 22951 - 39.72%
2026-06-19 06:46:34,300[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-28 23:30:00 (239 days).
2026-06-19 06:46:35,876[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 16478 - after: 23002 - 39.59%
2026-06-19 06:46:35,878[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-29 12:15:00 (239 days).
2026-06-19 06:46:37,553[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 16579 - after: 23295 - 40.51%
2026-06-19 06:46:37,554[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-01 13:30:00 (242 days).
2026-06-19 06:46:39,149[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 16639 - after: 23355 - 40.36%
2026-06-19 06:46:39,150[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-02 04:30:00 (243 days).
2026-06-19 06:46:40,853[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 17010 - after: 23918 - 40.61%
2026-06-19 06:46:40,854[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-08 01:15:00 (249 days).
2026-06-19 06:46:42,492[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 17082 - after: 23990 - 40.44%
2026-06-19 06:46:42,493[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-08 19:15:00 (249 days).
2026-06-19 06:46:44,093[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 18475 - after: 25959 - 40.51%
2026-06-19 06:46:44,094[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-29 07:30:00 (270 days).
2026-06-19 06:46:45,314[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 18665 - after: 26149 - 40.10%
2026-06-19 06:46:45,315[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-10-01 07:00:00 (272 days).
2026-06-19 06:46:46,606[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 18688 - after: 26172 - 40.05%
2026-06-19 06:46:46,607[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-10-01 12:45:00 (272 days).
2026-06-19 06:46:48,049[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 18699 - after: 26183 - 40.02%
2026-06-19 06:46:48,050[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-10-01 15:30:00 (272 days).
2026-06-19 06:46:49,247[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 19431 - after: 27299 - 40.49%
2026-06-19 06:46:49,248[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-10-13 06:30:00 (284 days).
2026-06-19 06:46:50,733[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 19437 - after: 27305 - 40.48%
2026-06-19 06:46:50,734[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-10-13 08:00:00 (284 days).
2026-06-19 06:46:52,548[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 19725 - after: 27593 - 39.89%
2026-06-19 06:46:52,549[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-10-16 08:00:00 (287 days).
2026-06-19 06:46:54,370[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 19787 - after: 27655 - 39.76%
2026-06-19 06:46:54,371[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-10-16 23:30:00 (288 days).
2026-06-19 06:46:56,072[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 19913 - after: 27973 - 40.48%
2026-06-19 06:46:56,073[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-10-20 07:00:00 (291 days).
2026-06-19 06:46:57,490[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 19956 - after: 28016 - 40.39%
2026-06-19 06:46:57,491[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-10-20 17:45:00 (291 days).
2026-06-19 06:46:58,844[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 20360 - after: 28612 - 40.53%
2026-06-19 06:46:58,845[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-10-26 22:45:00 (298 days).
2026-06-19 06:47:00,069[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 20632 - after: 28884 - 40.00%
2026-06-19 06:47:00,070[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-10-29 18:45:00 (300 days).
2026-06-19 06:47:01,503[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 21232 - after: 29680 - 39.79%
2026-06-19 06:47:01,504[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-11-07 01:45:00 (309 days).
2026-06-19 06:47:02,972[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 21287 - after: 29735 - 39.69%
2026-06-19 06:47:02,973[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-11-07 15:30:00 (309 days).
2026-06-19 06:47:04,378[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 21307 - after: 29755 - 39.65%
2026-06-19 06:47:04,379[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-11-07 20:30:00 (309 days).
2026-06-19 06:47:05,710[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 21642 - after: 30282 - 39.92%
2026-06-19 06:47:05,711[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-11-13 08:15:00 (315 days).
2026-06-19 06:47:07,266[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 22219 - after: 31051 - 39.75%
2026-06-19 06:47:07,267[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-11-21 08:30:00 (323 days).
2026-06-19 06:47:08,693[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 22226 - after: 31058 - 39.74%
2026-06-19 06:47:08,694[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-11-21 10:15:00 (323 days).
2026-06-19 06:47:10,196[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 22362 - after: 31386 - 40.35%
2026-06-19 06:47:10,197[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-11-24 20:15:00 (326 days).
2026-06-19 06:47:11,817[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 22439 - after: 31463 - 40.22%
2026-06-19 06:47:11,818[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-11-25 15:30:00 (327 days).
2026-06-19 06:47:14,007[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 22511 - after: 31535 - 40.09%
2026-06-19 06:47:14,008[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-11-26 09:30:00 (328 days).
2026-06-19 06:47:15,588[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 22529 - after: 31553 - 40.06%
2026-06-19 06:47:15,589[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-11-26 14:00:00 (328 days).
2026-06-19 06:47:17,480[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 22832 - after: 32048 - 40.36%
2026-06-19 06:47:17,481[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-01 17:45:00 (333 days).
2026-06-19 06:47:19,506[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 22897 - after: 32113 - 40.25%
2026-06-19 06:47:19,507[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-02 10:00:00 (334 days).
2026-06-19 06:47:21,094[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 23095 - after: 32311 - 39.90%
2026-06-19 06:47:21,095[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-04 11:30:00 (336 days).
2026-06-19 06:47:23,281[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 23126 - after: 32342 - 39.85%
2026-06-19 06:47:23,283[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-04 19:15:00 (336 days).
2026-06-19 06:47:25,338[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 23166 - after: 32382 - 39.78%
2026-06-19 06:47:25,339[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-05 05:15:00 (337 days).
2026-06-19 06:47:26,768[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 23211 - after: 32427 - 39.71%
2026-06-19 06:47:26,769[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-05 16:30:00 (337 days).
2026-06-19 06:47:28,779[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 23281 - after: 32689 - 40.41%
2026-06-19 06:47:28,780[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-08 10:00:00 (340 days).
2026-06-19 06:47:30,945[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 23303 - after: 32711 - 40.37%
2026-06-19 06:47:30,946[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-08 15:30:00 (340 days).
2026-06-19 06:47:32,920[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 23557 - after: 32965 - 39.94%
2026-06-19 06:47:32,921[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-11 07:00:00 (343 days).
2026-06-19 06:47:34,598[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 23585 - after: 32993 - 39.89%
2026-06-19 06:47:34,600[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-11 14:00:00 (343 days).
2026-06-19 06:47:36,576[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 23649 - after: 33057 - 39.78%
2026-06-19 06:47:36,577[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-12 06:00:00 (344 days).
2026-06-19 06:47:38,139[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 23870 - after: 33470 - 40.22%
2026-06-19 06:47:38,140[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-16 13:15:00 (348 days).
2026-06-19 06:47:39,985[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 24075 - after: 33675 - 39.88%
2026-06-19 06:47:39,986[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-18 16:30:00 (350 days).
2026-06-19 06:47:41,689[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 24079 - after: 33679 - 39.87%
2026-06-19 06:47:41,690[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-18 17:30:00 (350 days).
2026-06-19 06:47:43,532[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 24203 - after: 33995 - 40.46%
2026-06-19 06:47:43,533[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-22 00:30:00 (354 days).
2026-06-19 06:47:45,319[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 24257 - after: 34049 - 40.37%
2026-06-19 06:47:45,320[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-22 14:00:00 (354 days).
2026-06-19 06:47:47,516[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 24415 - after: 34207 - 40.11%
2026-06-19 06:47:47,518[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-24 05:30:00 (356 days).
2026-06-19 06:47:50,310[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 24516 - after: 34312 - 39.96%
2026-06-19 06:47:50,311[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-25 07:45:00 (357 days).
2026-06-19 06:47:52,251[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 24652 - after: 34696 - 40.74%
2026-06-19 06:47:52,252[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-29 07:45:00 (361 days).
2026-06-19 06:47:54,296[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 24780 - after: 34824 - 40.53%
2026-06-19 06:47:54,297[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-30 15:45:00 (362 days).
2026-06-19 06:47:57,693[38;5;243m - [0m[38;5;177mfreqtrade.loggers.set_log_levels[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mRestoring log verbosity.
2026-06-19 06:47:57,693[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMA_Pullback_Strategy: no bias detected
2026-06-19 06:47:57,693[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mChecking look ahead bias via backtests of MA_Pullback_Strategy.py took 163 seconds.

```


**رمز الخروج:** 0
