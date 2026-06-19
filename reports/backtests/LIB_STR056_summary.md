# ملخص باكتيست: LIB_STR056

**التاريخ:** 2026-06-19 06:55
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR056 --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
                                               BACKTESTING REPORT                                                
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│    TOTAL │     11 │        -0.02 │          -0.188 │        -0.02 │ 5 days, 15:26:00 │    5     0     6  45.5 │
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│    TOTAL │      1 │        -0.19 │          -0.191 │        -0.02 │ 2 days, 23:30:00 │    0     0     1     0 │
┃       Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│           TOTAL │      11 │        -0.02 │          -0.188 │        -0.02 │ 5 days, 15:26:00 │    5     0     6  45.5 │
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│       TOTAL │    11 │        -0.02 │          -0.188 │        -0.02 │ 5 days, 15:26:00 │    5     0     6  45.5 │
┃       Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│           TOTAL │             │     11 │        -0.02 │          -0.188 │        -0.02 │ 5 days, 15:26:00 │    5     0     6  45.5 │
│ Total/Daily Avg Trades                 │ 11 / 0.03                                 │
│ Profit factor                          │ 0.96                                      │
│ Min/Max/Avg. Duration Winners          │ 1d 20:45 / 8d 16:45 / 4d 00:54            │
│ Max Consecutive Wins / Loss            │ 2 / 3                                     │
│ Drawdown duration                      │ 106 days 07:45:00                         │
│ Profit at drawdown start               │ 2.001 USDT                                │
│ Profit at drawdown end                 │ -0.188 USDT                               │
│ Drawdown start                         │ 2025-09-16 14:00:00                       │
│ Drawdown end                           │ 2025-12-31 21:45:00                       │
│ Drawdown duration                      │ 288 days 06:45:00                         │
│ Profit at drawdown start               │ 2.679 USDT                                │
│ Profit at drawdown end                 │ -0.411 USDT                               │
│ Drawdown start                         │ 2025-03-18 08:30:00                       │
│ Drawdown end                           │ 2025-12-31 15:15:00                       │
┃   Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃         Drawdown ┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/LIB_STR056_20260619_065503.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
