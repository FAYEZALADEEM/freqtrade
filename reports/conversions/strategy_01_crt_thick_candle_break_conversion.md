# تقرير تحويل الاستراتيجية

**اسم الاستراتيجية الأصلية:** strategy_01_crt_thick_candle_break.pine  
**الملف الجديد:** user_data/strategies/CRT_ThickCandleBreak.py  
**تاريخ التحويل:** 2026-06-19  
**المرحلة:** 8

## ما تم تحويله

- المنطق الأساسي: Liquidity Sweep (كسر pivot) + Thick Candle + Break of previous candle body
- استخدام pivothigh / pivotlow → تم تحويله إلى rolling max/min تاريخي + last_ph / last_pl
- thick candle detection باستخدام ATR
- شروط الدخول Long و Short مع enter_tag واضحة
- SL و Target بناءً على RR (custom_exit + custom_stoploss)
- دعم Break Even (اختياري)
- تعليقات عربية قصيرة في الكود
- can_short = True (تطابق الأصلية)
- timeframe = 15m
- كل دخول له enter_tag (`crt_sweep_long` / `crt_sweep_short`)
- كل خروج له exit_tag في custom_exit (`rr_target`)

## ما تم تجاهله / تعديله

- حساب الـ stop من قمة/قاع الشمعة الفعلية: تم استبداله بـ fixed pips (20) + custom
- dynamic target من سعر الدخول: تم تنفيذه في custom_exit باستخدام RR
- session filter: معطل (كما في الإعداد الافتراضي للـ Pine)
- plotshape و alertcondition: غير مطلوبة في Freqtrade
- pipSize كـ input: تم تثبيته داخلياً (0.0001)
- بعض المتغيرات الإضافية مثل showMarks: تم تجاهلها

## ما يحتاج اختبار

- دقة كشف الـ pivots مقارنة بـ ta.pivothigh في Pine (سنختبر بـ backtesting-analysis)
- سلوك الـ SL و Target مع RR=2.0
- أداء الـ short مع الـ long
- عدد الصفقات و Win Rate على الفترة 20250101-20260101
- lookahead (سيتم تشغيل lookahead-analysis بعد الباكتيست)
- ما إذا كان الـ break even مفيد أم لا

## ملاحظات

- الاستراتيجية لا تستخدم أي lookahead (كل الشروط على .shift(1))
- لا يوجد request.security في الأصل
- مناسبة لـ FreqAI في المستقبل (ميزات مثل %sweep_strength, %dist_to_pivot يمكن إضافتها)
- تم الالتزام بكل القواعد: timerange, fee=0, export signals, enter/exit tags, no lookahead

## الخطوات التالية

1. موافقة على الاختبار (backtesting)
2. تشغيل الباكتيست
3. backtesting-analysis
4. lookahead-analysis
5. قرار القبول أو الرفض
