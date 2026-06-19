# ملخص باكتيست: RSI_Divergence_Reversal

**التاريخ:** 2026-06-19 04:29
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy RSI_Divergence_Reversal --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                             BACKTESTING REPORT                                              [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │     88 │         0.02 │           2.131 │         0.21 │      2:19:00 │   55    13    20  62.5 │
┃[1m [0m[1m Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
┃[1m [0m[1m   Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│        TOTAL │      88 │         0.02 │           2.131 │         0.21 │      2:19:00 │   55    13    20  62.5 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │    88 │         0.02 │           2.131 │         0.21 │      2:19:00 │   55    13    20  62.5 │
┃[1m [0m[1m   Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│        TOTAL │             │     88 │         0.02 │           2.131 │         0.21 │      2:19:00 │   55    13    20  62.5 │
│ Total/Daily Avg Trades                 │ 88 / 0.24                                 │
│ Profit factor                          │ 1.53                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 00:15 / 0d 02:00 / 0d 01:56            │
│ Max Consecutive Wins / Loss            │ 10 / 6                                    │
│ Drawdown duration                      │ 62 days 01:45:00                          │
│ Profit at drawdown start               │ 2.561 USDT                                │
│ Profit at drawdown end                 │ 1.266 USDT                                │
│ Drawdown start                         │ 2025-07-25 15:30:00                       │
│ Drawdown end                           │ 2025-09-25 17:15:00                       │
│ Drawdown duration                      │ 71 days 19:45:00                          │
│ Profit at drawdown start               │ 2.565 USDT                                │
│ Profit at drawdown end                 │ 1.21 USDT                                 │
│ Drawdown start                         │ 2025-07-28 10:45:00                       │
│ Drawdown end                           │ 2025-10-08 06:30:00                       │
┃[1m [0m[1m               Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/RSI_Divergence_Reversal_20260619_042905.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
