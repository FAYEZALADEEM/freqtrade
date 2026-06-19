# ملخص باكتيست: LIB_STR058

**التاريخ:** 2026-06-19 06:55
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR058 --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
                                               BACKTESTING REPORT                                               
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
│    TOTAL │     49 │         0.23 │          11.498 │         1.15 │ 6 days, 3:19:00 │   31     0    18  63.3 │
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
│    TOTAL │      1 │         0.07 │           0.070 │         0.01 │ 19 days, 13:15:00 │    1     0     0   100 │
┃       Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃
│           TOTAL │      49 │         0.23 │          11.498 │         1.15 │ 6 days, 3:19:00 │   31     0    18  63.3 │
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
│       TOTAL │    49 │         0.23 │          11.498 │         1.15 │   6 days, 3:19:00 │   31     0    18  63.3 │
┃       Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃      Avg Duration ┃  Win  Draw  Loss  Win% ┃
│           TOTAL │             │     49 │         0.23 │          11.498 │         1.15 │   6 days, 3:19:00 │   31     0    18  63.3 │
│ Total/Daily Avg Trades                 │ 49 / 0.13                                 │
│ Profit factor                          │ 1.62                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 07:00 / 31d 09:00 / 5d 08:57           │
│ Max Consecutive Wins / Loss            │ 4 / 3                                     │
│ Drawdown duration                      │ 45 days 04:45:00                          │
│ Profit at drawdown start               │ 12.427 USDT                               │
│ Profit at drawdown end                 │ 9.429 USDT                                │
│ Drawdown start                         │ 2025-09-16 09:30:00                       │
│ Drawdown end                           │ 2025-10-31 14:15:00                       │
│ Drawdown duration                      │ 48 days 19:45:00                          │
│ Profit at drawdown start               │ 12.785 USDT                               │
│ Profit at drawdown end                 │ 8.981 USDT                                │
│ Drawdown start                         │ 2025-09-17 18:15:00                       │
│ Drawdown end                           │ 2025-11-05 14:00:00                       │
┃   Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃    Avg Duration ┃  Win  Draw  Loss  Win% ┃          Drawdown ┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/LIB_STR058_20260619_065515.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
