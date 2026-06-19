# تحليل Pine Script: strategy_12_rsi_divergence_reversal

**الملف الأصلي:** strategy_12_rsi_divergence_reversal.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 04:28

## 1. المدخلات (Inputs)

- `pipSize = input...(0.0001, "حجم النقطة", step = 0.00001, group = grp01, tooltip = "حجم النقطة المستخدم في حساب الوقف والهدف.")`
- `enableLong = input...(true, "تفعيل الشراء", group = grp02, tooltip = "يسمح بإشارات الشراء بعد bullish divergence.")`
- `enableShort = input...(true, "تفعيل البيع", group = grp02, tooltip = "يسمح بإشارات البيع بعد bearish divergence.")`
- `rsiLen = input...(14, "طول RSI", minval = 1, maxval = 100, group = grp03, tooltip = "طول RSI المستخدم للديفرجنس.")`
- `pivotLen = input...(5, "طول Pivot", minval = 2, maxval = 50, group = grp03, tooltip = "عدد الشموع لتأكيد قاع أو قمة الديفرجنس.")`
- `oversold = input...(30.0, "مستوى التشبع البيعي", minval = 1.0, maxval = 50.0, group = grp03, tooltip = "يجب أن يكون RSI حول هذا المستوى للشراء.")`
- `overbought = input...(70.0, "مستوى التشبع الشرائي", minval = 50.0, maxval = 99.0, group = grp03, tooltip = "يجب أن يكون RSI حول هذا المستوى للبيع.")`
- `requireChoch = input...(true, "اشتراط CHoCH مبسط", group = grp04, tooltip = "يشترط كسر pivot معاكس بعد الديفرجنس لتأكيد تغير الاتجاه.")`
- `stopLossPips = input...(20.0, "وقف الخسارة بالنقاط", minval = 1.0, group = grp06, tooltip = "وقف الخسارة الافتراضي لأن التقرير لم يذكر وقفًا محددًا.")`
- `rr = input...(2.0, "نسبة الهدف إلى المخاطرة", minval = 0.5, step = 0.1, group = grp06, tooltip = "مضاعف الهدف مقابل المخاطرة.")`
- `useBreakEven = input...(false, "تفعيل التعادل", group = grp07, tooltip = "ينقل الوقف إلى الدخول بعد حركة ربح محددة.")`
- `breakEvenAfterPips = input...(15.0, "تفعيل التعادل بعد", minval = 1.0, group = grp07, tooltip = "عدد النقاط المطلوبة قبل التعادل.")`
- `useSessionFilter = input...(false, "تفعيل فلتر الجلسة", group = grp09, tooltip = "فلتر الجلسة معطل افتراضياً.")`
- `tradeSession = input...("0000-2359", "وقت الجلسة", group = grp09, tooltip = "وقت التداول عند تفعيل فلتر الجلسة.")`
- `showMarks = input...(true, "عرض العلامات", group = grp10, tooltip = "يعرض علامات الدخول على الشارت.")`

## 2. المؤشرات المستخدمة

- ta.rsi
- ta.pivotlow
- ta.pivothigh
- ta.valuewhen
- rsi

## 3. شروط الدخول (Long/Short)

```
strategy.entry("شراء RSI Div", strategy.long) bullDivActive := false if shortSignal strategy.entry("بيع RSI Div", strategy.short) bearDivActive := false longStop = useBreakEven and strategy.position_size > 0 and close >= strategy.position_avg_price + breakEvenAfterPips * pipSize ? strategy.position_
```

## 4. شروط الخروج

```
strategy.exit("خروج شراء RSI Div", "شراء RSI Div", stop = longStop, limit = strategy.position_avg_price + stopLossPips * pipSize * rr) strategy.exit("خروج بيع RSI Div", "بيع RSI Div", stop = shortStop, limit = strategy.position_avg_price - stopLossPips * pipSize * rr) plotshape(showMarks and longSig
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

pivot_high, pivot_low, close, high, volume, low, open

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_strategy_12_rsi_dive`
- exit_tag: `exit_pine_strategy_12_rsi_dive`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
