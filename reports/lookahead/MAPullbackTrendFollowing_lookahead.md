# تقرير Lookahead Analysis: MAPullbackTrendFollowing

**التاريخ:** 2026-06-19 06:47
**الأمر:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade lookahead-analysis --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --config <(echo '{"entry_pricing": {"price_side": "other"}, "exit_pricing": {"price_side": "other"}}') --strategy MAPullbackTrendFollowing --timeframe 15m --timerange 20250101-20260101 --fee 0 --targeted-trade-amount 100 -p EUR/USDT
```

## قاعدة التحقق المطبقة

- `targeted_trade_amount = 100` (ثابت حسب القاعدة الدائمة)
- يتم فحص حتى 100 إشارة. إذا كان عدد الإشارات أقل، يتم التوضيح.

## النتائج

```
[3m                                                                  Lookahead Analysis                                                                  [0m
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃[1m [0m[1m                   filename[0m[1m [0m┃[1m [0m[1m                strategy[0m[1m [0m┃[1m [0m[1mhas_bias[0m[1m [0m┃[1m [0m[1mtotal_signals[0m[1m [0m┃[1m [0m[1mbiased_entry_signals[0m[1m [0m┃[1m [0m[1mbiased_exit_signals[0m[1m [0m┃[1m [0m[1mbiased_indicators[0m[1m [0m┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ MAPullbackTrendFollowing.py │ MAPullbackTrendFollowing │ [1;32m      No[0m │            42 │                    0 │                   0 │                   │
└─────────────────────────────┴──────────────────────────┴──────────┴───────────────┴──────────────────────┴─────────────────────┴───────────────────┘

2026-06-19 06:46:07,859 - freqtrade - INFO - freqtrade 2026.6-dev-a29762684
2026-06-19 06:46:08,099 - numexpr.utils - INFO - NumExpr defaulting to 8 threads.
2026-06-19 06:46:09,126 - freqtrade.configuration.load_config - INFO - Using config: user_data/config.json ...
2026-06-19 06:46:09,127 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/63 ...
2026-06-19 06:46:09,127 - freqtrade.configuration.load_config - INFO - Using config: /dev/fd/62 ...
2026-06-19 06:46:09,129 - freqtrade.loggers - INFO - Enabling colorized output.
2026-06-19 06:46:09,130[38;5;243m - [0m[38;5;177mfreqtrade.loggers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLogfile configured
2026-06-19 06:46:09,130[38;5;243m - [0m[38;5;177mfreqtrade.loggers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mVerbosity set to 0
2026-06-19 06:46:09,130[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter -i/--timeframe detected ... Using timeframe: 15m ...
2026-06-19 06:46:09,131[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter --fee detected, setting fee to: 0.0 ...
2026-06-19 06:46:09,131[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mParameter --timerange detected: 20250101-20260101 ...
2026-06-19 06:46:09,131[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing user-data directory: /home/fayez/freqtrade/user_data ...
2026-06-19 06:46:09,132[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing data directory: /home/fayez/freqtrade/user_data/data/binance ...
2026-06-19 06:46:09,132[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing pairs ['EUR/USDT']
2026-06-19 06:46:09,132[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mFilter trades by timerange: 20250101-20260101
2026-06-19 06:46:09,133[38;5;243m - [0m[38;5;177mfreqtrade.configuration.configuration[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mTargeted Trade amount: 100
2026-06-19 06:46:09,133[38;5;243m - [0m[38;5;177mfreqtrade.exchange.check_exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mChecking exchange...
2026-06-19 06:46:09,139[38;5;243m - [0m[38;5;177mfreqtrade.exchange.check_exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mExchange "binance" is officially supported by the Freqtrade development team.
2026-06-19 06:46:09,140[38;5;243m - [0m[38;5;177mfreqtrade.configuration.config_validation[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mValidating configuration ...
2026-06-19 06:46:09,142[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mForced order_types to market orders.
2026-06-19 06:46:09,143[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mForced max_open_trades to -1 (same amount as there are pairs)
2026-06-19 06:46:09,143[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mDry run wallet was not set to 1 billion, pushing it up there just to avoid false positives
2026-06-19 06:46:09,143[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mfixing stake_amount to 10k
2026-06-19 06:46:09,154[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR072.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR072.py, line 34)'
2026-06-19 06:46:09,154[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR069.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR069.py, line 34)'
2026-06-19 06:46:09,159[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR061.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR061.py, line 34)'
2026-06-19 06:46:09,160[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR062.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR062.py, line 34)'
2026-06-19 06:46:09,162[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR060.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR060.py, line 34)'
2026-06-19 06:46:09,164[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR074.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR074.py, line 34)'
2026-06-19 06:46:09,165[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR068.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR068.py, line 34)'
2026-06-19 06:46:09,169[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR073.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR073.py, line 34)'
2026-06-19 06:46:09,174[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR071.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR071.py, line 34)'
2026-06-19 06:46:09,179[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[33mWARNING[0m[38;5;243m - [0mCould not import /home/fayez/freqtrade/user_data/strategies/LIB_STR065.py due to 'unterminated triple-quoted string literal 
(detected at line 37) (LIB_STR065.py, line 34)'
2026-06-19 06:46:09,179[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mBias test of MAPullbackTrendFollowing.py started.
2026-06-19 06:46:09,181[38;5;243m - [0m[38;5;177mfreqtrade.exchange.exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mInstance is running with dry_run enabled
2026-06-19 06:46:09,181[38;5;243m - [0m[38;5;177mfreqtrade.exchange.exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing CCXT 4.5.58
2026-06-19 06:46:09,194[38;5;243m - [0m[38;5;177mfreqtrade.exchange.exchange[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing Exchange "Binance"
2026-06-19 06:46:10,789[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.exchange_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing resolved exchange 'Binance'...
2026-06-19 06:46:10,795[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing resolved strategy MAPullbackTrendFollowing from '/home/fayez/freqtrade/user_data/strategies/MAPullbackTrendFollowing.py'...
2026-06-19 06:46:10,796[38;5;243m - [0m[38;5;177mfreqtrade.strategy.hyper[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mFound no parameter file.
2026-06-19 06:46:10,796[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'timeframe' with value from the configuration: 15m.
2026-06-19 06:46:10,797[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'order_types' with value from the configuration: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 
'stoploss_on_exchange': False}.
2026-06-19 06:46:10,797[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'stake_currency' with value from the configuration: USDT.
2026-06-19 06:46:10,798[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'stake_amount' with value from the configuration: 10000.
2026-06-19 06:46:10,798[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'unfilledtimeout' with value from the configuration: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 
'unit': 'minutes'}.
2026-06-19 06:46:10,798[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOverride strategy 'max_open_trades' with value from the configuration: -1.
2026-06-19 06:46:10,799[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using minimal_roi: {'0': 0.01}
2026-06-19 06:46:10,799[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using timeframe: 15m
2026-06-19 06:46:10,800[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using stoploss: -0.01
2026-06-19 06:46:10,800[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using trailing_stop: False
2026-06-19 06:46:10,800[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using trailing_stop_positive_offset: 0.0
2026-06-19 06:46:10,801[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using trailing_only_offset_is_reached: False
2026-06-19 06:46:10,801[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using use_custom_stoploss: False
2026-06-19 06:46:10,801[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using process_only_new_candles: True
2026-06-19 06:46:10,802[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using order_types: {'entry': 'market', 'exit': 'market', 'stoploss': 'market', 'stoploss_on_exchange': False}
2026-06-19 06:46:10,802[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using order_time_in_force: {'entry': 'GTC', 'exit': 'GTC'}
2026-06-19 06:46:10,802[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using stake_currency: USDT
2026-06-19 06:46:10,803[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using stake_amount: 10000
2026-06-19 06:46:10,803[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using startup_candle_count: 0
2026-06-19 06:46:10,803[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using unfilledtimeout: {'entry': 10, 'exit': 10, 'exit_timeout_count': 0, 'unit': 'minutes'}
2026-06-19 06:46:10,804[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using use_exit_signal: True
2026-06-19 06:46:10,804[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using exit_profit_only: False
2026-06-19 06:46:10,804[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using ignore_roi_if_entry_signal: False
2026-06-19 06:46:10,805[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using exit_profit_offset: 0.0
2026-06-19 06:46:10,805[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using disable_dataframe_checks: False
2026-06-19 06:46:10,805[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using ignore_buying_expired_candle_after: 0
2026-06-19 06:46:10,806[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using position_adjustment_enable: False
2026-06-19 06:46:10,806[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using max_entry_position_adjustment: -1
2026-06-19 06:46:10,806[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.strategy_resolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mStrategy using max_open_trades: -1
2026-06-19 06:46:10,807[38;5;243m - [0m[38;5;177mfreqtrade.configuration.config_validation[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mValidating configuration ...
2026-06-19 06:46:10,813[38;5;243m - [0m[38;5;177mfreqtrade.resolvers.iresolver[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing resolved pairlist StaticPairList from '/home/fayez/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2026-06-19 06:46:10,836[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mUsing fee 0.0000% from config.
2026-06-19 06:46:10,890[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 24900 - after: 34944 - 40.34%
2026-06-19 06:46:10,891[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-31 21:45:00 (363 days).
2026-06-19 06:46:12,619[38;5;243m - [0m[38;5;177mfreqtrade.loggers.set_log_levels[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mReducing verbosity for bias tester.
2026-06-19 06:46:12,620[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mOnly found 44 trades. Calculating all available trades.
2026-06-19 06:46:12,686[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 227 - after: 419 - 84.58%
2026-06-19 06:46:12,687[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-06 06:30:00 (4 days).
2026-06-19 06:46:12,789[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 247 - after: 439 - 77.73%
2026-06-19 06:46:12,790[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-06 11:30:00 (4 days).
2026-06-19 06:46:12,931[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 828 - after: 1212 - 46.38%
2026-06-19 06:46:12,932[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-14 12:45:00 (12 days).
2026-06-19 06:46:13,039[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 1216 - after: 1792 - 47.37%
2026-06-19 06:46:13,040[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-20 13:45:00 (18 days).
2026-06-19 06:46:13,216[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 1275 - after: 1851 - 45.18%
2026-06-19 06:46:13,217[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-21 04:30:00 (19 days).
2026-06-19 06:46:13,388[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 1581 - after: 2157 - 36.43%
2026-06-19 06:46:13,389[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-24 09:00:00 (22 days).
2026-06-19 06:46:13,660[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 1601 - after: 2177 - 35.98%
2026-06-19 06:46:13,660[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-24 14:00:00 (22 days).
2026-06-19 06:46:13,815[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 2062 - after: 2830 - 37.25%
2026-06-19 06:46:13,815[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-01-31 09:15:00 (29 days).
2026-06-19 06:46:14,047[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 2392 - after: 3352 - 40.13%
2026-06-19 06:46:14,047[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-05 19:45:00 (34 days).
2026-06-19 06:46:14,241[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 2575 - after: 3535 - 37.28%
2026-06-19 06:46:14,242[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-07 17:30:00 (36 days).
2026-06-19 06:46:14,483[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 2927 - after: 4079 - 39.36%
2026-06-19 06:46:14,484[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-13 09:30:00 (42 days).
2026-06-19 06:46:14,730[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 3570 - after: 5106 - 43.03%
2026-06-19 06:46:14,731[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-24 02:15:00 (53 days).
2026-06-19 06:46:15,046[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 3632 - after: 5168 - 42.29%
2026-06-19 06:46:15,047[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-24 17:45:00 (53 days).
2026-06-19 06:46:15,511[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4019 - after: 5555 - 38.22%
2026-06-19 06:46:15,512[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-02-28 18:30:00 (57 days).
2026-06-19 06:46:15,947[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4072 - after: 5800 - 42.44%
2026-06-19 06:46:15,948[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-03 07:45:00 (60 days).
2026-06-19 06:46:16,313[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4171 - after: 5899 - 41.43%
2026-06-19 06:46:16,314[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-04 08:30:00 (61 days).
2026-06-19 06:46:16,643[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4201 - after: 5929 - 41.13%
2026-06-19 06:46:16,644[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-04 16:00:00 (61 days).
2026-06-19 06:46:16,940[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4223 - after: 5951 - 40.92%
2026-06-19 06:46:16,942[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-04 21:30:00 (61 days).
2026-06-19 06:46:17,300[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4369 - after: 6097 - 39.55%
2026-06-19 06:46:17,301[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-06 10:00:00 (63 days).
2026-06-19 06:46:17,725[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4653 - after: 6569 - 41.18%
2026-06-19 06:46:17,726[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-11 08:00:00 (68 days).
2026-06-19 06:46:18,101[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 4705 - after: 6621 - 40.72%
2026-06-19 06:46:18,102[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-11 21:00:00 (68 days).
2026-06-19 06:46:18,562[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 5453 - after: 7561 - 38.66%
2026-06-19 06:46:18,563[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-21 16:00:00 (78 days).
2026-06-19 06:46:19,138[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 5505 - after: 7805 - 41.78%
2026-06-19 06:46:19,138[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-03-24 05:00:00 (81 days).
2026-06-19 06:46:19,752[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6275 - after: 8767 - 39.71%
2026-06-19 06:46:19,753[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-03 05:30:00 (91 days).
2026-06-19 06:46:20,497[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6328 - after: 8820 - 39.38%
2026-06-19 06:46:20,498[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-03 18:45:00 (91 days).
2026-06-19 06:46:21,186[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6434 - after: 9118 - 41.72%
2026-06-19 06:46:21,188[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-06 21:15:00 (94 days).
2026-06-19 06:46:21,977[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6450 - after: 9134 - 41.61%
2026-06-19 06:46:21,979[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-07 01:15:00 (95 days).
2026-06-19 06:46:22,733[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6665 - after: 9349 - 40.27%
2026-06-19 06:46:22,734[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-09 07:00:00 (97 days).
2026-06-19 06:46:23,581[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6672 - after: 9356 - 40.23%
2026-06-19 06:46:23,582[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-09 08:45:00 (97 days).
2026-06-19 06:46:24,373[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6784 - after: 9468 - 39.56%
2026-06-19 06:46:24,375[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-10 12:45:00 (98 days).
2026-06-19 06:46:24,991[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6857 - after: 9541 - 39.14%
2026-06-19 06:46:24,991[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-11 07:00:00 (99 days).
2026-06-19 06:46:25,777[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6862 - after: 9546 - 39.11%
2026-06-19 06:46:25,778[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-11 08:15:00 (99 days).
2026-06-19 06:46:26,563[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 6948 - after: 9824 - 41.39%
2026-06-19 06:46:26,564[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-14 05:45:00 (102 days).
2026-06-19 06:46:27,385[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 7415 - after: 10483 - 41.38%
2026-06-19 06:46:27,386[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-21 02:30:00 (109 days).
2026-06-19 06:46:28,316[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 7461 - after: 10529 - 41.12%
2026-06-19 06:46:28,318[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-21 14:00:00 (109 days).
2026-06-19 06:46:29,208[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 7588 - after: 10656 - 40.43%
2026-06-19 06:46:29,210[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-22 21:45:00 (110 days).
2026-06-19 06:46:30,059[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 7987 - after: 11247 - 40.82%
2026-06-19 06:46:30,060[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-04-29 01:30:00 (117 days).
2026-06-19 06:46:30,829[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8195 - after: 11455 - 39.78%
2026-06-19 06:46:30,830[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-01 05:30:00 (119 days).
2026-06-19 06:46:31,681[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8335 - after: 11595 - 39.11%
2026-06-19 06:46:31,682[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-02 16:30:00 (120 days).
2026-06-19 06:46:32,255[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 8719 - after: 12171 - 39.59%
2026-06-19 06:46:32,256[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-08 16:30:00 (126 days).
2026-06-19 06:46:32,904[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 9068 - after: 12712 - 40.19%
2026-06-19 06:46:32,905[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-14 07:45:00 (132 days).
2026-06-19 06:46:33,566[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 9526 - after: 13362 - 40.27%
2026-06-19 06:46:33,567[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-21 02:15:00 (139 days).
2026-06-19 06:46:34,303[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 9568 - after: 13404 - 40.09%
2026-06-19 06:46:34,304[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-05-21 12:45:00 (139 days).
2026-06-19 06:46:35,071[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 10317 - after: 14537 - 40.90%
2026-06-19 06:46:35,073[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-02 08:00:00 (151 days).
2026-06-19 06:46:36,223[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 10389 - after: 14609 - 40.62%
2026-06-19 06:46:36,224[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-03 02:00:00 (152 days).
2026-06-19 06:46:37,310[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 11090 - after: 15502 - 39.78%
2026-06-19 06:46:37,311[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-12 09:15:00 (161 days).
2026-06-19 06:46:38,482[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 11152 - after: 15564 - 39.56%
2026-06-19 06:46:38,483[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-13 00:45:00 (162 days).
2026-06-19 06:46:39,772[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 11514 - after: 16118 - 39.99%
2026-06-19 06:46:39,773[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-18 19:15:00 (167 days).
2026-06-19 06:46:40,685[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 11678 - after: 16282 - 39.42%
2026-06-19 06:46:40,689[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-20 12:15:00 (169 days).
2026-06-19 06:46:41,573[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 11879 - after: 16675 - 40.37%
2026-06-19 06:46:41,573[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-24 14:30:00 (173 days).
2026-06-19 06:46:42,820[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 11904 - after: 16700 - 40.29%
2026-06-19 06:46:42,821[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-24 20:45:00 (173 days).
2026-06-19 06:46:43,645[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 12046 - after: 16842 - 39.81%
2026-06-19 06:46:43,646[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-26 08:15:00 (175 days).
2026-06-19 06:46:44,503[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 12063 - after: 16859 - 39.76%
2026-06-19 06:46:44,504[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-06-26 12:30:00 (175 days).
2026-06-19 06:46:45,527[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 12337 - after: 17325 - 40.43%
2026-06-19 06:46:45,528[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-01 09:00:00 (180 days).
2026-06-19 06:46:47,038[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 12357 - after: 17345 - 40.37%
2026-06-19 06:46:47,040[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-01 14:00:00 (180 days).
2026-06-19 06:46:47,983[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 13030 - after: 18210 - 39.75%
2026-06-19 06:46:47,984[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-10 14:15:00 (189 days).
2026-06-19 06:46:48,950[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 13218 - after: 18590 - 40.64%
2026-06-19 06:46:48,951[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-14 13:15:00 (193 days).
2026-06-19 06:46:49,915[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 13413 - after: 18785 - 40.05%
2026-06-19 06:46:49,916[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-16 14:00:00 (195 days).
2026-06-19 06:46:51,059[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 13573 - after: 18945 - 39.58%
2026-06-19 06:46:51,060[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-18 06:00:00 (197 days).
2026-06-19 06:46:52,677[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 13803 - after: 19367 - 40.31%
2026-06-19 06:46:52,678[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-22 15:30:00 (201 days).
2026-06-19 06:46:54,371[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 13840 - after: 19404 - 40.20%
2026-06-19 06:46:54,372[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-23 00:45:00 (202 days).
2026-06-19 06:46:55,310[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 14187 - after: 19943 - 40.57%
2026-06-19 06:46:55,311[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-07-28 15:30:00 (207 days).
2026-06-19 06:46:56,485[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 14619 - after: 20567 - 40.69%
2026-06-19 06:46:56,486[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-04 03:30:00 (214 days).
2026-06-19 06:46:57,826[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 15306 - after: 21446 - 40.11%
2026-06-19 06:46:57,827[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-13 07:15:00 (223 days).
2026-06-19 06:46:59,122[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 15332 - after: 21472 - 40.05%
2026-06-19 06:46:59,123[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-13 13:45:00 (223 days).
2026-06-19 06:47:00,256[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 15967 - after: 22299 - 39.66%
2026-06-19 06:47:00,257[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-22 04:30:00 (232 days).
2026-06-19 06:47:02,084[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 16101 - after: 22625 - 40.52%
2026-06-19 06:47:02,085[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-25 14:00:00 (235 days).
2026-06-19 06:47:03,243[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 16271 - after: 22795 - 40.10%
2026-06-19 06:47:03,244[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-27 08:30:00 (237 days).
2026-06-19 06:47:04,519[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 16361 - after: 22885 - 39.88%
2026-06-19 06:47:04,520[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-08-28 07:00:00 (238 days).
2026-06-19 06:47:05,650[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 16966 - after: 23682 - 39.59%
2026-06-19 06:47:05,651[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-05 14:15:00 (246 days).
2026-06-19 06:47:06,901[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 16990 - after: 23706 - 39.53%
2026-06-19 06:47:06,902[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-05 20:15:00 (246 days).
2026-06-19 06:47:08,536[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 17638 - after: 24738 - 40.25%
2026-06-19 06:47:08,537[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-16 14:15:00 (257 days).
2026-06-19 06:47:10,025[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 17735 - after: 24835 - 40.03%
2026-06-19 06:47:10,026[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-17 14:30:00 (258 days).
2026-06-19 06:47:11,435[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 17919 - after: 25019 - 39.62%
2026-06-19 06:47:11,439[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-19 12:30:00 (260 days).
2026-06-19 06:47:13,103[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 18083 - after: 25375 - 40.33%
2026-06-19 06:47:13,105[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-23 05:30:00 (264 days).
2026-06-19 06:47:14,842[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 18310 - after: 25602 - 39.83%
2026-06-19 06:47:14,843[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-25 14:15:00 (266 days).
2026-06-19 06:47:16,393[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 18475 - after: 25959 - 40.51%
2026-06-19 06:47:16,394[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-09-29 07:30:00 (270 days).
2026-06-19 06:47:18,504[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 19138 - after: 26814 - 40.11%
2026-06-19 06:47:18,506[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-10-08 05:15:00 (279 days).
2026-06-19 06:47:20,759[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 19431 - after: 27299 - 40.49%
2026-06-19 06:47:20,760[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-10-13 06:30:00 (284 days).
2026-06-19 06:47:22,357[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 20895 - after: 29343 - 40.43%
2026-06-19 06:47:22,358[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-11-03 13:30:00 (305 days).
2026-06-19 06:47:24,541[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 21229 - after: 29677 - 39.79%
2026-06-19 06:47:24,542[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-11-07 01:00:00 (309 days).
2026-06-19 06:47:26,178[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 22995 - after: 32211 - 40.08%
2026-06-19 06:47:26,179[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-03 10:30:00 (335 days).
2026-06-19 06:47:27,930[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 23055 - after: 32271 - 39.97%
2026-06-19 06:47:27,930[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-04 01:30:00 (336 days).
2026-06-19 06:47:29,703[38;5;243m - [0m[38;5;177mfreqtrade.data.converter.converter[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMissing data fillup for EUR/USDT, 15m: before: 23872 - after: 33472 - 40.21%
2026-06-19 06:47:29,705[38;5;243m - [0m[38;5;177mfreqtrade.optimize.backtesting[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mLoading data from 2025-01-01 22:00:00 up to 2025-12-16 13:45:00 (348 days).
2026-06-19 06:47:31,503[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mfound force-exit in pair: EUR/USDT, timerange:2025-12-16 17:00:00+00:00-2025-12-31 21:45:00+00:00, idx: 42, skipping this one 
to avoid a false-positive.
2026-06-19 06:47:31,503[38;5;243m - [0m[38;5;177mfreqtrade.loggers.set_log_levels[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mRestoring log verbosity.
2026-06-19 06:47:31,503[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mMAPullbackTrendFollowing: no bias detected
2026-06-19 06:47:31,504[38;5;243m - [0m[38;5;177mfreqtrade.optimize.analysis.lookahead_helpers[0m[38;5;243m - [0m[34mINFO[0m[38;5;243m - [0mChecking look ahead bias via backtests of MAPullbackTrendFollowing.py took 82 seconds.

```


**رمز الخروج:** 0
