# تحليل Pine Script: strategy_02_ict_silver_bullet_liquidity_sweep_fvg

**الملف الأصلي:** strategy_02_ict_silver_bullet_liquidity_sweep_fvg.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 03:28

## 1. المدخلات (Inputs)

- `pipSize = input...(0.0001, "حجم النقطة", step = 0.00001, group = grp01, tooltip = "حجم النقطة المستخدم في حساب الوقف والهدف.")`
- `enableLong = input...(true, "تفعيل الشراء", group = grp02, tooltip = "يسمح بصفقات الشراء عند ظهور إشارة صاعدة.")`
- `enableShort = input...(true, "تفعيل البيع", group = grp02, tooltip = "يسمح بصفقات البيع عند ظهور إشارة هابطة.")`
- `pivotLen = input...(5, "طول سيولة القمم والقيعان", minval = 2, maxval = 50, group = grp03, tooltip = "يحدد القمم والقيعان التي تعتبر مناطق سيولة للسحب.")`
- `maxRetestBars = input...(20, "أقصى عدد شموع لإعادة اختبار FVG", minval = 1, maxval = 200, group = grp03, tooltip = "عدد الشموع المسموح بها بين تكوّن FVG وعودة السعر إليه.")`
- `useBias = input...(false, "تفعيل فلتر EMA للانحياز", group = grp04, tooltip = "عند التفعيل يتم فلترة الشراء أعلى EMA والبيع أسفل EMA.")`
- `biasEmaLen = input...(50, "طول EMA للانحياز", minval = 1, maxval = 300, group = grp04, tooltip = "طول المتوسط المستخدم كبديل برمجي مبسط للـDaily Bias.")`
- `stopLossPips = input...(20.0, "وقف الخسارة بالنقاط", minval = 1.0, group = grp06, tooltip = "مسافة الوقف الافتراضية بالنقاط.")`
- `rr = input...(3.0, "نسبة الهدف إلى المخاطرة", minval = 0.5, step = 0.1, group = grp06, tooltip = "الملف ذكر حدًا أدنى 1:3 لهذه الاستراتيجية.")`
- `useBreakEven = input...(false, "تفعيل التعادل", group = grp07, tooltip = "ينقل الوقف إلى نقطة الدخول بعد تحقق حركة ربح محددة.")`
- `breakEvenAfterPips = input...(15.0, "تفعيل التعادل بعد", minval = 1.0, group = grp07, tooltip = "عدد النقاط المطلوبة قبل تفعيل التعادل.")`
- `useSessionFilter = input...(false, "تفعيل فلتر الجلسة", group = grp09, tooltip = "فلتر الجلسة معطل افتراضياً كما هو مطلوب.")`
- `tradeSession = input...("1000-1100", "وقت Silver Bullet", group = grp09, tooltip = "نافذة Silver Bullet المقترحة؛ لا تعمل إلا عند تفعيل فلتر الجلسة.")`
- `showMarks = input...(true, "عرض العلامات", group = grp10, tooltip = "يعرض علامات الإشارات على الشارت.")`

## 2. المؤشرات المستخدمة

- ta.ema
- ta.pivothigh
- ta.pivotlow
- ta.valuewhen
- ema

## 3. شروط الدخول (Long/Short)

```
strategy.entry("شراء Silver", strategy.long) if shortSignal strategy.entry("بيع Silver", strategy.short) longStop = (useBreakEven and strategy.position_size > 0 and close >= strategy.position_avg_price + breakEvenAfterPips * pipSize) ? strategy.position_avg_price : strategy.position_avg_price - stop
```

## 4. شروط الخروج

```
strategy.exit("خروج شراء Silver", "شراء Silver", stop = longStop, limit = strategy.position_avg_price + stopLossPips * pipSize * rr) strategy.exit("خروج بيع Silver", "بيع Silver", stop = shortStop, limit = strategy.position_avg_price - stopLossPips * pipSize * rr) plotshape(showMarks and longSignal,
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

volume, close, open, pivot_low, low, pivot_high, high

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_strategy_02_ict_silv`
- exit_tag: `exit_pine_strategy_02_ict_silv`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
