# ملخص باكتيست: BreakerBlock_Retest

**التاريخ:** 2026-06-19 04:15
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy BreakerBlock_Retest --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                             BACKTESTING REPORT                                              [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │    435 │         0.01 │           4.184 │         0.42 │     13:55:00 │  150     0   285  34.5 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │         0.05 │           0.054 │         0.01 │     10:30:00 │    1     0     0   100 │
┃[1m [0m[1m   Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│        TOTAL │     435 │         0.01 │           4.184 │         0.42 │     13:55:00 │  150     0   285  34.5 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │   435 │         0.01 │           4.184 │         0.42 │     13:55:00 │  150     0   285  34.5 │
┃[1m [0m[1m   Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│        TOTAL │             │    435 │         0.01 │           4.184 │         0.42 │     13:55:00 │  150     0   285  34.5 │
│ Total/Daily Avg Trades                 │ 435 / 1.2                                 │
│ Profit factor                          │ 1.07                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 00:00 / 4d 23:15 / 0d 17:42            │
│ Max Consecutive Wins / Loss            │ 5 / 15                                    │
│ Drawdown duration                      │ 31 days 07:30:00                          │
│ Profit at drawdown start               │ 6.277 USDT                                │
│ Profit at drawdown end                 │ 2.013 USDT                                │
│ Drawdown start                         │ 2025-04-11 08:45:00                       │
│ Drawdown end                           │ 2025-05-12 16:15:00                       │
│ Drawdown duration                      │ 31 days 14:15:00                          │
│ Profit at drawdown start               │ 6.36 USDT                                 │
│ Profit at drawdown end                 │ 1.996 USDT                                │
│ Drawdown start                         │ 2025-04-11 09:45:00                       │
│ Drawdown end                           │ 2025-05-13 00:00:00                       │
┃[1m [0m[1m           Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/BreakerBlock_Retest_20260619_041536.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
