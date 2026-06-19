# ملخص باكتيست: OneHourForexReversal

**التاريخ:** 2026-06-19 06:47
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy OneHourForexReversal --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                                BACKTESTING REPORT                                                [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      8 │         0.82 │           6.569 │         0.66 │ 34 days, 13:58:00 │    6     0     2  75.0 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │         0.57 │           0.574 │         0.06 │ 97 days, 5:30:00 │    1     0     0   100 │
┃[1m [0m[1m Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│      TOTAL │       8 │         0.82 │           6.569 │         0.66 │ 34 days, 13:58:00 │    6     0     2  75.0 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │     8 │         0.82 │           6.569 │         0.66 │ 34 days, 13:58:00 │    6     0     2  75.0 │
┃[1m [0m[1m Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│      TOTAL │             │      8 │         0.82 │           6.569 │         0.66 │ 34 days, 13:58:00 │    6     0     2  75.0 │
│ Total/Daily Avg Trades                 │ 8 / 0.02                                  │
│ Profit factor                          │ 2.64                                      │
│ Min/Max/Avg. Duration Winners          │ 8d 23:15 / 97d 05:30 / 37d 10:28          │
│ Max Consecutive Wins / Loss            │ 2 / 1                                     │
│ Drawdown duration                      │ 48 days 00:00:00                          │
│ Profit at drawdown start               │ 5.997 USDT                                │
│ Profit at drawdown end                 │ 3.998 USDT                                │
│ Drawdown start                         │ 2025-06-12 12:30:00                       │
│ Drawdown end                           │ 2025-07-30 12:30:00                       │
│ Drawdown duration                      │ 25 days 07:00:00                          │
│ Profit at drawdown start               │ 5.484 USDT                                │
│ Profit at drawdown end                 │ 1.673 USDT                                │
│ Drawdown start                         │ 2025-04-21 09:15:00                       │
│ Drawdown end                           │ 2025-05-16 16:15:00                       │
┃[1m [0m[1m            Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/OneHourForexReversal_20260619_064719.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
