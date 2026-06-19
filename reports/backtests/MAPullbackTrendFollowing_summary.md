# ملخص باكتيست: MAPullbackTrendFollowing

**التاريخ:** 2026-06-19 06:46
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy MAPullbackTrendFollowing --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                               BACKTESTING REPORT                                               [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m   Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     43 │         0.13 │           5.521 │         0.55 │ 6 days, 8:59:00 │   24     0    19  55.8 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │        -0.18 │          -0.184 │        -0.02 │ 15 days, 4:45:00 │    0     0     1     0 │
┃[1m [0m[1m   Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m   Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│        TOTAL │      43 │         0.13 │           5.521 │         0.55 │ 6 days, 8:59:00 │   24     0    19  55.8 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    43 │         0.13 │           5.521 │         0.55 │  6 days, 8:59:00 │   24     0    19  55.8 │
┃[1m [0m[1m   Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│        TOTAL │             │     43 │         0.13 │           5.521 │         0.55 │  6 days, 8:59:00 │   24     0    19  55.8 │
│ Total/Daily Avg Trades                 │ 43 / 0.12                                 │
│ Profit factor                          │ 1.30                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 01:15 / 26d 09:30 / 6d 12:28           │
│ Max Consecutive Wins / Loss            │ 4 / 4                                     │
│ Drawdown duration                      │ 125 days 04:30:00                         │
│ Profit at drawdown start               │ 8.699 USDT                                │
│ Profit at drawdown end                 │ 3.707 USDT                                │
│ Drawdown start                         │ 2025-07-01 08:45:00                       │
│ Drawdown end                           │ 2025-11-03 13:15:00                       │
│ Drawdown duration                      │ 141 days 15:15:00                         │
│ Profit at drawdown start               │ 8.78 USDT                                 │
│ Profit at drawdown end                 │ 3.296 USDT                                │
│ Drawdown start                         │ 2025-07-03 01:30:00                       │
│ Drawdown end                           │ 2025-11-21 16:45:00                       │
┃[1m [0m[1m                Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m   Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/MAPullbackTrendFollowing_20260619_064600.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
