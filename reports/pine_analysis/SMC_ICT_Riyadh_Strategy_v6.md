# تحليل Pine Script: SMC_ICT_Riyadh_Strategy_v6

**الملف الأصلي:** SMC_ICT_Riyadh_Strategy_v6.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 03:34

## 1. المدخلات (Inputs)

- `enableLong = input...(true, "تفعيل صفقات الشراء", group="1. الإعدادات العامة")`
- `enableShort = input...(true, "تفعيل صفقات البيع", group="1. الإعدادات العامة")`
- `confirmOnClose = input...(true, "تأكيد الإشارة بعد إغلاق الشمعة", group="1. الإعدادات العامة")`
- `minBarsBetweenSignals = input...(10, "أقل عدد شموع بين الصفقات", minval=0, group="1. الإعدادات العامة")`
- `useSessionFilter = input...(true, "تفعيل فلتر الجلسات بتوقيت الرياض", group="2. فلتر الوقت")`
- `riyadhTimezone = input...("Asia/Riyadh", "المنطقة الزمنية", group="2. فلتر الوقت")`
- `sessionOne = input...("1000-1300", "الجلسة الأولى - الرياض", group="2. فلتر الوقت")`
- `sessionTwo = input...("1530-1800", "الجلسة الثانية - الرياض", group="2. فلتر الوقت")`
- `pivotLeft = input...(3, "شموع يسار القمة/القاع", minval=1, maxval=20, group="3. هيكل السوق")`
- `pivotRight = input...(3, "شموع يمين القمة/القاع", minval=1, maxval=20, group="3. هيكل السوق")`
- `structureLookback = input...(50, "مدى Premium / Discount", minval=10, group="3. هيكل السوق")`
- `usePdFilter = input...(false, "استخدام فلتر Premium / Discount", group="3. هيكل السوق")`
- `liquidityLookback = input...(20, "مدى البحث عن السيولة", minval=5, group="4. السيولة")`
- `sweepValidBars = input...(8, "صلاحية سحب السيولة بالشموع", minval=1, group="4. السيولة")`
- `fvgValidBars = input...(40, "صلاحية FVG بالشموع", minval=5, group="5. FVG")`
- `showFvgBoxes = input...(true, "عرض مناطق FVG", group="5. FVG")`
- `obLookback = input...(20, "البحث عن آخر شمعة معاكسة للـ OB", minval=3, maxval=100, group="6. Order Block")`
- `obValidBars = input...(60, "صلاحية Order Block بالشموع", minval=5, group="6. Order Block")`
- `showObBoxes = input...(true, "عرض مناطق Order Block", group="6. Order Block")`
- `minConfluence = input...(3, "أقل عدد توافقات للدخول", minval=1, maxval=5, group="7. شروط الدخول")`
- `requireStructure = input...(true, "اشتراط BOS أو CHoCH", group="7. شروط الدخول")`
- `requireLiquidity = input...(true, "اشتراط سحب سيولة حديث", group="7. شروط الدخول")`
- `allowFvgEntry = input...(true, "السماح بالدخول من FVG", group="7. شروط الدخول")`
- `allowObEntry = input...(true, "السماح بالدخول من Order Block", group="7. شروط الدخول")`
- `riskPercent = input...(1.0, "نسبة المخاطرة من رأس المال %", minval=0.1, maxval=10, step=0.1, group="8. إدارة المخاطر")`
- `pointValueUsd = input...(10.0, "قيمة النقطة بالدولار", minval=0.01, step=0.01, group="8. إدارة المخاطر")`
- `rr = input...(2.0, "نسبة العائد إلى المخاطرة", minval=0.2, step=0.1, group="8. إدارة المخاطر")`
- `stopMode = input...("خلف السوينغ", "طريقة وقف الخسارة", options=["خلف السوينغ", "خلف OB", "ATR"], group="8. إدارة المخاطر")`
- `atrLength = input...(14, "طول ATR", minval=1, group="8. إدارة المخاطر")`
- `atrMult = input...(1.5, "مضاعف ATR للوقف", minval=0.1, step=0.1, group="8. إدارة المخاطر")`
- `maxQty = input...(100.0, "أقصى حجم صفقة", minval=0.01, step=0.01, group="8. إدارة المخاطر")`
- `showLabels = input...(true, "عرض تسميات BOS / CHoCH", group="9. العرض")`
- `extendBoxes = input...(30, "تمديد المناطق يمينًا", minval=1, group="9. العرض")`

## 2. المؤشرات المستخدمة

- ta.pivothigh
- ta.pivotlow
- ta.highest
- ta.lowest
- ta.barssince
- ta.atr
- atr

## 3. شروط الدخول (Long/Short)

```
strategy.entry("شراء", strategy.long, qty=longQty) lastSignalBar := bar_index if shortSignal activeShortStop := shortStop activeShortTarget := shortTarget activeLongStop := na activeLongTarget := na strategy.entry("بيع", strategy.short, qty=shortQty) lastSignalBar := bar_index if strategy.position_s
```

## 4. شروط الخروج

```
strategy.exit("خروج شراء", "شراء", stop=activeLongStop, limit=activeLongTarget) if strategy.position_size < 0 strategy.exit("خروج بيع", "بيع", stop=activeShortStop, limit=activeShortTarget) if strategy.position_size == 0 and not longSignal and not shortSignal activeLongStop := na activeLongTarget :=
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

atr, pivot_low, high, volume, pivot_high, close, low, open

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_smc_ict_riyadh_strat`
- exit_tag: `exit_pine_smc_ict_riyadh_strat`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
