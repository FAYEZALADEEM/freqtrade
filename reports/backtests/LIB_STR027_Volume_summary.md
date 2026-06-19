# ملخص باكتيست: LIB_STR027_Volume

**التاريخ:** 2026-06-19 06:37
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR027_Volume --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                               BACKTESTING REPORT                                                [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     58 │         0.17 │          10.077 │         1.01 │ 5 days, 15:05:00 │   34     0    24  58.6 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │        -0.24 │          -0.240 │        -0.02 │ 15 days, 7:45:00 │    0     0     1     0 │
┃[1m [0m[1m     Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│          TOTAL │      58 │         0.17 │          10.077 │         1.01 │ 5 days, 15:05:00 │   34     0    24  58.6 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    58 │         0.17 │          10.077 │         1.01 │ 5 days, 15:05:00 │   34     0    24  58.6 │
┃[1m [0m[1m     Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│          TOTAL │             │     58 │         0.17 │          10.077 │         1.01 │ 5 days, 15:05:00 │   34     0    24  58.6 │
│ Total/Daily Avg Trades                 │ 58 / 0.16                                 │
│ Profit factor                          │ 1.42                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 01:15 / 31d 09:00 / 4d 19:34           │
│ Max Consecutive Wins / Loss            │ 4 / 3                                     │
│ Drawdown duration                      │ 29 days 18:45:00                          │
│ Profit at drawdown start               │ 11.313 USDT                               │
│ Profit at drawdown end                 │ 7.317 USDT                                │
│ Drawdown start                         │ 2025-07-01 00:00:00                       │
│ Drawdown end                           │ 2025-07-30 18:45:00                       │
│ Drawdown duration                      │ 31 days 02:45:00                          │
│ Profit at drawdown start               │ 11.544 USDT                               │
│ Profit at drawdown end                 │ 6.757 USDT                                │
│ Drawdown start                         │ 2025-07-01 09:45:00                       │
│ Drawdown end                           │ 2025-08-01 12:30:00                       │
┃[1m [0m[1m         Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1m    Avg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/LIB_STR027_Volume_20260619_063706.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
