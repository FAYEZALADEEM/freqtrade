# ملخص باكتيست: LIB_STR012

**التاريخ:** 2026-06-19 06:31
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR012 --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                               BACKTESTING REPORT                                                [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     60 │         0.21 │          12.534 │         1.25 │ 5 days, 23:48:00 │   37     0    23  61.7 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │         0.41 │           0.414 │         0.04 │ 21 days, 1:30:00 │    1     0     0   100 │
┃[1m [0m[1m   Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│        TOTAL │      60 │         0.21 │          12.534 │         1.25 │ 5 days, 23:48:00 │   37     0    23  61.7 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    60 │         0.21 │          12.534 │         1.25 │ 5 days, 23:48:00 │   37     0    23  61.7 │
┃[1m [0m[1m   Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│        TOTAL │             │     60 │         0.21 │          12.534 │         1.25 │ 5 days, 23:48:00 │   37     0    23  61.7 │
│ Total/Daily Avg Trades                 │ 60 / 0.17                                 │
│ Profit factor                          │ 1.53                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 03:15 / 40d 23:45 / 5d 14:33           │
│ Max Consecutive Wins / Loss            │ 5 / 3                                     │
│ Drawdown duration                      │ 29 days 04:00:00                          │
│ Profit at drawdown start               │ 13.112 USDT                               │
│ Profit at drawdown end                 │ 10.115 USDT                               │
│ Drawdown start                         │ 2025-07-01 08:45:00                       │
│ Drawdown end                           │ 2025-07-30 12:45:00                       │
│ Drawdown duration                      │ 31 days 02:45:00                          │
│ Profit at drawdown start               │ 13.256 USDT                               │
│ Profit at drawdown end                 │ 9.376 USDT                                │
│ Drawdown start                         │ 2025-07-01 09:45:00                       │
│ Drawdown end                           │ 2025-08-01 12:30:00                       │
┃[1m [0m[1m  Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/LIB_STR012_20260619_063141.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
