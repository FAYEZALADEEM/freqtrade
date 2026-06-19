# تحليل Pine Script: strategy_11_one_hour_forex_reversal

**الملف الأصلي:** strategy_11_one_hour_forex_reversal.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 06:45

## 1. المدخلات (Inputs)

- `pipSize = input...(0.0001, "حجم النقطة", step = 0.00001, group = grp01, tooltip = "حجم النقطة المستخدم في حساب الوقف والهدف.")`
- `enableLong = input...(true, "تفعيل الشراء", group = grp02, tooltip = "يسمح بالشراء عند شروط oversold العكسية.")`
- `enableShort = input...(true, "تفعيل البيع", group = grp02, tooltip = "يسمح بالبيع حسب القواعد الأصلية المذكورة.")`
- `wmaLen = input...(14, "طول WMA", minval = 1, maxval = 200, group = grp03, tooltip = "طول Weighted Moving Average المذكور في التقرير.")`
- `stochLen = input...(14, "طول Stochastic K", minval = 1, maxval = 100, group = grp03, tooltip = "قيمة K في Stochastic.")`
- `stochD = input...(3, "طول Stochastic D", minval = 1, maxval = 50, group = grp03, tooltip = "قيمة D في Stochastic.")`
- `stochSmooth = input...(3, "تنعيم Stochastic", minval = 1, maxval = 50, group = grp03, tooltip = "قيمة التنعيم في Stochastic.")`
- `psarStart = input...(0.02, "PSAR Start", minval = 0.001, step = 0.001, group = grp03, tooltip = "قيمة البداية في Parabolic SAR.")`
- `psarInc = input...(0.02, "PSAR Increment", minval = 0.001, step = 0.001, group = grp03, tooltip = "قيمة الزيادة في Parabolic SAR.")`
- `psarMax = input...(0.2, "PSAR Max", minval = 0.01, step = 0.01, group = grp03, tooltip = "القيمة القصوى في Parabolic SAR.")`
- `stopLossPips = input...(20.0, "وقف الخسارة بالنقاط", minval = 1.0, group = grp06, tooltip = "وقف الخسارة الافتراضي لأن التقرير لم يذكر وقفًا محددًا.")`
- `rr = input...(2.0, "نسبة الهدف إلى المخاطرة", minval = 0.5, step = 0.1, group = grp06, tooltip = "مضاعف الهدف مقابل الوقف.")`
- `useBreakEven = input...(false, "تفعيل التعادل", group = grp07, tooltip = "ينقل الوقف إلى الدخول بعد ربح محدد.")`
- `breakEvenAfterPips = input...(15.0, "تفعيل التعادل بعد", minval = 1.0, group = grp07, tooltip = "عدد النقاط المطلوبة قبل التعادل.")`
- `useSessionFilter = input...(false, "تفعيل فلتر الجلسة", group = grp09, tooltip = "فلتر الجلسة معطل افتراضياً.")`
- `tradeSession = input...("0000-2359", "وقت الجلسة", group = grp09, tooltip = "وقت التداول عند تفعيل فلتر الجلسة.")`
- `showMarks = input...(true, "عرض العلامات", group = grp10, tooltip = "يعرض إشارات الشراء والبيع.")`

## 2. المؤشرات المستخدمة

- ta.wma
- ta.sar
- ta.stoch
- ta.sma
- stoch
- sma

## 3. شروط الدخول (Long/Short)

```
strategy.entry("شراء 1H Reversal", strategy.long) if shortSignal strategy.entry("بيع 1H Reversal", strategy.short) longStop = useBreakEven and strategy.position_size > 0 and close >= strategy.position_avg_price + breakEvenAfterPips * pipSize ? strategy.position_avg_price : strategy.position_avg_pric
```

## 4. شروط الخروج

```
strategy.exit("خروج شراء 1H Reversal", "شراء 1H Reversal", stop = longStop, limit = strategy.position_avg_price + stopLossPips * pipSize * rr) strategy.exit("خروج بيع 1H Reversal", "بيع 1H Reversal", stop = shortStop, limit = strategy.position_avg_price - stopLossPips * pipSize * rr) plot(wma, "WMA"
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

close, volume, high, open, low

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_strategy_11_one_hour`
- exit_tag: `exit_pine_strategy_11_one_hour`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
