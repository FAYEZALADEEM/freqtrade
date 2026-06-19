# تحليل Pine Script: LIB-STR051

**الملف الأصلي:** LIB-STR051.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 06:41

## 1. المدخلات (Inputs)

- `enableLong = input...(true, "Enable Long / تفعيل الشراء")`
- `enableShort = input...(true, "Enable Short / تفعيل البيع")`
- `minBarsBetweenSignals = input...(5, "Minimum bars between signals / حد أدنى بين الإشارات", minval=0)`
- `useOptionalExit = input...(false, "Use optional inferred exit / استخدام خروج اختياري مستنتج")`
- `useOptionalSLTP = input...(false, "Use optional inferred SL/TP / استخدام وقف وهدف اختياري مستنتج")`
- `slPercent = input...(1.0, "Optional SL % / نسبة وقف اختيارية", minval=0.1, step=0.1)`
- `tpPercent = input...(2.0, "Optional TP % / نسبة هدف اختيارية", minval=0.1, step=0.1)`
- `liquidityLookback = input...(20, "Liquidity Lookback / نافذة السيولة", minval=5)`
- `structureLookback = input...(20, "Structure Lookback / نافذة الهيكل", minval=5)`

## 2. المؤشرات المستخدمة

- ta.highest
- ta.lowest

## 3. شروط الدخول (Long/Short)

```
strategy.entry("Long", strategy.long) lastLongSignalBar := bar_index if sellCondition strategy.entry("Short", strategy.short) lastShortSignalBar := bar_index // 11. Plots and alerts / الرسوم والتنبيهات plotshape(buyCondition, title="Buy", style=shape.triangleup, location=location.belowbar, color=col
```

## 4. شروط الخروج

```
strategy.exit("L-Opt-SLTP", "Long", stop=strategy.position_avg_price * (1 - slPercent / 100.0), limit=strategy.position_avg_price * (1 + tpPercent / 100.0)) if useOptionalSLTP and strategy.position_size < 0 strategy.exit("S-Opt-SLTP", "Short", stop=strategy.position_avg_price * (1 + slPercent / 100.
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

high, volume, open, close, low

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_lib-str051`
- exit_tag: `exit_pine_lib-str051`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
