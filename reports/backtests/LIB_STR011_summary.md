# ملخص باكتيست: LIB_STR011

**التاريخ:** 2026-06-19 06:28
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR011 --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                               BACKTESTING REPORT                                                [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     54 │         0.16 │           8.772 │         0.88 │ 5 days, 23:03:00 │   32     0    22  59.3 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │         0.09 │           0.095 │         0.01 │ 19 days, 19:30:00 │    1     0     0   100 │
┃[1m [0m[1m  Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │      54 │         0.16 │           8.772 │         0.88 │ 5 days, 23:03:00 │   32     0    22  59.3 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    54 │         0.16 │           8.772 │         0.88 │  5 days, 23:03:00 │   32     0    22  59.3 │
┃[1m [0m[1m  Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │             │     54 │         0.16 │           8.772 │         0.88 │  5 days, 23:03:00 │   32     0    22  59.3 │
│ Total/Daily Avg Trades                 │ 54 / 0.15                                 │
│ Profit factor                          │ 1.39                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 01:15 / 19d 19:30 / 5d 22:34           │
│ Max Consecutive Wins / Loss            │ 4 / 3                                     │
│ Drawdown duration                      │ 21 days 07:45:00                          │
│ Profit at drawdown start               │ 3.673 USDT                                │
│ Profit at drawdown end                 │ 0.677 USDT                                │
│ Drawdown start                         │ 2025-04-20 23:30:00                       │
│ Drawdown end                           │ 2025-05-12 07:15:00                       │
│ Drawdown duration                      │ 20 days 13:00:00                          │
│ Profit at drawdown start               │ 3.952 USDT                                │
│ Profit at drawdown end                 │ 0.341 USDT                                │
│ Drawdown start                         │ 2025-04-22 05:30:00                       │
│ Drawdown end                           │ 2025-05-12 18:30:00                       │
┃[1m [0m[1m  Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/LIB_STR011_20260619_062852.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
