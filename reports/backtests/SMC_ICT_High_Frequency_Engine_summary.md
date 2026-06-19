# ملخص باكتيست: SMC_ICT_High_Frequency_Engine

**التاريخ:** 2026-06-19 03:12
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy SMC_ICT_High_Frequency_Engine --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                             BACKTESTING REPORT                                              [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │    298 │        -0.01 │          -1.660 │        -0.17 │     11:09:00 │   97     0   201  32.6 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │         0.04 │           0.042 │          0.0 │     17:45:00 │    1     0     0   100 │
┃[1m [0m[1m      Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│           TOTAL │     298 │        -0.01 │          -1.660 │        -0.17 │     11:09:00 │   97     0   201  32.6 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │   298 │        -0.01 │          -1.660 │        -0.17 │     11:09:00 │   97     0   201  32.6 │
┃[1m [0m[1m      Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│           TOTAL │             │    298 │        -0.01 │          -1.660 │        -0.17 │     11:09:00 │   97     0   201  32.6 │
│ Total/Daily Avg Trades                 │ 298 / 0.82                                │
│ Profit factor                          │ 0.96                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 00:30 / 4d 07:30 / 0d 14:49            │
│ Max Consecutive Wins / Loss            │ 4 / 11                                    │
│ Drawdown duration                      │ 126 days 17:30:00                         │
│ Profit at drawdown start               │ 1.856 USDT                                │
│ Profit at drawdown end                 │ -2.91 USDT                                │
│ Drawdown start                         │ 2025-06-30 18:15:00                       │
│ Drawdown end                           │ 2025-11-04 11:45:00                       │
│ Drawdown duration                      │ 127 days 04:15:00                         │
│ Profit at drawdown start               │ 2.139 USDT                                │
│ Profit at drawdown end                 │ -2.996 USDT                               │
│ Drawdown start                         │ 2025-07-01 09:45:00                       │
│ Drawdown end                           │ 2025-11-05 14:00:00                       │
┃[1m [0m[1m                     Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/SMC_ICT_High_Frequency_Engine_20260619_031256.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
