# ملخص باكتيست: LIB_STR006

**التاريخ:** 2026-06-19 04:52
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR006 --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                               BACKTESTING REPORT                                                [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     11 │        -0.02 │          -0.188 │        -0.02 │ 5 days, 15:26:00 │    5     0     6  45.5 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │        -0.19 │          -0.191 │        -0.02 │ 2 days, 23:30:00 │    0     0     1     0 │
┃[1m [0m[1m  Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │      11 │        -0.02 │          -0.188 │        -0.02 │ 5 days, 15:26:00 │    5     0     6  45.5 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    11 │        -0.02 │          -0.188 │        -0.02 │ 5 days, 15:26:00 │    5     0     6  45.5 │
┃[1m [0m[1m  Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │             │     11 │        -0.02 │          -0.188 │        -0.02 │ 5 days, 15:26:00 │    5     0     6  45.5 │
│ Total/Daily Avg Trades                 │ 11 / 0.03                                 │
│ Profit factor                          │ 0.96                                      │
│ Min/Max/Avg. Duration Winners          │ 1d 20:45 / 8d 16:45 / 4d 00:54            │
│ Max Consecutive Wins / Loss            │ 2 / 3                                     │
│ Drawdown duration                      │ 106 days 07:45:00                         │
│ Profit at drawdown start               │ 2.001 USDT                                │
│ Profit at drawdown end                 │ -0.188 USDT                               │
│ Drawdown start                         │ 2025-09-16 14:00:00                       │
│ Drawdown end                           │ 2025-12-31 21:45:00                       │
│ Drawdown duration                      │ 288 days 06:45:00                         │
│ Profit at drawdown start               │ 2.679 USDT                                │
│ Profit at drawdown end                 │ -0.411 USDT                               │
│ Drawdown start                         │ 2025-03-18 08:30:00                       │
│ Drawdown end                           │ 2025-12-31 15:15:00                       │
┃[1m [0m[1m  Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m        Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/LIB_STR006_20260619_045201.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
