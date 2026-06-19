# ملخص باكتيست: LIB_STR005

**التاريخ:** 2026-06-19 04:40
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR005 --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                               BACKTESTING REPORT                                               [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m   Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     56 │         0.21 │          11.766 │         1.18 │ 6 days, 1:53:00 │   34     0    22  60.7 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │        -0.26 │          -0.258 │        -0.03 │ 15 days, 8:45:00 │    0     0     1     0 │
┃[1m [0m[1m  Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m   Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │      56 │         0.21 │          11.766 │         1.18 │ 6 days, 1:53:00 │   34     0    22  60.7 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    56 │         0.21 │          11.766 │         1.18 │  6 days, 1:53:00 │   34     0    22  60.7 │
┃[1m [0m[1m  Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │             │     56 │         0.21 │          11.766 │         1.18 │  6 days, 1:53:00 │   34     0    22  60.7 │
│ Total/Daily Avg Trades                 │ 56 / 0.15                                 │
│ Profit factor                          │ 1.53                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 01:15 / 33d 03:00 / 5d 21:23           │
│ Max Consecutive Wins / Loss            │ 6 / 3                                     │
│ Drawdown duration                      │ 30 days 00:30:00                          │
│ Profit at drawdown start               │ 13.022 USDT                               │
│ Profit at drawdown end                 │ 10.024 USDT                               │
│ Drawdown start                         │ 2025-06-30 18:15:00                       │
│ Drawdown end                           │ 2025-07-30 18:45:00                       │
│ Drawdown duration                      │ 127 days 04:15:00                         │
│ Profit at drawdown start               │ 13.389 USDT                               │
│ Profit at drawdown end                 │ 9.52 USDT                                 │
│ Drawdown start                         │ 2025-07-01 09:45:00                       │
│ Drawdown end                           │ 2025-11-05 14:00:00                       │
┃[1m [0m[1m  Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m   Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/LIB_STR005_20260619_044036.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
