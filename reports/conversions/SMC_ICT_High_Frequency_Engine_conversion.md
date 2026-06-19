# تقرير تحويل الاستراتيجية

**اسم الاستراتيجية الأصلية:** SMC_ICT_High_Frequency_Engine_v6.pine  
**الملف الجديد:** user_data/strategies/SMC_ICT_High_Frequency_Engine.py  
**تاريخ التحويل:** 2026-06-19  

## ما تم تحويله

- منطق الجلسات (CRT + Killzone)
- كشف السيولة باستخدام pivots
- FVG detection
- شروط الدخول على sweep + FVG في Killzone
- SL و TP بناءً على RR 1:2
- enter_tag و exit_tag

## ما تم تجاهله / تعديله

- var state معقد (sweep counters, FVG arrays) - تم تبسيطه بـ shift
- daily_trade_count limit - تم تجاهله في هذه النسخة
- max_boxes و max_lines - غير ذي صلة
- بعض الذاكرة لتجنب التكرار - تم تبسيطها

## ما يحتاج اختبار

- أداء في الباكتيست
- هل الـ FVG و sweep دقيق
- عدد الصفقات و Win Rate
- lookahead (سيتم فحصه)

## ملاحظات

- الاستراتيجية عالية التردد (high frequency)
- تعتمد على جلسات محددة
- مناسبة لـ FreqAI في المستقبل (ميزات الجلسة والـ FVG)
