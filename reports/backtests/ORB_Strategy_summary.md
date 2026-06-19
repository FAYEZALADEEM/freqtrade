# ملخص باكتيست: ORB_Strategy

**التاريخ:** 2026-06-19 06:42
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy ORB_Strategy --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                             BACKTESTING REPORT                                              [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │    346 │        -0.03 │         -12.032 │         -1.2 │     10:26:00 │  111     0   235  32.1 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │         0.03 │           0.027 │          0.0 │      5:45:00 │    1     0     0   100 │
┃[1m [0m[1mEnter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│     TOTAL │     346 │        -0.03 │         -12.032 │         -1.2 │     10:26:00 │  111     0   235  32.1 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │   346 │        -0.03 │         -12.032 │         -1.2 │     10:26:00 │  111     0   235  32.1 │
┃[1m [0m[1mEnter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│     TOTAL │             │    346 │        -0.03 │         -12.032 │         -1.2 │     10:26:00 │  111     0   235  32.1 │
│ Total/Daily Avg Trades                 │ 346 / 0.95                                │
│ Profit factor                          │ 0.74                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 00:15 / 4d 01:45 / 0d 13:54            │
│ Max Consecutive Wins / Loss            │ 4 / 12                                    │
│ Drawdown duration                      │ 303 days 19:15:00                         │
│ Profit at drawdown start               │ 1.126 USDT                                │
│ Profit at drawdown end                 │ -12.396 USDT                              │
│ Drawdown start                         │ 2025-01-21 16:30:00                       │
│ Drawdown end                           │ 2025-11-21 11:45:00                       │
│ Drawdown duration                      │ 307 days 06:45:00                         │
│ Profit at drawdown start               │ 1.207 USDT                                │
│ Profit at drawdown end                 │ -12.575 USDT                              │
│ Drawdown start                         │ 2025-01-21 22:45:00                       │
│ Drawdown end                           │ 2025-11-25 05:30:00                       │
┃[1m [0m[1m    Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m          Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/ORB_Strategy_20260619_064229.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
