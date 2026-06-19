# تحليل Pine Script: strategy_05_fvg_inversion_trade

**الملف الأصلي:** strategy_05_fvg_inversion_trade.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 04:09

## 1. المدخلات (Inputs)

- `pipSize = input...(0.0001, "حجم النقطة", step = 0.00001, group = grp01, tooltip = "حجم النقطة المستخدم في حساب الوقف والهدف.")`
- `enableLong = input...(true, "تفعيل الشراء", group = grp02, tooltip = "يسمح بإشارات الشراء.")`
- `enableShort = input...(true, "تفعيل البيع", group = grp02, tooltip = "يسمح بإشارات البيع.")`
- `maxWaitBars = input...(50, "أقصى انتظار لإعادة الاختبار", minval = 1, maxval = 300, group = grp03, tooltip = "عدد الشموع المسموح به بعد انقلاب FVG حتى يحدث retest.")`
- `useCeOnly = input...(true, "اشتراط عدم تجاوز CE", group = grp03, tooltip = "عند التفعيل يجب ألا يتجاوز الإغلاق منتصف FVG أثناء الاختبار.")`
- `stopLossPips = input...(20.0, "وقف الخسارة بالنقاط", minval = 1.0, group = grp06, tooltip = "مسافة الوقف الافتراضية بالنقاط.")`
- `rr = input...(2.0, "نسبة الهدف إلى المخاطرة", minval = 0.5, step = 0.1, group = grp06, tooltip = "مضاعف الهدف إلى الوقف.")`
- `useBreakEven = input...(false, "تفعيل التعادل", group = grp07, tooltip = "ينقل الوقف إلى نقطة الدخول عند تحقق ربح محدد.")`
- `breakEvenAfterPips = input...(15.0, "تفعيل التعادل بعد", minval = 1.0, group = grp07, tooltip = "عدد النقاط المطلوبة لتفعيل التعادل.")`
- `useSessionFilter = input...(false, "تفعيل فلتر الجلسة", group = grp09, tooltip = "فلتر الجلسة معطل افتراضياً.")`
- `tradeSession = input...("0000-2359", "وقت الجلسة", group = grp09, tooltip = "وقت الجلسة عند تفعيل الفلتر.")`
- `showMarks = input...(true, "عرض العلامات", group = grp10, tooltip = "يعرض علامات الشراء والبيع.")`

## 2. المؤشرات المستخدمة


## 3. شروط الدخول (Long/Short)

```
strategy.entry("شراء FVG INV", strategy.long) if shortSignal strategy.entry("بيع FVG INV", strategy.short) longStop = useBreakEven and strategy.position_size > 0 and close >= strategy.position_avg_price + breakEvenAfterPips * pipSize ? strategy.position_avg_price : strategy.position_avg_price - stop
```

## 4. شروط الخروج

```
strategy.exit("خروج شراء FVG INV", "شراء FVG INV", stop = longStop, limit = strategy.position_avg_price + stopLossPips * pipSize * rr) strategy.exit("خروج بيع FVG INV", "بيع FVG INV", stop = shortStop, limit = strategy.position_avg_price - stopLossPips * pipSize * rr) plotshape(showMarks and longSig
```

## 5. المخاطر والعناصر الصعبة في التحويل

- ⚠️ var / حالة محفوظة - قد تحتاج logic معقدة في Python

## 6. معلومات إضافية

- يستخدم `request.security`: False
- يستخدم pivothigh/pivotlow: False
- دعم/مقاومة يدوية محتملة: False
- يستخدم `var`: True
- يدعم Long: True
- يدعم Short: True

## 7. الأعمدة المقترحة في DataFrame

close, open, high, low, volume

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_strategy_05_fvg_inve`
- exit_tag: `exit_pine_strategy_05_fvg_inve`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
