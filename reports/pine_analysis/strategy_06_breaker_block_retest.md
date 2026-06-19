# تحليل Pine Script: strategy_06_breaker_block_retest

**الملف الأصلي:** strategy_06_breaker_block_retest.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 04:12

## 1. المدخلات (Inputs)

- `pipSize = input...(0.0001, "حجم النقطة", step = 0.00001, group = grp01, tooltip = "حجم النقطة المستخدم في حساب الوقف والهدف.")`
- `enableLong = input...(true, "تفعيل الشراء", group = grp02, tooltip = "يسمح بصفقات الشراء.")`
- `enableShort = input...(true, "تفعيل البيع", group = grp02, tooltip = "يسمح بصفقات البيع.")`
- `pivotLen = input...(5, "طول الكسر", minval = 2, maxval = 50, group = grp03, tooltip = "عدد الشموع لاكتشاف مستويات الدعم والمقاومة التي تكوّن breaker.")`
- `maxRetestBars = input...(40, "أقصى شموع لإعادة الاختبار", minval = 1, maxval = 200, group = grp03, tooltip = "يلغي المنطقة إذا لم يحدث retest خلالها.")`
- `stopLossPips = input...(20.0, "وقف الخسارة بالنقاط", minval = 1.0, group = grp06, tooltip = "وقف افتراضي بالنقاط.")`
- `rr = input...(2.0, "نسبة الهدف إلى المخاطرة", minval = 0.5, step = 0.1, group = grp06, tooltip = "مضاعف الهدف مقابل الوقف.")`
- `useBreakEven = input...(false, "تفعيل التعادل", group = grp07, tooltip = "ينقل الوقف إلى الدخول بعد ربح محدد.")`
- `breakEvenAfterPips = input...(15.0, "تفعيل التعادل بعد", minval = 1.0, group = grp07, tooltip = "عدد النقاط اللازمة لتفعيل التعادل.")`
- `useSessionFilter = input...(false, "تفعيل فلتر الجلسة", group = grp09, tooltip = "فلتر الجلسة معطل افتراضياً.")`
- `tradeSession = input...("0000-2359", "وقت الجلسة", group = grp09, tooltip = "وقت التداول عند تفعيل فلتر الجلسة.")`
- `showMarks = input...(true, "عرض العلامات", group = grp10, tooltip = "يعرض إشارات الدخول على الشارت.")`

## 2. المؤشرات المستخدمة

- ta.pivothigh
- ta.pivotlow
- ta.valuewhen

## 3. شروط الدخول (Long/Short)

```
strategy.entry("شراء Breaker", strategy.long) if shortSignal strategy.entry("بيع Breaker", strategy.short) longStop = useBreakEven and strategy.position_size > 0 and close >= strategy.position_avg_price + breakEvenAfterPips * pipSize ? strategy.position_avg_price : strategy.position_avg_price - stop
```

## 4. شروط الخروج

```
strategy.exit("خروج شراء Breaker", "شراء Breaker", stop = longStop, limit = strategy.position_avg_price + stopLossPips * pipSize * rr) strategy.exit("خروج بيع Breaker", "بيع Breaker", stop = shortStop, limit = strategy.position_avg_price - stopLossPips * pipSize * rr) plotshape(showMarks and longSig
```

## 5. المخاطر والعناصر الصعبة في التحويل

- ⚠️ var / حالة محفوظة - قد تحتاج logic معقدة في Python

## 6. معلومات إضافية

- يستخدم `request.security`: False
- يستخدم pivothigh/pivotlow: True
- دعم/مقاومة يدوية محتملة: False
- يستخدم `var`: True
- يدعم Long: True
- يدعم Short: True

## 7. الأعمدة المقترحة في DataFrame

high, pivot_low, pivot_high, open, close, volume, low

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_strategy_06_breaker_`
- exit_tag: `exit_pine_strategy_06_breaker_`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
