# ملخص باكتيست: VSAConservativeTemplate

**التاريخ:** 2026-06-19 06:51
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy VSAConservativeTemplate --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                                BACKTESTING REPORT                                                [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      9 │         1.34 │          12.015 │          1.2 │ 32 days, 20:15:00 │    6     0     3  66.7 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │         1.52 │           1.522 │         0.15 │ 51 days, 11:30:00 │    1     0     0   100 │
┃[1m [0m[1m         Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│              TOTAL │       9 │         1.34 │          12.015 │          1.2 │ 32 days, 20:15:00 │    6     0     3  66.7 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │     9 │         1.34 │          12.015 │          1.2 │ 32 days, 20:15:00 │    6     0     3  66.7 │
┃[1m [0m[1m         Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│              TOTAL │             │      9 │         1.34 │          12.015 │          1.2 │ 32 days, 20:15:00 │    6     0     3  66.7 │
│ Total/Daily Avg Trades                 │ 9 / 0.02                                  │
│ Profit factor                          │ 3.67                                      │
│ Min/Max/Avg. Duration Winners          │ 6d 20:00 / 60d 07:45 / 30d 08:48          │
│ Max Consecutive Wins / Loss            │ 4 / 2                                     │
│ Drawdown duration                      │ 131 days 13:00:00                         │
│ Profit at drawdown start               │ 13.491 USDT                               │
│ Profit at drawdown end                 │ 10.493 USDT                               │
│ Drawdown start                         │ 2025-06-25 23:30:00                       │
│ Drawdown end                           │ 2025-11-04 12:30:00                       │
│ Drawdown duration                      │ 120 days 02:30:00                         │
│ Profit at drawdown start               │ 14.225 USDT                               │
│ Profit at drawdown end                 │ 9.82 USDT                                 │
│ Drawdown start                         │ 2025-07-24 14:15:00                       │
│ Drawdown end                           │ 2025-11-21 16:45:00                       │
┃[1m [0m[1m               Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/VSAConservativeTemplate_20260619_065114.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
