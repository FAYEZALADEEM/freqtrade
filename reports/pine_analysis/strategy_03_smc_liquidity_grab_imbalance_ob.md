# تحليل Pine Script: strategy_03_smc_liquidity_grab_imbalance_ob

**الملف الأصلي:** strategy_03_smc_liquidity_grab_imbalance_ob.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 03:31

## 1. المدخلات (Inputs)

- `pipSize = input...(0.0001, "حجم النقطة", step = 0.00001, group = grp01, tooltip = "حجم النقطة المستخدم في حساب الوقف والهدف.")`
- `enableLong = input...(true, "تفعيل الشراء", group = grp02, tooltip = "يسمح بفتح صفقات شراء.")`
- `enableShort = input...(true, "تفعيل البيع", group = grp02, tooltip = "يسمح بفتح صفقات بيع.")`
- `pivotLen = input...(5, "طول مناطق السيولة", minval = 2, maxval = 50, group = grp03, tooltip = "يحدد القمم والقيعان المستخدمة لرصد liquidity grab.")`
- `atrLen = input...(14, "طول ATR", minval = 1, maxval = 100, group = grp03, tooltip = "يستخدم لقياس الاندفاع وحساب وقف ATR.")`
- `impulseMult = input...(1.0, "معامل شمعة الاندفاع", minval = 0.1, step = 0.1, group = grp03, tooltip = "يجب أن يكون جسم شمعة الاندفاع أكبر من ATR مضروبًا في هذا الرقم.")`
- `useTrendFilter = input...(true, "تفعيل فلتر الاتجاه", group = grp04, tooltip = "يستخدم EMA لتقدير اتجاه أعلى بدلاً من structure mapping اليدوي.")`
- `trendLen = input...(100, "طول EMA للاتجاه", minval = 1, maxval = 500, group = grp04, tooltip = "طول EMA المستخدم لفلترة الاتجاه العام.")`
- `stopLossPips = input...(20.0, "وقف الخسارة بالنقاط", minval = 1.0, group = grp06, tooltip = "وقف احتياطي إذا لم يتم استخدام ATR.")`
- `atrStopMult = input...(0.5, "مضاعف ATR للوقف", minval = 0.1, step = 0.1, group = grp06, tooltip = "ورد في التقرير استخدام 0.5 ATR خلف الحركة.")`
- `rr = input...(2.0, "نسبة الهدف إلى المخاطرة", minval = 0.5, step = 0.1, group = grp06, tooltip = "مضاعف الهدف مقابل المخاطرة.")`
- `useBreakEven = input...(false, "تفعيل التعادل", group = grp07, tooltip = "ينقل الوقف إلى نقطة الدخول بعد تحرك السعر لصالح الصفقة.")`
- `breakEvenAfterPips = input...(15.0, "تفعيل التعادل بعد", minval = 1.0, group = grp07, tooltip = "عدد النقاط المطلوبة قبل نقل الوقف للتعادل.")`
- `useSessionFilter = input...(false, "تفعيل فلتر الجلسة", group = grp09, tooltip = "فلتر الجلسة معطل افتراضياً.")`
- `tradeSession = input...("0000-2359", "وقت الجلسة", group = grp09, tooltip = "الفترة الزمنية المسموحة عند تفعيل فلتر الجلسة.")`
- `showMarks = input...(true, "عرض العلامات", group = grp10, tooltip = "يعرض علامات الشراء والبيع.")`

## 2. المؤشرات المستخدمة

- ta.ema
- ta.atr
- ta.pivothigh
- ta.pivotlow
- ta.valuewhen
- ema
- atr

## 3. شروط الدخول (Long/Short)

```
strategy.entry("شراء SMC Grab", strategy.long) if shortSignal strategy.entry("بيع SMC Grab", strategy.short) baseRisk = math.max(stopLossPips * pipSize, atr * atrStopMult) longStop = useBreakEven and strategy.position_size > 0 and close >= strategy.position_avg_price + breakEvenAfterPips * pipSize ?
```

## 4. شروط الخروج

```
strategy.exit("خروج شراء SMC Grab", "شراء SMC Grab", stop = longStop, limit = strategy.position_avg_price + baseRisk * rr) strategy.exit("خروج بيع SMC Grab", "بيع SMC Grab", stop = shortStop, limit = strategy.position_avg_price - baseRisk * rr) plotshape(showMarks and longSignal, title = "إشارة شراء
```

## 5. المخاطر والعناصر الصعبة في التحويل

- لا توجد مخاطر واضحة في التحليل الآلي.

## 6. معلومات إضافية

- يستخدم `request.security`: False
- يستخدم pivothigh/pivotlow: True
- دعم/مقاومة يدوية محتملة: False
- يستخدم `var`: False
- يدعم Long: True
- يدعم Short: True

## 7. الأعمدة المقترحة في DataFrame

volume, atr, pivot_high, open, pivot_low, high, low, close

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_strategy_03_smc_liqu`
- exit_tag: `exit_pine_strategy_03_smc_liqu`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
