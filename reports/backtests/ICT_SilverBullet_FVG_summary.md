# ملخص باكتيست: ICT_SilverBullet_FVG

**التاريخ:** 2026-06-19 03:29
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy ICT_SilverBullet_FVG --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                             BACKTESTING REPORT                                              [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     68 │         0.03 │           2.172 │         0.22 │      3:41:00 │   37    13    18  54.4 │
┃[1m [0m[1m Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
┃[1m [0m[1m          Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│               TOTAL │      68 │         0.03 │           2.172 │         0.22 │      3:41:00 │   37    13    18  54.4 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    68 │         0.03 │           2.172 │         0.22 │      3:41:00 │   37    13    18  54.4 │
┃[1m [0m[1m          Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│               TOTAL │             │     68 │         0.03 │           2.172 │         0.22 │      3:41:00 │   37    13    18  54.4 │
│ Total/Daily Avg Trades                 │ 68 / 0.19                                 │
│ Profit factor                          │ 1.61                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 02:15 / 0d 04:00 / 0d 03:54            │
│ Max Consecutive Wins / Loss            │ 4 / 6                                     │
│ Drawdown duration                      │ 81 days 20:00:00                          │
│ Profit at drawdown start               │ 1.251 USDT                                │
│ Profit at drawdown end                 │ 0.696 USDT                                │
│ Drawdown start                         │ 2025-04-18 15:45:00                       │
│ Drawdown end                           │ 2025-07-09 11:45:00                       │
│ Drawdown duration                      │ 96 days 17:30:00                          │
│ Profit at drawdown start               │ 1.337 USDT                                │
│ Profit at drawdown end                 │ 0.577 USDT                                │
│ Drawdown start                         │ 2025-04-03 23:00:00                       │
│ Drawdown end                           │ 2025-07-09 16:30:00                       │
┃[1m [0m[1m            Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/ICT_SilverBullet_FVG_20260619_032915.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
