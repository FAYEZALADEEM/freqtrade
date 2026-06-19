# تحليل Pine Script: CRT_1AM_Strategy_V1_Pine_v6

**الملف الأصلي:** CRT_1AM_Strategy_V1_Pine_v6.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 03:42

## 1. المدخلات (Inputs)

- `tz = input...("GMT-5", "توقيت النموذج — EST ثابت", group = groupMain,
     tooltip = "المصدر ذكر EST. القيمة GMT-5 تثبت التوقيت دون تغيير الصيف/الشتاء.")`
- `direction = input...("الكل", "اتجاه التداول", options = ["الكل", "شراء فقط", "بيع فقط"], group = groupMain)`
- `startDate = input...(timestamp("01 Jan 2023 00:00 +0000")`
- `endDate = input...(timestamp("31 Dec 2030 23:59 +0000")`
- `pipSize = input...(0.0001, "حجم النقطة Pip", step = 0.00001, group = groupRisk,
     tooltip = "EURUSD/GBPUSD غالبًا 0.0001، و USDJPY غالبًا 0.01.")`
- `bufferPips = input...(1.0, "هامش الوقف خلف ذيل السحب — Pips", minval = 0.0, step = 0.5, group = groupRisk)`
- `tp1Percent = input...(50.0, "نسبة الإغلاق عند منتصف النطاق %", minval = 1.0, maxval = 99.0, step = 1.0, group = groupRisk)`
- `closeInsideRequired = input...(true, "يشترط إغلاق ساعة السحب داخل النطاق", group = groupFilter,
     tooltip = "يفعّل تعريفًا قابلًا للاختبار لسحب السيولة ثم العودة للنطاق.")`
- `rejectDoubleSweep = input...(true, "إلغاء اليوم إذا سُحب الطرفان في ساعة 02:00", group = groupFilter,
     tooltip = "لأن اتجاه الصفقة يصبح غير محسوم إذا سُحبت القمة والقاع في نفس ساعة التلاعب.")`
- `showRange = input...(true, "إظهار نطاق CRT", group = groupVisual)`
- `showMarks = input...(true, "إظهار إشارات السحب والدخول", group = groupVisual)`
- `showPanel = input...(true, "إظهار شاشة الأداء", group = groupVisual)`

## 2. المؤشرات المستخدمة


## 3. شروط الدخول (Long/Short)

```
strategy.entry("CRT شراء", strategy.long, comment = "سحب القاع ثم عودة") strategy.exit("شراء TP1", from_entry = "CRT شراء", stop = longStop, limit = rangeMid, qty_percent = tp1Percent) strategy.exit("شراء TP2", from_entry = "CRT شراء", stop = longStop, limit = rangeHigh, qty_percent = 100.0 - tp1Per
```

## 4. شروط الخروج

```
strategy.exit("شراء TP1", from_entry = "CRT شراء", stop = longStop, limit = rangeMid, qty_percent = tp1Percent) strategy.exit("شراء TP2", from_entry = "CRT شراء", stop = longStop, limit = rangeHigh, qty_percent = 100.0 - tp1Percent) if shortSignal float shortStop = purgeHigh + stopBuffer activeHigh 
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

high, close, low, volume, open

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_crt_1am_strategy_v1_`
- exit_tag: `exit_pine_crt_1am_strategy_v1_`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
