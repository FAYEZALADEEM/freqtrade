# ملخص باكتيست: LIB_STR057

**التاريخ:** 2026-06-19 06:55
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR057 --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
                                               BACKTESTING REPORT                                                
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│    TOTAL │     47 │         0.11 │           5.211 │         0.52 │ 6 days, 14:24:00 │   27     0    20  57.4 │
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
│    TOTAL │      1 │         0.38 │           0.378 │         0.04 │ 20 days, 21:30:00 │    1     0     0   100 │
┃       Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│           TOTAL │      47 │         0.11 │           5.211 │         0.52 │ 6 days, 14:24:00 │   27     0    20  57.4 │
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
│       TOTAL │    47 │         0.11 │           5.211 │         0.52 │  6 days, 14:24:00 │   27     0    20  57.4 │
┃       Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
│           TOTAL │             │     47 │         0.11 │           5.211 │         0.52 │  6 days, 14:24:00 │   27     0    20  57.4 │
│ Total/Daily Avg Trades                 │ 47 / 0.13                                 │
│ Profit factor                          │ 1.25                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 01:15 / 33d 03:00 / 6d 18:53           │
│ Max Consecutive Wins / Loss            │ 4 / 4                                     │
│ Drawdown duration                      │ 49 days 05:00:00                          │
│ Profit at drawdown start               │ 6.831 USDT                                │
│ Profit at drawdown end                 │ 2.834 USDT                                │
│ Drawdown start                         │ 2025-09-16 09:30:00                       │
│ Drawdown end                           │ 2025-11-04 14:30:00                       │
│ Drawdown duration                      │ 48 days 19:45:00                          │
│ Profit at drawdown start               │ 6.975 USDT                                │
│ Profit at drawdown end                 │ 2.715 USDT                                │
│ Drawdown start                         │ 2025-09-17 18:15:00                       │
│ Drawdown end                           │ 2025-11-05 14:00:00                       │
┃   Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃          Drawdown ┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/LIB_STR057_20260619_065509.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
