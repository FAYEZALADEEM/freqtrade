# ملخص باكتيست: LIB_STR045

**التاريخ:** 2026-06-19 06:45
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR045 --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
                                               BACKTESTING REPORT                                                
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│    TOTAL │     56 │         0.25 │          14.087 │         1.41 │ 6 days, 10:14:00 │   35     0    21  62.5 │
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│    TOTAL │      1 │        -0.26 │          -0.258 │        -0.03 │ 15 days, 8:45:00 │    0     0     1     0 │
┃   Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│       TOTAL │      56 │         0.25 │          14.087 │         1.41 │ 6 days, 10:14:00 │   35     0    21  62.5 │
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│       TOTAL │    56 │         0.25 │          14.087 │         1.41 │ 6 days, 10:14:00 │   35     0    21  62.5 │
┃   Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│       TOTAL │             │     56 │         0.25 │          14.087 │         1.41 │ 6 days, 10:14:00 │   35     0    21  62.5 │
│ Total/Daily Avg Trades                 │ 56 / 0.15                                 │
│ Profit factor                          │ 1.67                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 02:45 / 33d 03:00 / 6d 06:38           │
│ Max Consecutive Wins / Loss            │ 6 / 3                                     │
│ Drawdown duration                      │ 21 days 21:00:00                          │
│ Profit at drawdown start               │ 15.343 USDT                               │
│ Profit at drawdown end                 │ 12.345 USDT                               │
│ Drawdown start                         │ 2025-09-17 18:00:00                       │
│ Drawdown end                           │ 2025-10-09 15:00:00                       │
│ Drawdown duration                      │ 48 days 19:45:00                          │
│ Profit at drawdown start               │ 15.343 USDT                               │
│ Profit at drawdown end                 │ 11.765 USDT                               │
│ Drawdown start                         │ 2025-09-17 18:15:00                       │
│ Drawdown end                           │ 2025-11-05 14:00:00                       │
┃   Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃          Drawdown ┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/LIB_STR045_20260619_064514.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
