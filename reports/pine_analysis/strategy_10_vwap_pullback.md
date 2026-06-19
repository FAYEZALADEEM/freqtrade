# تحليل Pine Script: strategy_10_vwap_pullback

**الملف الأصلي:** strategy_10_vwap_pullback.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 06:45

## 1. المدخلات (Inputs)

- `pipSize = input...(0.0001, "حجم النقطة", step = 0.00001, group = grp01, tooltip = "حجم النقطة المستخدم في حساب الوقف والهدف.")`
- `enableLong = input...(true, "تفعيل الشراء", group = grp02, tooltip = "يسمح بشراء إعادة اختبار VWAP من الأعلى.")`
- `enableShort = input...(true, "تفعيل البيع", group = grp02, tooltip = "يسمح ببيع إعادة اختبار VWAP من الأسفل.")`
- `awayPips = input...(10.0, "أدنى ابتعاد عن VWAP", minval = 0.1, group = grp03, tooltip = "يجب أن يكون السعر قد ابتعد عن VWAP بهذا المقدار قبل العودة.")`
- `lookbackAway = input...(10, "شموع البحث عن الابتعاد", minval = 1, maxval = 100, group = grp03, tooltip = "عدد الشموع السابقة المستخدمة للتحقق من ابتعاد السعر عن VWAP.")`
- `rvolLen = input...(20, "طول RVOL", minval = 1, maxval = 200, group = grp04, tooltip = "طول متوسط الحجم لحساب حجم نسبي اختياري.")`
- `minRvol = input...(1.0, "أدنى RVOL", minval = 0.1, step = 0.1, group = grp04, tooltip = "أدنى حجم نسبي لقبول الإشارة.")`
- `stopLossPips = input...(15.0, "وقف الخسارة بالنقاط", minval = 1.0, group = grp06, tooltip = "وقف الخسارة خلف VWAP أو نقطة الدخول حسب السوق.")`
- `rr = input...(1.5, "نسبة الهدف إلى المخاطرة", minval = 0.5, step = 0.1, group = grp06, tooltip = "نسبة الهدف إلى المخاطرة.")`
- `useBreakEven = input...(false, "تفعيل التعادل", group = grp07, tooltip = "ينقل الوقف إلى نقطة الدخول بعد حركة ربح محددة.")`
- `breakEvenAfterPips = input...(15.0, "تفعيل التعادل بعد", minval = 1.0, group = grp07, tooltip = "عدد النقاط المطلوبة قبل التعادل.")`
- `useSessionFilter = input...(false, "تفعيل فلتر الجلسة", group = grp09, tooltip = "فلتر الجلسة معطل افتراضياً.")`
- `tradeSession = input...("1100-1400", "وقت تداول VWAP", group = grp09, tooltip = "جلسة مقترحة للاستراتيجية ولا تعمل إلا عند تفعيل الفلتر.")`
- `showMarks = input...(true, "عرض العلامات", group = grp10, tooltip = "يعرض علامات الدخول.")`

## 2. المؤشرات المستخدمة

- ta.vwap
- ta.sma
- ta.highest
- vwap
- sma

## 3. شروط الدخول (Long/Short)

```
strategy.entry("شراء VWAP", strategy.long) if shortSignal strategy.entry("بيع VWAP", strategy.short) longStop = useBreakEven and strategy.position_size > 0 and close >= strategy.position_avg_price + breakEvenAfterPips * pipSize ? strategy.position_avg_price : strategy.position_avg_price - stopLossPi
```

## 4. شروط الخروج

```
strategy.exit("خروج شراء VWAP", "شراء VWAP", stop = longStop, limit = strategy.position_avg_price + stopLossPips * pipSize * rr) strategy.exit("خروج بيع VWAP", "بيع VWAP", stop = shortStop, limit = strategy.position_avg_price - stopLossPips * pipSize * rr) plot(vwap, "VWAP", color = color.purple) pl
```

## 5. المخاطر والعناصر الصعبة في التحويل

- لا توجد مخاطر واضحة في التحليل الآلي.

## 6. معلومات إضافية

- يستخدم `request.security`: False
- يستخدم pivothigh/pivotlow: False
- دعم/مقاومة يدوية محتملة: False
- يستخدم `var`: False
- يدعم Long: True
- يدعم Short: True

## 7. الأعمدة المقترحة في DataFrame

close, open, high, volume, low

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_strategy_10_vwap_pul`
- exit_tag: `exit_pine_strategy_10_vwap_pul`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
