# تقرير تحويل الاستراتيجية

**اسم الاستراتيجية الأصلية:** LIB-STR011.pine (Research Draft)  
**الملف الجديد:** user_data/strategies/LIB_STR011.py  
**تاريخ:** 2026-06-19

## ما تم تحويله
- Liquidity sweep detection using recent high/low (lookback 20)
- Score based entry (sweep = 1)
- minBarsBetweenSignals
- Optional exit/SLTP (default off)
- enter_tag lib011_long / lib011_short

## النتائج
- 54 trades
- +0.88%
- WR 59.3%
- Profit factor 1.39

## ملاحظات
- Simple liquidity sweep strategy.
- Research draft nature, rules inferred from description.
