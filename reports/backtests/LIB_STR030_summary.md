# ملخص باكتيست: LIB_STR030

**التاريخ:** 2026-06-19 06:38
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR030 --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                               BACKTESTING REPORT                                                [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     60 │          0.2 │          11.984 │          1.2 │ 5 days, 16:42:00 │   36     0    24  60.0 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │        -0.26 │          -0.258 │        -0.03 │ 15 days, 8:45:00 │    0     0     1     0 │
┃[1m [0m[1m  Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │      60 │          0.2 │          11.984 │          1.2 │ 5 days, 16:42:00 │   36     0    24  60.0 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    60 │          0.2 │          11.984 │          1.2 │ 5 days, 16:42:00 │   36     0    24  60.0 │
┃[1m [0m[1m  Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │             │     60 │          0.2 │          11.984 │          1.2 │ 5 days, 16:42:00 │   36     0    24  60.0 │
│ Total/Daily Avg Trades                 │ 60 / 0.17                                 │
│ Profit factor                          │ 1.50                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 03:00 / 33d 03:00 / 5d 21:38           │
│ Max Consecutive Wins / Loss            │ 6 / 3                                     │
│ Drawdown duration                      │ 30 days 00:30:00                          │
│ Profit at drawdown start               │ 13.24 USDT                                │
│ Profit at drawdown end                 │ 10.241 USDT                               │
│ Drawdown start                         │ 2025-06-30 18:15:00                       │
│ Drawdown end                           │ 2025-07-30 18:45:00                       │
│ Drawdown duration                      │ 127 days 04:15:00                         │
│ Profit at drawdown start               │ 13.606 USDT                               │
│ Profit at drawdown end                 │ 9.664 USDT                                │
│ Drawdown start                         │ 2025-07-01 09:45:00                       │
│ Drawdown end                           │ 2025-11-05 14:00:00                       │
┃[1m [0m[1m  Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/LIB_STR030_20260619_063803.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
