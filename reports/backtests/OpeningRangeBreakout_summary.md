# ملخص باكتيست: OpeningRangeBreakout

**التاريخ:** 2026-06-19 06:43
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy OpeningRangeBreakout --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                               BACKTESTING REPORT                                                [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     40 │         0.27 │          10.615 │         1.06 │ 8 days, 13:24:00 │   21     0    19  52.5 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │         0.03 │           0.034 │          0.0 │ 20 days, 7:00:00 │    1     0     0   100 │
┃[1m [0m[1mEnter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│     TOTAL │      40 │         0.27 │          10.615 │         1.06 │ 8 days, 13:24:00 │   21     0    19  52.5 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    40 │         0.27 │          10.615 │         1.06 │ 8 days, 13:24:00 │   21     0    19  52.5 │
┃[1m [0m[1mEnter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│     TOTAL │             │     40 │         0.27 │          10.615 │         1.06 │ 8 days, 13:24:00 │   21     0    19  52.5 │
│ Total/Daily Avg Trades                 │ 40 / 0.11                                 │
│ Profit factor                          │ 1.55                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 03:45 / 62d 13:15 / 10d 04:29          │
│ Max Consecutive Wins / Loss            │ 3 / 4                                     │
│ Drawdown duration                      │ 21 days 06:45:00                          │
│ Profit at drawdown start               │ 8.574 USDT                                │
│ Profit at drawdown end                 │ 4.578 USDT                                │
│ Drawdown start                         │ 2025-04-21 00:30:00                       │
│ Drawdown end                           │ 2025-05-12 07:15:00                       │
│ Drawdown duration                      │ 21 days 17:15:00                          │
│ Profit at drawdown start               │ 8.678 USDT                                │
│ Profit at drawdown end                 │ 4.529 USDT                                │
│ Drawdown start                         │ 2025-04-21 09:15:00                       │
│ Drawdown end                           │ 2025-05-13 02:30:00                       │
┃[1m [0m[1m            Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/OpeningRangeBreakout_20260619_064312.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
