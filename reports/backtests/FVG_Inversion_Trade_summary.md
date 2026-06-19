# ملخص باكتيست: FVG_Inversion_Trade

**التاريخ:** 2026-06-19 04:10
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy FVG_Inversion_Trade --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
[3m                                             BACKTESTING REPORT                                              [0m
┃[1m [0m[1m    Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│    TOTAL │   1630 │          0.0 │           3.181 │         0.32 │      2:46:00 │  782   492   356  48.0 │
┃[1m [0m[1m Pair[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│ TOTAL │      0 │          0.0 │           0.000 │          0.0 │         0:00 │    0     0     0     0 │
┃[1m [0m[1m   Enter Tag[0m[1m [0m┃[1m [0m[1mEntries[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│        TOTAL │    1630 │          0.0 │           3.181 │         0.32 │      2:46:00 │  782   492   356  48.0 │
┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mExits[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│       TOTAL │  1630 │          0.0 │           3.181 │         0.32 │      2:46:00 │  782   492   356  48.0 │
┃[1m [0m[1m   Enter Tag[0m[1m [0m┃[1m [0m[1mExit Reason[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃
│        TOTAL │             │   1630 │          0.0 │           3.181 │         0.32 │      2:46:00 │  782   492   356  48.0 │
│ Total/Daily Avg Trades                 │ 1630 / 4.49                               │
│ Profit factor                          │ 1.04                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 00:15 / 2d 03:15 / 0d 01:44            │
│ Max Consecutive Wins / Loss            │ 7 / 10                                    │
│ Drawdown duration                      │ 61 days 05:30:00                          │
│ Profit at drawdown start               │ 1.154 USDT                                │
│ Profit at drawdown end                 │ -2.795 USDT                               │
│ Drawdown start                         │ 2025-01-31 16:45:00                       │
│ Drawdown end                           │ 2025-04-02 22:15:00                       │
│ Drawdown duration                      │ 61 days 01:45:00                          │
│ Profit at drawdown start               │ 1.226 USDT                                │
│ Profit at drawdown end                 │ -2.795 USDT                               │
│ Drawdown start                         │ 2025-01-31 20:45:00                       │
│ Drawdown end                           │ 2025-04-02 22:30:00                       │
┃[1m [0m[1m           Strategy[0m[1m [0m┃[1m [0m[1mTrades[0m[1m [0m┃[1m [0m[1mAvg Profit %[0m[1m [0m┃[1m [0m[1mTot Profit USDT[0m[1m [0m┃[1m [0m[1mTot Profit %[0m[1m [0m┃[1m [0m[1mAvg Duration[0m[1m [0m┃[1m [0m[1m Win  Draw  Loss  Win%[0m[1m [0m┃[1m [0m[1m         Drawdown[0m[1m [0m┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/FVG_Inversion_Trade_20260619_041023.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
