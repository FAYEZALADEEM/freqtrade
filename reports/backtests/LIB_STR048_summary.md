# ملخص باكتيست: LIB_STR048

**التاريخ:** 2026-06-19 06:45
**الأمر المستخدم:**
```
/home/fayez/freqtrade/.venv/bin/freqtrade backtesting --config user_data/config.json --config <(echo '{"freqai": {"enabled": false}}') --strategy LIB_STR048 --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## النتائج الرئيسية

```
                                               BACKTESTING REPORT                                                
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│    TOTAL │     60 │         0.15 │           8.845 │         0.88 │ 5 days, 19:36:00 │   35     0    25  58.3 │
┃     Pair ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│    TOTAL │      1 │         0.41 │           0.414 │         0.04 │ 21 days, 1:30:00 │    1     0     0   100 │
┃   Enter Tag ┃ Entries ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│       TOTAL │      60 │         0.15 │           8.845 │         0.88 │ 5 days, 19:36:00 │   35     0    25  58.3 │
┃ Exit Reason ┃ Exits ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│       TOTAL │    60 │         0.15 │           8.845 │         0.88 │ 5 days, 19:36:00 │   35     0    25  58.3 │
┃   Enter Tag ┃ Exit Reason ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃
│       TOTAL │             │     60 │         0.15 │           8.845 │         0.88 │ 5 days, 19:36:00 │   35     0    25  58.3 │
│ Total/Daily Avg Trades                 │ 60 / 0.17                                 │
│ Profit factor                          │ 1.35                                      │
│ Min/Max/Avg. Duration Winners          │ 0d 00:45 / 40d 10:45 / 6d 01:51           │
│ Max Consecutive Wins / Loss            │ 6 / 4                                     │
│ Drawdown duration                      │ 29 days 18:30:00                          │
│ Profit at drawdown start               │ 10.426 USDT                               │
│ Profit at drawdown end                 │ 6.429 USDT                                │
│ Drawdown start                         │ 2025-06-30 18:15:00                       │
│ Drawdown end                           │ 2025-07-30 12:45:00                       │
│ Drawdown duration                      │ 31 days 02:45:00                          │
│ Profit at drawdown start               │ 10.792 USDT                               │
│ Profit at drawdown end                 │ 5.638 USDT                                │
│ Drawdown start                         │ 2025-07-01 09:45:00                       │
│ Drawdown end                           │ 2025-08-01 12:30:00                       │
┃   Strategy ┃ Trades ┃ Avg Profit % ┃ Tot Profit USDT ┃ Tot Profit % ┃     Avg Duration ┃  Win  Draw  Loss  Win% ┃          Drawdown ┃
```

**رمز الخروج:** 0
**ملف السجل الكامل:** reports/backtests/LIB_STR048_20260619_064529.log

---
**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.
