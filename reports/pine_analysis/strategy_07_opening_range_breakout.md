# تحليل Pine Script: strategy_07_opening_range_breakout

**الملف الأصلي:** strategy_07_opening_range_breakout.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 06:42

## 1. المدخلات (Inputs)

- `pipSize = input...(0.0001, "حجم النقطة", step = 0.00001, group = grp01, tooltip = "حجم النقطة المستخدم في حساب الوقف والهدف.")`
- `enableLong = input...(true, "تفعيل الشراء", group = grp02, tooltip = "يسمح بإشارات الشراء أعلى نطاق الافتتاح.")`
- `enableShort = input...(true, "تفعيل البيع", group = grp02, tooltip = "يسمح بإشارات البيع أسفل نطاق الافتتاح.")`
- `orbSession = input...("0930-0945", "جلسة بناء ORB", group = grp03, tooltip = "الفترة التي يتم خلالها حساب أعلى وأدنى نطاق الافتتاح.")`
- `oneTradePerDay = input...(true, "صفقة واحدة يومياً", group = grp03, tooltip = "يمنع تكرار الدخول بعد أول صفقة في اليوم.")`
- `rvolLen = input...(20, "طول متوسط الحجم", minval = 1, maxval = 200, group = grp04, tooltip = "يستخدم لحساب RVOL مقارنة بمتوسط الحجم.")`
- `rvolMin = input...(1.5, "أدنى RVOL", minval = 0.1, step = 0.1, group = grp04, tooltip = "يشترط أن يكون الحجم النسبي أعلى من هذه القيمة.")`
- `rsiLen = input...(14, "طول RSI", minval = 1, maxval = 100, group = grp04, tooltip = "طول RSI المستخدم لتأكيد اتجاه الاختراق.")`
- `useVwapFilter = input...(true, "تفعيل فلتر VWAP", group = grp04, tooltip = "يشترط أن يكون الشراء أعلى VWAP والبيع أسفل VWAP.")`
- `stopLossPips = input...(20.0, "وقف الخسارة بالنقاط", minval = 1.0, group = grp06, tooltip = "وقف احتياطي إذا كان الطرف المقابل للنطاق غير مناسب.")`
- `rr = input...(1.5, "نسبة الهدف إلى المخاطرة", minval = 0.5, step = 0.1, group = grp06, tooltip = "مضاعف الهدف مقابل الوقف، ويمكن جعله 1 لاستخدام هدف يساوي النطاق.")`
- `useBreakEven = input...(false, "تفعيل التعادل", group = grp07, tooltip = "ينقل الوقف إلى نقطة الدخول بعد تحرك السعر لصالح الصفقة.")`
- `breakEvenAfterPips = input...(15.0, "تفعيل التعادل بعد", minval = 1.0, group = grp07, tooltip = "عدد النقاط المطلوبة قبل نقل الوقف للتعادل.")`
- `useSessionFilter = input...(false, "تفعيل فلتر الجلسة", group = grp09, tooltip = "فلتر إضافي للتداول معطل افتراضياً.")`
- `tradeSession = input...("0930-1200", "وقت التداول بعد ORB", group = grp09, tooltip = "الفترة المسموح فيها بالاختراق إذا تم تفعيل فلتر الجلسة.")`
- `showMarks = input...(true, "عرض العلامات", group = grp10, tooltip = "يعرض إشارات الشراء والبيع على الشارت.")`

## 2. المؤشرات المستخدمة

- ta.change
- ta.rsi
- ta.sma
- ta.vwap
- rsi
- sma
- vwap

## 3. شروط الدخول (Long/Short)

```
strategy.entry("شراء ORB", strategy.long) tradedToday := true if shortSignal strategy.entry("بيع ORB", strategy.short) tradedToday := true risk = math.max(stopLossPips * pipSize, math.abs(orbHigh - orbLow)) longStop = useBreakEven and strategy.position_size > 0 and close >= strategy.position_avg_pri
```

## 4. شروط الخروج

```
strategy.exit("خروج شراء ORB", "شراء ORB", stop = longStop, limit = strategy.position_avg_price + risk * rr) strategy.exit("خروج بيع ORB", "بيع ORB", stop = shortStop, limit = strategy.position_avg_price - risk * rr) plot(orbHigh, "ORB High", color = color.new(color.green, 20)) plot(orbLow, "ORB Low
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

low, volume, open, high, close

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_strategy_07_opening_`
- exit_tag: `exit_pine_strategy_07_opening_`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
