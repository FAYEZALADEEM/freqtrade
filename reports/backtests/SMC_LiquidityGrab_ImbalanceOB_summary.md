# ملخص باكتيست: SMC_LiquidityGrab_ImbalanceOB

**التاريخ:** 2026-06-19 03:32
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy SMC_LiquidityGrab_ImbalanceOB --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                             BACKTESTING REPORT                                              [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     14 │          0.0 │           0.013 │          0.0 │      3:11:00 │    8     3     3  57.1 │
┃[1m [0m[1m Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
┃[1m [0m[1m    Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│         TOTAL │      14 │          0.0 │           0.013 │          0.0 │      3:11:00 │    8     3     3  57.1 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    14 │          0.0 │           0.013 │          0.0 │      3:11:00 │    8     3     3  57.1 │
┃[1m [0m[1m    Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│         TOTAL │             │     14 │          0.0 │           0.013 │          0.0 │      3:11:00 │    8     3     3  57.1 │
│ Total/Daily Avg Trades                 │ 14 / 0.04                                 │
│ Profit factor                          │ 1.02                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 03:00 / 0d 03:00 / 0d 03:00            │
│ Max Consecutive Wins / Loss            │ 3 / 2                                     │
│ Drawdown duration                      │ 98 days 21:45:00                          │
│ Profit at drawdown start               │ 0 USDT                                    │
│ Profit at drawdown end                 │ -0.325 USDT                               │
│ Drawdown start                         │ 2025-01-20 17:00:00                       │
│ Drawdown end                           │ 2025-04-29 14:45:00                       │
│ Drawdown duration                      │ 112 days 05:45:00                         │
│ Profit at drawdown start               │ 0.263 USDT                                │
│ Profit at drawdown end                 │ -0.366 USDT                               │
│ Drawdown start                         │ 2025-01-20 15:15:00                       │
│ Drawdown end                           │ 2025-05-12 21:00:00                       │
┃[1m [0m[1m                     Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/SMC_LiquidityGrab_ImbalanceOB_20260619_033213.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
