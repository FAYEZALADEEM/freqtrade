# تحليل Pine Script: strategy_04_smc_order_block_bos

**الملف الأصلي:** strategy_04_smc_order_block_bos.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 03:32

## 1. المدخلات (Inputs)

- `pipSize = input...(0.0001, "حجم النقطة", step = 0.00001, group = grp01, tooltip = "حجم النقطة المستخدم في حساب الوقف والهدف.")`
- `enableLong = input...(true, "تفعيل الشراء", group = grp02, tooltip = "يسمح بصفقات الشراء.")`
- `enableShort = input...(true, "تفعيل البيع", group = grp02, tooltip = "يسمح بصفقات البيع.")`
- `pivotLen = input...(5, "طول BOS", minval = 2, maxval = 50, group = grp03, tooltip = "عدد الشموع لاكتشاف القمم والقيعان المستخدمة في BOS.")`
- `maxRetestBars = input...(30, "أقصى شموع لإعادة اختبار OB", minval = 1, maxval = 200, group = grp03, tooltip = "يلغي منطقة OB إذا لم تعد لها الأسعار خلال هذا العدد من الشموع.")`
- `useFvgConfirm = input...(false, "تأكيد FVG", group = grp04, tooltip = "يشترط وجود FVG مع BOS لزيادة الانتقائية.")`
- `stopLossPips = input...(20.0, "وقف الخسارة بالنقاط", minval = 1.0, group = grp06, tooltip = "وقف احتياطي عند عدم استخدام حدود OB.")`
- `bufferPips = input...(1.0, "هامش خلف OB", minval = 0.0, group = grp06, tooltip = "هامش إضافي خلف قاع/قمة OB بالنقاط.")`
- `rr = input...(2.0, "نسبة الهدف إلى المخاطرة", minval = 0.5, step = 0.1, group = grp06, tooltip = "مضاعف الهدف مقابل المخاطرة.")`
- `useBreakEven = input...(false, "تفعيل التعادل", group = grp07, tooltip = "ينقل وقف الخسارة إلى الدخول بعد حركة ربح محددة.")`
- `breakEvenAfterPips = input...(15.0, "تفعيل التعادل بعد", minval = 1.0, group = grp07, tooltip = "عدد النقاط المطلوبة لتفعيل التعادل.")`
- `useSessionFilter = input...(false, "تفعيل فلتر الجلسة", group = grp09, tooltip = "فلتر الجلسة معطل افتراضياً.")`
- `tradeSession = input...("0000-2359", "وقت الجلسة", group = grp09, tooltip = "وقت التداول المسموح عند تفعيل فلتر الجلسة.")`
- `showMarks = input...(true, "عرض العلامات", group = grp10, tooltip = "يعرض علامات الإشارات.")`

## 2. المؤشرات المستخدمة

- ta.pivothigh
- ta.pivotlow
- ta.valuewhen

## 3. شروط الدخول (Long/Short)

```
strategy.entry("شراء OB BOS", strategy.long) if shortSignal strategy.entry("بيع OB BOS", strategy.short) longRisk = math.max(stopLossPips * pipSize, strategy.position_avg_price - nz(bullObLo, strategy.position_avg_price - stopLossPips * pipSize) + bufferPips * pipSize) shortRisk = math.max(stopLossP
```

## 4. شروط الخروج

```
strategy.exit("خروج شراء OB BOS", "شراء OB BOS", stop = longStop, limit = strategy.position_avg_price + longRisk * rr) strategy.exit("خروج بيع OB BOS", "بيع OB BOS", stop = shortStop, limit = strategy.position_avg_price - shortRisk * rr) plotshape(showMarks and longSignal, title = "إشارة شراء", styl
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

high, close, open, volume, low, pivot_high, pivot_low

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_strategy_04_smc_orde`
- exit_tag: `exit_pine_strategy_04_smc_orde`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
