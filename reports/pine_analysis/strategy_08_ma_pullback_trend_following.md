# تحليل Pine Script: strategy_08_ma_pullback_trend_following

**الملف الأصلي:** strategy_08_ma_pullback_trend_following.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 06:45

## 1. المدخلات (Inputs)

- `pipSize = input...(0.0001, "حجم النقطة", step = 0.00001, group = grp01, tooltip = "حجم النقطة المستخدم في حساب الوقف والهدف.")`
- `enableLong = input...(true, "تفعيل الشراء", group = grp02, tooltip = "يسمح بصفقات الشراء مع الاتجاه الصاعد.")`
- `enableShort = input...(true, "تفعيل البيع", group = grp02, tooltip = "يسمح بصفقات البيع مع الاتجاه الهابط.")`
- `fastEmaLen = input...(50, "EMA السحب", minval = 1, maxval = 300, group = grp03, tooltip = "المتوسط الذي ينتظر السعر الرجوع إليه للدخول.")`
- `slowEmaLen = input...(200, "EMA الاتجاه", minval = 1, maxval = 500, group = grp03, tooltip = "المتوسط الذي يحدد اتجاه التداول العام.")`
- `trailEmaLen = input...(20, "EMA التتبع", minval = 1, maxval = 200, group = grp03, tooltip = "متوسط اختياري لمراقبة الخروج أو تتبع الاتجاه بصرياً.")`
- `rsiLen = input...(14, "طول RSI", minval = 1, maxval = 100, group = grp04, tooltip = "طول RSI المستخدم في فلتر منطقة 40-60.")`
- `adxLen = input...(14, "طول ADX", minval = 1, maxval = 100, group = grp04, tooltip = "طول ADX المستخدم لتجنب السوق المتذبذب.")`
- `adxMin = input...(20.0, "أدنى ADX", minval = 1.0, step = 0.5, group = grp04, tooltip = "إذا كان ADX أقل من هذه القيمة يتم تجاهل الإشارة.")`
- `stopLossPips = input...(20.0, "وقف الخسارة بالنقاط", minval = 1.0, group = grp06, tooltip = "مسافة وقف الخسارة الافتراضية بالنقاط.")`
- `rr = input...(2.0, "نسبة الهدف إلى المخاطرة", minval = 0.5, step = 0.1, group = grp06, tooltip = "الهدف كنسبة من المخاطرة.")`
- `useBreakEven = input...(false, "تفعيل التعادل", group = grp07, tooltip = "ينقل الوقف إلى الدخول بعد ربح محدد.")`
- `breakEvenAfterPips = input...(15.0, "تفعيل التعادل بعد", minval = 1.0, group = grp07, tooltip = "عدد النقاط المطلوبة قبل التعادل.")`
- `useSessionFilter = input...(false, "تفعيل فلتر الجلسة", group = grp09, tooltip = "فلتر الجلسة معطل افتراضياً.")`
- `tradeSession = input...("0000-2359", "وقت الجلسة", group = grp09, tooltip = "وقت التداول عند تفعيل فلتر الجلسة.")`
- `showMarks = input...(true, "عرض العلامات", group = grp10, tooltip = "يعرض علامات الدخول على الشارت.")`

## 2. المؤشرات المستخدمة

- ta.ema
- ta.rsi
- ta.dmi
- ema
- rsi

## 3. شروط الدخول (Long/Short)

```
strategy.entry("شراء MA Pullback", strategy.long) if shortSignal strategy.entry("بيع MA Pullback", strategy.short) longStop = useBreakEven and strategy.position_size > 0 and close >= strategy.position_avg_price + breakEvenAfterPips * pipSize ? strategy.position_avg_price : strategy.position_avg_pric
```

## 4. شروط الخروج

```
strategy.exit("خروج شراء MA Pullback", "شراء MA Pullback", stop = longStop, limit = strategy.position_avg_price + stopLossPips * pipSize * rr) strategy.exit("خروج بيع MA Pullback", "بيع MA Pullback", stop = shortStop, limit = strategy.position_avg_price - stopLossPips * pipSize * rr) plot(ema50, "EM
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

close, open, low, high, volume

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_strategy_08_ma_pullb`
- exit_tag: `exit_pine_strategy_08_ma_pullb`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
