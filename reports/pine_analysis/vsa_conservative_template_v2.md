# تحليل Pine Script: vsa_conservative_template_v2

**الملف الأصلي:** vsa_conservative_template_v2.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 06:50

## 1. المدخلات (Inputs)

- `volLen = input...(20,  "Volume average length")`
- `spreadLen = input...(20,  "Spread average length")`
- `backgroundBars = input...(50,  "Background lookback bars")`
- `newGroundLookback = input...(200, "New ground lookback for End of Rising Market [يتطلب مراجعة]")`
- `riskPct = input...(2.5, "Risk % per trade", step=0.1, minval=0.1)`
- `rrMultiple = input...(3.0, "Reward/Risk multiple", step=0.1, minval=0.1)`
- `entryBufferTicks = input...(1,   "Entry buffer (ticks)`
- `stopBufferTicks = input...(1,   "Stop buffer (ticks)`
- `narrowSpreadFactor = input...(0.9, "Narrow spread factor [يتطلب مراجعة]", step=0.05)`
- `wideSpreadFactor = input...(1.3, "Wide spread factor [يتطلب مراجعة]", step=0.05)`
- `ultraVolFactor = input...(1.5, "Ultra volume factor [يتطلب مراجعة]", step=0.05)`
- `nearHighFrac = input...(0.70,"Close near high fraction [يتطلب مراجعة]", step=0.05, minval=0.5, maxval=1.0)`
- `nearLowFrac = input...(0.30,"Close near low fraction [يتطلب مراجعة]", step=0.05, minval=0.0, maxval=0.5)`
- `midTolerance = input...(0.25,"Mid-close tolerance [يتطلب مراجعة]", step=0.01, minval=0.01, maxval=0.49)`
- `entryMode = input...("Market on confirmation", "Entry mode", options=["Market on confirmation", "Stop above/below signal"])`
- `useBackgroundFilter = input...(true,  "Require recent background strength/weakness")`
- `useTrendFilter = input...(true,  "Use EMA trend filter [تقريب]")`
- `useAboveStrength = input...(false, "Require close above Shake-out high for longs")`
- `allowLongs = input...(true,  "Allow Longs")`
- `allowShorts = input...(true,  "Allow Shorts")`
- `emaFastLen = input...(20, "EMA fast [تقريب]", minval=1)`
- `emaSlowLen = input...(50, "EMA slow [تقريب]", minval=1)`

## 2. المؤشرات المستخدمة

- ta.sma
- ta.ema
- ta.highest
- ta.valuewhen
- ta.barssince
- sma
- ema

## 3. شروط الدخول (Long/Short)

```
strategy.entry("Long", strategy.long, qty=qty) else strategy.entry("Long", strategy.long, qty=qty, stop=entryPrice) strategy.exit("Long Exit", from_entry="Long", stop=stopPrice, limit=entryPrice + (entryPrice - stopPrice) * rrMultiple) // --------------------------- // Build/submit Short // --------
```

## 4. شروط الخروج

```
strategy.exit("Long Exit", from_entry="Long", stop=stopPrice, limit=entryPrice + (entryPrice - stopPrice) * rrMultiple) // --------------------------- // Build/submit Short // --------------------------- if strategy.position_size == 0 and allowShorts and noDemandConfirmed and shortContextOk and not 
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

close, high, open, low, volume

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_vsa_conservative_tem`
- exit_tag: `exit_pine_vsa_conservative_tem`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
