# ملخص باكتيست: CRT_1AM

**التاريخ:** 2026-06-19 04:05
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy CRT_1AM --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                             BACKTESTING REPORT                                              [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     93 │        -0.01 │          -1.024 │         -0.1 │     10:05:00 │   45     0    48  48.4 │
┃[1m [0m[1m Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
┃[1m [0m[1m   Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│        TOTAL │      93 │        -0.01 │          -1.024 │         -0.1 │     10:05:00 │   45     0    48  48.4 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    93 │        -0.01 │          -1.024 │         -0.1 │     10:05:00 │   45     0    48  48.4 │
┃[1m [0m[1m   Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│        TOTAL │             │     93 │        -0.01 │          -1.024 │         -0.1 │     10:05:00 │   45     0    48  48.4 │
│ Total/Daily Avg Trades                 │ 93 / 0.26                                 │
│ Profit factor                          │ 0.91                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 00:30 / 2d 04:45 / 0d 07:03            │
│ Max Consecutive Wins / Loss            │ 4 / 4                                     │
│ Drawdown duration                      │ 75 days 21:30:00                          │
│ Profit at drawdown start               │ 0.639 USDT                                │
│ Profit at drawdown end                 │ -1.214 USDT                               │
│ Drawdown start                         │ 2025-09-23 17:45:00                       │
│ Drawdown end                           │ 2025-12-08 15:15:00                       │
│ Drawdown duration                      │ 63 days 07:00:00                          │
│ Profit at drawdown start               │ 0.664 USDT                                │
│ Profit at drawdown end                 │ -1.391 USDT                               │
│ Drawdown start                         │ 2025-10-07 08:15:00                       │
│ Drawdown end                           │ 2025-12-09 15:15:00                       │
┃[1m [0m[1mStrategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/CRT_1AM_20260619_040557.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
