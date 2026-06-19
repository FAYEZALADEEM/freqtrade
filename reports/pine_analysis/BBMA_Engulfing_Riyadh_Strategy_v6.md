# تحليل Pine Script: BBMA_Engulfing_Riyadh_Strategy_v6

**الملف الأصلي:** BBMA_Engulfing_Riyadh_Strategy_v6.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 03:15

## 1. المدخلات (Inputs)

- `tradeSide = input...("شراء وبيع", "اتجاه التداول", options=["شراء وبيع", "شراء فقط", "بيع فقط"], group=groupGeneral)`
- `confirmOnClose = input...(true, "تأكيد الإشارة بعد إغلاق الشمعة", group=groupGeneral)`
- `minBarsBetweenTrades = input...(5, "أقل عدد شموع بين الصفقات", minval=0, group=groupGeneral)`
- `maxZoneAgeBars = input...(30, "إلغاء المنطقة بعد عدد شموع", minval=1, group=groupGeneral)`
- `entryMode = input...("لمس المنطقة", "طريقة تفعيل الدخول", options=["لمس المنطقة", "إغلاق داخل المنطقة"], group=groupGeneral)`
- `accountCapital = input...(10000.0, "رأس المال بالدولار", minval=100, step=100, group=groupRisk)`
- `leverageInfo = input...(400, "الرافعة المالية المرجعية", minval=1, maxval=400, group=groupRisk)`
- `useRiskQty = input...(true, "حساب حجم الصفقة حسب المخاطرة", group=groupRisk)`
- `riskPct = input...(1.0, "نسبة المخاطرة من رأس المال %", minval=0.01, maxval=10, step=0.1, group=groupRisk)`
- `pointValueUsd = input...(10.0, "قيمة النقطة بالدولار", minval=0.01, step=0.1, group=groupRisk)`
- `pricePointSize = input...(0.0001, "حجم النقطة السعرية", minval=0.00000001, step=0.0001, group=groupRisk)`
- `fixedQty = input...(1.0, "حجم ثابت عند تعطيل حساب المخاطرة", minval=0.01, step=0.01, group=groupRisk)`
- `useSessionFilter = input...(false, "تفعيل فلتر الجلسة", group=groupTime)`
- `riyadhSession = input...("0000-2359", "جلسة التداول بتوقيت الرياض", group=groupTime)`
- `bbLen = input...(20, "فترة Bollinger Bands", minval=2, group=groupBB)`
- `bbMult = input...(2.0, "انحراف Bollinger Bands", minval=0.1, step=0.1, group=groupBB)`
- `emaLen = input...(50, "فترة EMA 50 / BBMA", minval=2, group=groupBB)`
- `squeezeLookback = input...(20, "فترة قياس BB Squeeze", minval=5, group=groupBB)`
- `squeezeFactor = input...(0.70, "حساسية BB Squeeze", minval=0.1, maxval=2.0, step=0.05, group=groupBB)`
- `squeezeValidBars = input...(8, "صلاحية الاختراق بعد BB Squeeze", minval=1, group=groupBB)`
- `useEmaBias = input...(false, "تفعيل فلتر الاتجاه بواسطة EMA 50", group=groupBB)`
- `engulfMode = input...("ابتلاع جسم الشمعة السابقة", "تعريف Engulfing البرمجي", options=["ابتلاع جسم الشمعة السابقة", "كسر قمة/قاع الشمعة السابقة"], group=groupEngulf)`
- `zoneSource = input...("جسم شمعة Engulfing", "مصدر حدود المنطقة", options=["جسم شمعة Engulfing", "كامل شمعة Engulfing"], group=groupEngulf)`
- `zonePaddingTicks = input...(2, "هامش المنطقة بعدد Tick", minval=0, group=groupEngulf)`
- `invalidateOnCloseOutside = input...(true, "إلغاء المنطقة عند إغلاق السعر خارجها عكس الاتجاه", group=groupEngulf)`
- `setupMode = input...("كل النماذج", "النموذج المستخدم", options=["كل النماذج", "BB Squeeze", "BB Extreme A", "BB Extreme B", "BB Rejection A", "BB Rejection B", "BB Rejection C"], group=groupModels)`
- `slMode = input...("خارج منطقة Engulfing", "طريقة وقف الخسارة", options=["خارج منطقة Engulfing", "ATR", "نسبة مئوية"], group=groupExit)`
- `atrLen = input...(14, "فترة ATR", minval=1, group=groupExit)`
- `atrMult = input...(1.5, "مضاعف ATR للوقف", minval=0.1, step=0.1, group=groupExit)`
- `slPercent = input...(0.5, "وقف خسارة بالنسبة المئوية", minval=0.01, step=0.05, group=groupExit)`
- `riskReward = input...(2.0, "نسبة العائد إلى المخاطرة", minval=0.1, step=0.1, group=groupExit)`
- `closeOnOpposite = input...(true, "إغلاق الصفقة عند ظهور إشارة عكسية", group=groupExit)`

## 2. المؤشرات المستخدمة

- ta.sma
- ta.stdev
- ta.ema
- ta.atr
- ta.barssince
- sma
- ema
- atr

## 3. شروط الدخول (Long/Short)

```
strategy.entry("شراء", strategy.long, qty=qty, comment="شراء BBMA") activeLongStop := stopPrice activeLongTarget := targetPrice lastTradeBar := bar_index pendingLong := false if shortEntrySignal entryPrice = close stopPrice = calcShortStop(entryPrice) riskDistance = stopPrice - entryPrice if riskDis
```

## 4. شروط الخروج

```
strategy.exit("خروج شراء", "شراء", stop=activeLongStop, limit=activeLongTarget, comment="SL/TP شراء") if strategy.position_size < 0 strategy.exit("خروج بيع", "بيع", stop=activeShortStop, limit=activeShortTarget, comment="SL/TP بيع") if strategy.position_size == 0 and not longEntrySignal and not shor
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

low, atr, open, high, volume, close

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_bbma_engulfing_riyad`
- exit_tag: `exit_pine_bbma_engulfing_riyad`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
