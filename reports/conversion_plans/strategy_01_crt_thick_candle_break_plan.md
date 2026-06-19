# خطة التحويل - strategy_01_crt_thick_candle_break

**التاريخ:** 2026-06-19  
**الاستراتيجية الأصلية:** pine_strategies/strategy_01_crt_thick_candle_break.pine  
**التقرير السابق:** reports/pine_analysis/strategy_01_crt_thick_candle_break.md

## 1. اسم ملف Python المقترح
`user_data/strategies/CRT_ThickCandleBreak.py`

## 2. اسم class
`class CRT_ThickCandleBreak(IStrategy):`

## 3. المؤشرات التي ستُحسب في `populate_indicators`
- `atr` = ta.ATR(timeperiod=atrLen)
- `pivot_high` و `pivot_low` (تنفيذ مؤكد بـ left/right = pivotLen)
- `last_ph` = آخر قمة pivot مؤكدة (باستخدام ffill أو shift مناسب)
- `last_pl` = آخر قاع pivot مؤكدة
- `body` = abs(close - open)
- `thick_bull` = (close > open) & (body > atr * thickAtrMult)
- `thick_bear` = (close < open) & (body > atr * thickAtrMult)
- `sweep_low` = (low < last_pl) & thick_bear
- `sweep_high` = (high > last_ph) & thick_bull
- `in_session` (اختياري، default true بما أن الفلتر معطل)

**ملاحظة:** سيتم تعريف pivotLen, atrLen, thickAtrMult كـ hyperparameters أو ثابتة في البداية.

## 4. شروط `populate_entry_trend`
```python
dataframe.loc[
    (
        dataframe['sweep_low'].shift(1) &
        (dataframe['close'] > dataframe[['open', 'close']].shift(1).max(axis=1)) &
        (dataframe['volume'] > 0)
    ),
    ['enter_long', 'enter_tag']
] = (1, 'crt_sweep_long')

dataframe.loc[
    (
        dataframe['sweep_high'].shift(1) &
        (dataframe['close'] < dataframe[['open', 'close']].shift(1).min(axis=1)) &
        (dataframe['volume'] > 0)
    ),
    ['enter_short', 'enter_tag']
] = (1, 'crt_sweep_short')
```

## 5. شروط `populate_exit_trend`
- في البداية: استخدام ROI + Stoploss فقط (مثل الأصلية).
- يمكن إضافة exit_signal بسيط إذا لزم لاحقاً.
- `use_exit_signal = False` مبدئياً لتجنب التعارض مع SL/TP.

## 6. إعدادات ROI
- بما أن الهدف ديناميكي (RR من سعر الدخول)، سيتم استخدام `custom_exit` للحساب الدقيق.
- تقريبي: 
```python
minimal_roi = {
    "0": 0.004,      # ~ 40 pips إذا SL 20 pips
    "60": 0.002,
    "120": 0.0
}
```
أو تعطيل واستخدام custom فقط.

## 7. إعدادات stoploss
- `stoploss = -0.002` (20 pips تقريباً على EURUSD)
- سيتم تنفيذ `custom_stoploss` لدعم:
  - Break even بعد breakEvenAfterPips
  - استخدام سعر الدخول +/- stopLossPips * pipSize

## 8. هل سيتم تفعيل short أو لا
- **نعم** (`can_short = True`)
- لأن الاستراتيجية الأصلية تدعم كلا الاتجاهين.

## 9. كيف ستمنع lookahead
- كل الحسابات ستستخدم `.shift(1)` أو rolling مع min_periods.
- `pivot_high/low` سيتم حسابها بطريقة تؤكد الـ pivot بعد pivotLen شمعات (مثل ta.pivothigh).
- لا `iloc[-1]` في منطق الإشارات.
- لا `shift(-n)`.
- سيتم اختبارها لاحقاً بـ lookahead-analysis.

## 10. كيف ستتعامل مع `request.security`
- **لا يوجد** في الأصلية → لا حاجة لـ informative_pairs في هذه النسخة.

## 11. كيف ستتعامل مع `pivothigh/pivotlow`
- سيتم تنفيذ دالة مكافئة:
```python
def pivots(df, left, right):
    # تنفيذ يدوي أو استخدام pandas_ta / technical
    ph = df['high'].shift(right).rolling(left + right + 1).max() == ...
    # أو استخدام:
    # from technical import pivots
```
- `last_ph = ph.ffill().shift(1)` للحصول على آخر قمة مؤكدة.

## 12. كيف ستتعامل مع الدعم/المقاومة اليدوية
- **لا يوجد** دعم/مقاومة يدوية في الكود (لا line.new أو var).
- الـ pivots هنا تمثل مناطق سيولة (lastHigh / lastLow).
- سيتم استخدامها مباشرة كـ dynamic levels للـ sweep detection.

## 13. أمر الباكتيست
```bash
freqtrade backtesting --config user_data/config.json --strategy CRT_ThickCandleBreak --timeframe 15m --timerange 20250101-20260101 --fee 0 --export signals --cache none -p EUR/USDT
```

## 14. أمر backtesting-analysis
```bash
freqtrade backtesting-analysis --config user_data/config.json --analysis-groups 0 1 2 4 5 --analysis-to-csv
```

## 15. أمر lookahead-analysis
```bash
freqtrade lookahead-analysis --config user_data/config.json --strategy CRT_ThickCandleBreak --timeframe 15m --timerange 20250101-20260101 --fee 0 -p EUR/USDT
```

---

**الخطوات بعد الموافقة:**
1. إنشاء الملف الجديد في `user_data/strategies/`
2. إضافة تعليقات عربية قصيرة
3. تنفيذ الباكتيست (بعد موافقة منفصلة)
4. تشغيل التحليلات

**ملاحظة:** سيتم الالتزام بـ `can_short = True` لأن الاستراتيجية الأصلية تدعم الاتجاهين، مع إمكانية تعديل لاحقاً إذا أردنا البدء بـ long فقط.
