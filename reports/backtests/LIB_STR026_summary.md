# ملخص باكتيست: LIB_STR026

**التاريخ:** 2026-06-19 06:35
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR026 --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                               BACKTESTING REPORT                                                [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     54 │          0.2 │          10.764 │         1.08 │ 6 days, 12:54:00 │   33     0    21  61.1 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │         0.41 │           0.414 │         0.04 │ 21 days, 1:30:00 │    1     0     0   100 │
┃[1m [0m[1m  Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │      54 │          0.2 │          10.764 │         1.08 │ 6 days, 12:54:00 │   33     0    21  61.1 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    54 │          0.2 │          10.764 │         1.08 │ 6 days, 12:54:00 │   33     0    21  61.1 │
┃[1m [0m[1m  Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │             │     54 │          0.2 │          10.764 │         1.08 │ 6 days, 12:54:00 │   33     0    21  61.1 │
│ Total/Daily Avg Trades                 │ 54 / 0.15                                 │
│ Profit factor                          │ 1.50                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 03:00 / 40d 13:45 / 7d 04:39           │
│ Max Consecutive Wins / Loss            │ 6 / 4                                     │
│ Drawdown duration                      │ 30 days 00:30:00                          │
│ Profit at drawdown start               │ 12.347 USDT                               │
│ Profit at drawdown end                 │ 8.35 USDT                                 │
│ Drawdown start                         │ 2025-06-30 18:15:00                       │
│ Drawdown end                           │ 2025-07-30 18:45:00                       │
│ Drawdown duration                      │ 31 days 02:45:00                          │
│ Profit at drawdown start               │ 12.714 USDT                               │
│ Profit at drawdown end                 │ 7.791 USDT                                │
│ Drawdown start                         │ 2025-07-01 09:45:00                       │
│ Drawdown end                           │ 2025-08-01 12:30:00                       │
┃[1m [0m[1m  Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/LIB_STR026_20260619_063509.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
