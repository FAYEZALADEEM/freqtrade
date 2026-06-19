# ملخص باكتيست: LIB_STR013

**التاريخ:** 2026-06-19 06:34
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR013 --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                               BACKTESTING REPORT                                               [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m   Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     67 │         0.19 │          12.980 │          1.3 │ 5 days, 7:41:00 │   40     0    27  59.7 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │        -0.14 │          -0.140 │        -0.01 │ 16 days, 6:30:00 │    0     0     1     0 │
┃[1m [0m[1m  Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m   Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │      67 │         0.19 │          12.980 │          1.3 │ 5 days, 7:41:00 │   40     0    27  59.7 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    67 │         0.19 │          12.980 │          1.3 │  5 days, 7:41:00 │   40     0    27  59.7 │
┃[1m [0m[1m  Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │             │     67 │         0.19 │          12.980 │          1.3 │  5 days, 7:41:00 │   40     0    27  59.7 │
│ Total/Daily Avg Trades                 │ 67 / 0.18                                 │
│ Profit factor                          │ 1.48                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 03:15 / 15d 11:00 / 4d 15:51           │
│ Max Consecutive Wins / Loss            │ 5 / 3                                     │
│ Drawdown duration                      │ 20 days 23:30:00                          │
│ Profit at drawdown start               │ 10.115 USDT                               │
│ Profit at drawdown end                 │ 7.117 USDT                                │
│ Drawdown start                         │ 2025-04-21 07:45:00                       │
│ Drawdown end                           │ 2025-05-12 07:15:00                       │
│ Drawdown duration                      │ 21 days 09:15:00                          │
│ Profit at drawdown start               │ 10.219 USDT                               │
│ Profit at drawdown end                 │ 6.491 USDT                                │
│ Drawdown start                         │ 2025-04-21 09:15:00                       │
│ Drawdown end                           │ 2025-05-12 18:30:00                       │
┃[1m [0m[1m  Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m   Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/LIB_STR013_20260619_063452.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
