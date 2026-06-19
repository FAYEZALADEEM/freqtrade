# ملخص باكتيست: BBMA_Engulfing_Riyadh_Strategy

**التاريخ:** 2026-06-19 03:16
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy BBMA_Engulfing_Riyadh_Strategy --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                               BACKTESTING REPORT                                                [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     17 │         0.76 │          12.955 │          1.3 │ 20 days, 6:52:00 │   11     0     6  64.7 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │        -0.03 │          -0.031 │         -0.0 │ 15 days, 15:00:00 │    0     0     1     0 │
┃[1m [0m[1m       Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│            TOTAL │      17 │         0.76 │          12.955 │          1.3 │ 20 days, 6:52:00 │   11     0     6  64.7 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    17 │         0.76 │          12.955 │          1.3 │  20 days, 6:52:00 │   11     0     6  64.7 │
┃[1m [0m[1m       Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│            TOTAL │             │     17 │         0.76 │          12.955 │          1.3 │  20 days, 6:52:00 │   11     0     6  64.7 │
│ Total/Daily Avg Trades                 │ 17 / 0.05                                 │
│ Profit factor                          │ 2.29                                      │
│ Min/Max/Avg. Duration Winners          │ 2d 01:45 / 61d 09:30 / 22d 00:57          │
│ Max Consecutive Wins / Loss            │ 5 / 2                                     │
│ Drawdown duration                      │ 21 days 05:30:00                          │
│ Profit at drawdown start               │ 10.793 USDT                               │
│ Profit at drawdown end                 │ 6.794 USDT                                │
│ Drawdown start                         │ 2025-04-21 02:30:00                       │
│ Drawdown end                           │ 2025-05-12 08:00:00                       │
│ Drawdown duration                      │ 29 days 11:00:00                          │
│ Profit at drawdown start               │ 13.034 USDT                               │
│ Profit at drawdown end                 │ 8.697 USDT                                │
│ Drawdown start                         │ 2025-07-03 01:30:00                       │
│ Drawdown end                           │ 2025-08-01 12:30:00                       │
┃[1m [0m[1m                      Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/BBMA_Engulfing_Riyadh_Strategy_20260619_031653.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
