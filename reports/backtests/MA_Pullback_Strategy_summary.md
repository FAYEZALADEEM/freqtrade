# ملخص باكتيست: MA_Pullback_Strategy

**التاريخ:** 2026-06-19 06:45
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy MA_Pullback_Strategy --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                             BACKTESTING REPORT                                              [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     86 │        -0.03 │          -2.555 │        -0.26 │     14:25:00 │   24     0    62  27.9 │
┃[1m [0m[1m Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
┃[1m [0m[1m       Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│            TOTAL │      86 │        -0.03 │          -2.555 │        -0.26 │     14:25:00 │   24     0    62  27.9 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    86 │        -0.03 │          -2.555 │        -0.26 │     14:25:00 │   24     0    62  27.9 │
┃[1m [0m[1m       Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│            TOTAL │             │     86 │        -0.03 │          -2.555 │        -0.26 │     14:25:00 │   24     0    62  27.9 │
│ Total/Daily Avg Trades                 │ 86 / 0.24                                 │
│ Profit factor                          │ 0.79                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 00:30 / 5d 11:45 / 0d 22:36            │
│ Max Consecutive Wins / Loss            │ 3 / 11                                    │
│ Drawdown duration                      │ 222 days 17:45:00                         │
│ Profit at drawdown start               │ 1.213 USDT                                │
│ Profit at drawdown end                 │ -3.293 USDT                               │
│ Drawdown start                         │ 2025-01-22 10:30:00                       │
│ Drawdown end                           │ 2025-09-02 04:15:00                       │
│ Drawdown duration                      │ 146 days 21:15:00                         │
│ Profit at drawdown start               │ 1.323 USDT                                │
│ Profit at drawdown end                 │ -3.347 USDT                               │
│ Drawdown start                         │ 2025-04-14 07:00:00                       │
│ Drawdown end                           │ 2025-09-08 04:15:00                       │
┃[1m [0m[1m            Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/MA_Pullback_Strategy_20260619_064509.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
