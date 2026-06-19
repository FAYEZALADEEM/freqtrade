# ملخص باكتيست: SMC_ICT_Riyadh

**التاريخ:** 2026-06-19 03:35
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy SMC_ICT_Riyadh --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                             BACKTESTING REPORT                                              [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │    400 │         0.03 │          13.717 │         1.37 │     20:37:00 │  189     0   211  47.2 │
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │      1 │         0.21 │           0.209 │         0.02 │     12:45:00 │    1     0     0   100 │
┃[1m [0m[1m       Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│            TOTAL │     400 │         0.03 │          13.717 │         1.37 │     20:37:00 │  189     0   211  47.2 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │   400 │         0.03 │          13.717 │         1.37 │     20:37:00 │  189     0   211  47.2 │
┃[1m [0m[1m       Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│            TOTAL │             │    400 │         0.03 │          13.717 │         1.37 │     20:37:00 │  189     0   211  47.2 │
│ Total/Daily Avg Trades                 │ 400 / 1.1                                 │
│ Profit factor                          │ 1.21                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 00:30 / 7d 12:45 / 0d 21:58            │
│ Max Consecutive Wins / Loss            │ 6 / 7                                     │
│ Drawdown duration                      │ 20 days 03:45:00                          │
│ Profit at drawdown start               │ 9.539 USDT                                │
│ Profit at drawdown end                 │ 6.526 USDT                                │
│ Drawdown start                         │ 2025-04-22 03:15:00                       │
│ Drawdown end                           │ 2025-05-12 07:00:00                       │
│ Drawdown duration                      │ 20 days 01:45:00                          │
│ Profit at drawdown start               │ 9.624 USDT                                │
│ Profit at drawdown end                 │ 6.526 USDT                                │
│ Drawdown start                         │ 2025-04-22 05:30:00                       │
│ Drawdown end                           │ 2025-05-12 07:15:00                       │
┃[1m [0m[1m      Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/SMC_ICT_Riyadh_20260619_033533.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
