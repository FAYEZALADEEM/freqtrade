# ملخص باكتيست: LIB_STR007

**التاريخ:** 2026-06-19 04:52
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR007 --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                               BACKTESTING REPORT                                               [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m   Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     59 │         0.23 │          13.289 │         1.33 │ 6 days, 3:37:00 │   36     0    23  61.0 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │        -0.26 │          -0.258 │        -0.03 │ 15 days, 8:45:00 │    0     0     1     0 │
┃[1m [0m[1m  Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m   Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │      59 │         0.23 │          13.289 │         1.33 │ 6 days, 3:37:00 │   36     0    23  61.0 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    59 │         0.23 │          13.289 │         1.33 │  6 days, 3:37:00 │   36     0    23  61.0 │
┃[1m [0m[1m  Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │             │     59 │         0.23 │          13.289 │         1.33 │  6 days, 3:37:00 │   36     0    23  61.0 │
│ Total/Daily Avg Trades                 │ 59 / 0.16                                 │
│ Profit factor                          │ 1.59                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 01:30 / 34d 00:00 / 5d 21:50           │
│ Max Consecutive Wins / Loss            │ 6 / 3                                     │
│ Drawdown duration                      │ 21 days 05:00:00                          │
│ Profit at drawdown start               │ 10.544 USDT                               │
│ Profit at drawdown end                 │ 7.547 USDT                                │
│ Drawdown start                         │ 2025-04-21 02:15:00                       │
│ Drawdown end                           │ 2025-05-12 07:15:00                       │
│ Drawdown duration                      │ 21 days 09:15:00                          │
│ Profit at drawdown start               │ 11.018 USDT                               │
│ Profit at drawdown end                 │ 7.211 USDT                                │
│ Drawdown start                         │ 2025-04-21 09:15:00                       │
│ Drawdown end                           │ 2025-05-12 18:30:00                       │
┃[1m [0m[1m  Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m   Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/LIB_STR007_20260619_045244.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
