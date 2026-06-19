# تحليل Pine Script: LIB-STR027_Volume_Fib_EMA_Manual_Test_v6

**الملف الأصلي:** LIB-STR027_Volume_Fib_EMA_Manual_Test_v6.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 06:39

## 1. المدخلات (Inputs)

- `enableLong = input...(true, "Enable long", group=groupCore)`
- `enableShort = input...(true, "Enable short", group=groupCore)`
- `minBarsBetweenSignals = input...(5, "Minimum bars between signals", minval=0, group=groupCore)`
- `fastLen = input...(21, "Fast EMA", minval=2, group=groupCore)`
- `slowLen = input...(55, "Slow EMA", minval=3, group=groupCore)`
- `structureLookback = input...(20, "Structure lookback", minval=5, group=groupCore)`
- `fibLookback = input...(50, "Fibonacci lookback", minval=10, group=groupCore)`
- `minScore = input...(3, "Minimum confluence score", minval=1, maxval=4, group=groupCore)`
- `volLookback = input...(20, "Volume average length", minval=5, group=groupVolume)`
- `volSpikeMult = input...(1.2, "Volume expansion multiplier", minval=0.1, step=0.1, group=groupVolume)`
- `useVwapFilter = input...(true, "Use VWAP side filter", group=groupVolume)`
- `useOptionalExit = input...(false, "Use optional inferred exit", group=groupRisk)`
- `useOptionalSLTP = input...(false, "Use optional inferred SL/TP", group=groupRisk)`
- `slPercent = input...(1.0, "Optional SL %", minval=0.1, step=0.1, group=groupRisk)`
- `tpPercent = input...(2.0, "Optional TP %", minval=0.1, step=0.1, group=groupRisk)`
- `showFib = input...(true, "Show Fibonacci mid", group=groupVisual)`
- `showSignals = input...(true, "Show signals", group=groupVisual)`

## 2. المؤشرات المستخدمة

- ta.ema
- ta.highest
- ta.lowest
- ta.vwap
- ta.sma
- ema
- vwap
- sma

## 3. شروط الدخول (Long/Short)

```
strategy.entry("Long", strategy.long) lastLongSignalBar := bar_index if sellSignal strategy.entry("Short", strategy.short) lastShortSignalBar := bar_index plot(emaFast, "Fast EMA", color=color.new(color.teal, 0)) plot(emaSlow, "Slow EMA", color=color.new(color.orange, 0)) plot(vwapValue, "VWAP", col
```

## 4. شروط الخروج

```
strategy.exit("Long optional SLTP", "Long", stop=strategy.position_avg_price * (1 - slPercent / 100.0), limit=strategy.position_avg_price * (1 + tpPercent / 100.0)) if useOptionalSLTP and strategy.position_size < 0 strategy.exit("Short optional SLTP", "Short", stop=strategy.position_avg_price * (1 +
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

high, low, open, volume, close

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_lib-str027_volume_fi`
- exit_tag: `exit_pine_lib-str027_volume_fi`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
