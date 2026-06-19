# تحليل Pine Script: strategy_01_crt_thick_candle_break

**اسم الاستراتيجية:** 01 - CRT Thick Candle Break  
**الملف الأصلي:** strategy_01_crt_thick_candle_break.pine  
**الإصدار:** Pine v6  
**نوع الاستراتيجية:** Reversal + Liquidity Sweep Breakout (CRT)  
**تاريخ التحليل:** 2026-06-19  

## 1. اسم الاستراتيجية
strategy_01_crt_thick_candle_break

## 2. نوعها
- Reversal (انعكاس بعد كسر السيولة)
- Liquidity Sweep + Thick Candle Breakout
- مناسبة للسوق الجانبي/المتذبذب مع حركة قوية بعد كسر الـ liquidity

## 3. الفريم المناسب
15m (كما في متطلبات المشروع). تعمل أيضًا على 5m أو 30m لكن الإعدادات (pivotLen=5, atr=14) تتناسب جيدًا مع 15m.

## 4. هل تستخدم إطار أعلى
**لا**. لا يوجد `request.security` على الإطلاق. كل الحسابات على الفريم الأساسي.

## 5. كل inputs
- `pipSize = 0.0001` (حجم النقطة لـ EURUSD)
- `enableLong = true`
- `enableShort = true`
- `pivotLen = 5` (طول للـ pivothigh/pivotlow)
- `atrLen = 14`
- `thickAtrMult = 0.8` (الجسم > ATR * 0.8)
- `stopLossPips = 20.0`
- `rr = 2.0`
- `useBreakEven = false`
- `breakEvenAfterPips = 15.0`
- `useSessionFilter = false` (معطل افتراضيًا)
- `tradeSession = "0000-2359"`
- `showMarks = true`

## 6. كل indicators
- `ta.pivothigh(high, pivotLen, pivotLen)`
- `ta.pivotlow(low, pivotLen, pivotLen)`
- `ta.valuewhen(...)` للحصول على آخر قمة/قاع مؤكد
- `ta.atr(atrLen)`
- حسابات يدوية: `body = math.abs(close - open)`

## 7. شروط long
```pine
sweepLow = low < lastLow and thickBear   // thick bear candle تحت الـ pivot low السابق
longSignal = enableLong and inSession and sweepLow[1] and close > math.max(open[1], close[1])
```
- الشمعة السابقة: liquidity sweep للأسفل + thick bear candle
- الشمعة الحالية: إغلاق فوق أعلى سعر/إغلاق الشمعة السابقة (كسر الجسم)

## 8. شروط short
```pine
sweepHigh = high > lastHigh and thickBull
shortSignal = enableShort and inSession and sweepHigh[1] and close < math.min(open[1], close[1])
```
- symmetric للـ short (sweep فوق الـ pivot high + thick bull ثم كسر للأسفل)

## 9. شروط exit
- `strategy.exit(..., stop = longStop, limit = longTarget)`
- نفس الشيء للـ short
- الـ stop يمكن أن يكون dynamic (break even) أو fixed pips من سعر الدخول

## 10. stoploss/target إن وجدت
- **Stoploss**: 
  - أساسي: `stopLossPips * pipSize` من سعر الدخول (احتياطي)
  - أفضل: من قمة/قاع الشمعة (لكن في الكود يستخدم fixed pips)
- **Target**: RR = 2.0 (الهدف = مخاطرة × 2)
- Break Even اختياري بعد 15 pips لصالح الصفقة

## 11. هل يوجد `request.security`
**لا** — لا يستخدم أي إطار زمني أعلى.

## 12. هل يوجد `var` أو phase logic
**لا**. لا يوجد `var`. المنطق stateless باستخدام `ta.valuewhen` ومصفوفات [1].

## 13. هل يوجد دعم/مقاومة يدوي
**لا**. يستخدم فقط `pivothigh`/`pivotlow` المؤكدة لاكتشاف مناطق السيولة (lastHigh / lastLow).

## 14. طريقة تحويل الدعم/المقاومة اليدوية إلى آلية
- الـ "lastHigh" و "lastLow" هما دعم/مقاومة ديناميكية من pivots مؤكدة.
- في Python:
  - `df['pivot_high'] = df['high'].rolling(window=2*pivotLen+1, min_periods=...).apply(lambda x: x.iloc[pivotLen] if ... )` أو استخدم `ta.pivothigh` من pandas-ta أو تنفيذ يدوي.
  - أفضل: استخدم `df['ph'] = ta.pivothigh(df['high'], pivotLen, pivotLen)`
  - `df['last_ph'] = df['ph'].ffill()` أو `df['last_ph'] = df['ph'].shift(pivotLen)` مع تأكيد.
  - أضف ATR tolerance: الـ sweep يكون valid إذا كسر بـ ATR * mult.

## 15. مخاطر lookahead
- **منخفضة جداً**.
- يستخدم `[1]` للـ sweep (الشمعة السابقة).
- `ta.pivothigh` و `ta.pivotlow` في Pine تكون مؤكدة فقط بعد `pivotLen` شمعات (لا repaint).
- لا يوجد `shift(-n)` أو `barstate.islast` أو أي وصول مستقبلي.
- يجب في Python استخدام `shift(1)` فقط وتجنب أي حساب يعتمد على بيانات غير مكتملة.

## 16. الأعمدة المطلوبة في DataFrame
- `open`, `high`, `low`, `close`, `volume`
- `atr` (ta.ATR)
- `pivot_high` (ta.pivothigh)
- `pivot_low` (ta.pivotlow)
- `last_pivot_high` / `last_pivot_low` (valuewhen أو ffill بعد التأكيد)
- `body` = abs(close - open)
- `thick_bull` / `thick_bear`

## 17. enter_tag المقترح
- `crt_thick_sweep_long`
- `crt_thick_sweep_short`

## 18. exit_tag المقترح
- `rr_target` (للـ limit)
- `sl_pips` أو `sl_pivot`
- `break_even` (إذا تم تفعيله)

## 19. هل تصلح كنسخة Freqtrade عادية
**نعم بقوة**. 
- قواعد واضحة وقابلة للترجمة إلى `populate_entry_trend` و `populate_exit_trend`.
- يمكن استخدام `can_short = True`.
- ROI و stoploss يمكن تعريفهما أو استخدام custom.
- عدد إشارات معقول إذا كان هناك سيولة كافية.

## 20. هل تصلح لاحقًا لـ FreqAI
**نعم ممتازة**.
- يمكن تحويل المؤشرات إلى features تبدأ بـ `%`:
  - `%body_atr_ratio`
  - `%dist_to_last_pivot_low`
  - `%thick_candle_flag`
  - `%sweep_strength` (volume + body)
- الـ targets يمكن أن تكون توقع الاتجاه بعد الـ sweep أو RR.
- مناسبة لـ classification أو regression model لتحسين الدخول.

---

**ملاحظات إضافية للتحويل:**
- الاستراتيجية تعتمد بشكل أساسي على تأكيد الـ pivot + thick candle بعد sweep.
- في Freqtrade: يجب حساب الـ pivots مع `min_periods` كافية لتجنب NaN في البداية.
- يُفضل إضافة `volume > 0` وفلتر بسيط إذا لزم.
- يمكن جعل الـ stop أفضل باستخدام الـ actual pivot high/low بدلاً من fixed pips.

**التوصية:** هذه استراتيجية ممتازة للبدء. قواعدها نظيفة وقليلة المخاطر.
