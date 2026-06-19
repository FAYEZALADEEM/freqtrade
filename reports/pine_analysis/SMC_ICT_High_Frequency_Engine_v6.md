# تحليل Pine Script: SMC_ICT_High_Frequency_Engine_v6

**الملف الأصلي:** SMC_ICT_High_Frequency_Engine_v6.pine
**الإصدار:** Pine v6
**نوع:** Strategy
**تاريخ التحليل:** 2026-06-19 03:11

## 1. المدخلات (Inputs)

- `tz_input = input...("America/New_York", title="المنطقة الزمنية | Timezone", options=["Asia/Riyadh", "America/New_York", "GMT+3", "UTC"])`
- `crt_session_str = input...("0100-0200", title="ساعة تحديد النطاق | CRT Reference Hour")`
- `kz_session_str = input...("0200-1100", title="ساعة الكيلزون والتلاعب | Killzone Window")`
- `sl_buffer = input...(1.5, title="هامش وقف الخسارة للنقاط | SL Buffer (Pips)`
- `max_daily_trades = input...(8, title="الحد الأقصى للصفقات يومياً (تم رفعه)`
- `swing_len = input...(8, title="حجم هيكل السيولة (Swing Length)`

## 2. المؤشرات المستخدمة

- ta.change
- ta.pivothigh
- ta.pivotlow

## 3. شروط الدخول (Long/Short)

```
strategy.entry("HF-SHORT", strategy.short) strategy.exit("TP-Short", "HF-SHORT", limit=tp_level, stop=stop_level) sweep_h_bars := 100 // تصفير الذاكرة لتجنب الدخول المتكرر على نفس السحب daily_trade_count += 1 // الشراء: يجب أن يكون السحب حدث خلال آخر 5 شموع + تشكلت فجوة حالياً bool long_condition = 
```

## 4. شروط الخروج

```
strategy.exit("TP-Short", "HF-SHORT", limit=tp_level, stop=stop_level) sweep_h_bars := 100 // تصفير الذاكرة لتجنب الدخول المتكرر على نفس السحب daily_trade_count += 1 // الشراء: يجب أن يكون السحب حدث خلال آخر 5 شموع + تشكلت فجوة حالياً bool long_condition = in_killzone and sweep_l_bars <= 5 and is_bu
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

high, low, close, pivot_high, open, volume, pivot_low

## 8. enter_tag / exit_tag المقترحة

- enter_tag: `pine_smc_ict_high_frequen`
- exit_tag: `exit_pine_smc_ict_high_frequen`

## 9. ملاحظات التحويل

- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).
- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.
- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.
- تجنب أي shift سلبي أو iloc مستقبلي.

---
**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.
