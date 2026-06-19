# ملخص باكتيست: SMC_OrderBlock_BOS

**التاريخ:** 2026-06-19 03:33
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy SMC_OrderBlock_BOS --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                             BACKTESTING REPORT                                              [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │    517 │          0.0 │           0.957 │          0.1 │      3:21:00 │  249   125   143  48.2 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │         0.03 │           0.032 │          0.0 │      1:30:00 │    1     0     0   100 │
┃[1m [0m[1m   Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│        TOTAL │     517 │          0.0 │           0.957 │          0.1 │      3:21:00 │  249   125   143  48.2 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │   517 │          0.0 │           0.957 │          0.1 │      3:21:00 │  249   125   143  48.2 │
┃[1m [0m[1m   Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│        TOTAL │             │    517 │          0.0 │           0.957 │          0.1 │      3:21:00 │  249   125   143  48.2 │
│ Total/Daily Avg Trades                 │ 517 / 1.42                                │
│ Profit factor                          │ 1.03                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 00:15 / 2d 02:00 / 0d 02:08            │
│ Max Consecutive Wins / Loss            │ 7 / 8                                     │
│ Drawdown duration                      │ 90 days 20:00:00                          │
│ Profit at drawdown start               │ 2.764 USDT                                │
│ Profit at drawdown end                 │ -0.123 USDT                               │
│ Drawdown start                         │ 2025-08-22 14:15:00                       │
│ Drawdown end                           │ 2025-11-21 10:15:00                       │
│ Drawdown duration                      │ 91 days 01:15:00                          │
│ Profit at drawdown start               │ 2.824 USDT                                │
│ Profit at drawdown end                 │ -0.15 USDT                                │
│ Drawdown start                         │ 2025-08-25 06:45:00                       │
│ Drawdown end                           │ 2025-11-24 08:00:00                       │
┃[1m [0m[1m          Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/SMC_OrderBlock_BOS_20260619_033318.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
