# ملخص باكتيست: LIB_STR012_BBMA

**التاريخ:** 2026-06-19 06:34
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR012_BBMA --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                               BACKTESTING REPORT                                                [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     52 │         0.19 │           9.800 │         0.98 │ 6 days, 12:05:00 │   31     0    21  59.6 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │         -0.1 │          -0.100 │        -0.01 │ 20 days, 4:30:00 │    0     0     1     0 │
┃[1m [0m[1m      Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│           TOTAL │      52 │         0.19 │           9.800 │         0.98 │ 6 days, 12:05:00 │   31     0    21  59.6 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    52 │         0.19 │           9.800 │         0.98 │ 6 days, 12:05:00 │   31     0    21  59.6 │
┃[1m [0m[1m      Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│           TOTAL │             │     52 │         0.19 │           9.800 │         0.98 │ 6 days, 12:05:00 │   31     0    21  59.6 │
│ Total/Daily Avg Trades                 │ 52 / 0.14                                 │
│ Profit factor                          │ 1.46                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 02:30 / 40d 00:00 / 6d 04:55           │
│ Max Consecutive Wins / Loss            │ 5 / 4                                     │
│ Drawdown duration                      │ 25 days 14:45:00                          │
│ Profit at drawdown start               │ 8.898 USDT                                │
│ Profit at drawdown end                 │ 4.902 USDT                                │
│ Drawdown start                         │ 2025-04-21 00:30:00                       │
│ Drawdown end                           │ 2025-05-16 15:15:00                       │
│ Drawdown duration                      │ 22 days 01:00:00                          │
│ Profit at drawdown start               │ 9.82 USDT                                 │
│ Profit at drawdown end                 │ 4.785 USDT                                │
│ Drawdown start                         │ 2025-04-21 09:15:00                       │
│ Drawdown end                           │ 2025-05-13 10:15:00                       │
┃[1m [0m[1m       Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/LIB_STR012_BBMA_20260619_063420.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
