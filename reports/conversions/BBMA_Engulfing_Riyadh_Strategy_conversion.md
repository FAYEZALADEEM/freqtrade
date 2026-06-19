# تقرير تحويل الاستراتيجية

**اسم الاستراتيجية الأصلية:** BBMA_Engulfing_Riyadh_Strategy_v6.pine  
**الملف الجديد:** user_data/strategies/BBMA_Engulfing_Riyadh_Strategy.py  
**تاريخ التحويل:** 2026-06-19  

## ما تم تحويله

- BBMA (Bollinger + EMA)
- Engulfing detection (body or break)
- Zones and confluence models (squeeze, extreme, rejection)
- Session filter (Riyadh)
- Risk based position sizing
- SL/TP with RR
- Min bars between trades, zone age

## ما تم تجاهله / تعديله

- Full var pending zones and active SL/TP state - simplified (may miss some edge cases)
- Exact array based FVG or other complex memory
- Some inputs mapped to class attributes

## ما يحتاج اختبار

- Number of trades
- Win rate and profit
- If zones and entries match original
- Lookahead (will be checked)

## ملاحظات

- Strategy uses complex state; conversion is approximate for backtesting.
- Good candidate for further tuning.
