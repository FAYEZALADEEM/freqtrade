# ملخص باكتيست: VWAPPullback

**التاريخ:** 2026-06-19 06:46
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy VWAPPullback --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                                BACKTESTING REPORT                                                [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     21 │         0.25 │           5.328 │         0.53 │ 14 days, 18:07:00 │   12     0     9  57.1 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │        -0.24 │          -0.240 │        -0.02 │ 15 days, 7:45:00 │    0     0     1     0 │
┃[1m [0m[1mEnter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│     TOTAL │      21 │         0.25 │           5.328 │         0.53 │ 14 days, 18:07:00 │   12     0     9  57.1 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    21 │         0.25 │           5.328 │         0.53 │ 14 days, 18:07:00 │   12     0     9  57.1 │
┃[1m [0m[1mEnter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│     TOTAL │             │     21 │         0.25 │           5.328 │         0.53 │ 14 days, 18:07:00 │   12     0     9  57.1 │
│ Total/Daily Avg Trades                 │ 21 / 0.06                                 │
│ Profit factor                          │ 1.42                                      │
│ Min/Max/Avg. Duration Winners          │ 3d 12:15 / 34d 09:45 / 15d 05:29          │
│ Max Consecutive Wins / Loss            │ 3 / 2                                     │
│ Drawdown duration                      │ 37 days 15:45:00                          │
│ Profit at drawdown start               │ 5.57 USDT                                 │
│ Profit at drawdown end                 │ 2.57 USDT                                 │
│ Drawdown start                         │ 2025-04-21 07:45:00                       │
│ Drawdown end                           │ 2025-05-28 23:30:00                       │
│ Drawdown duration                      │ 20 days 13:00:00                          │
│ Profit at drawdown start               │ 5.8 USDT                                  │
│ Profit at drawdown end                 │ 1.194 USDT                                │
│ Drawdown start                         │ 2025-04-22 05:30:00                       │
│ Drawdown end                           │ 2025-05-12 18:30:00                       │
┃[1m [0m[1m    Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m     Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m     Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/VWAPPullback_20260619_064610.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
