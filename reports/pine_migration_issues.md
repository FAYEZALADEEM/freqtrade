# تقرير مفصل: مشاكل التوافق مع Pine Script v6

**التاريخ:** 2026-06-19  
**الغرض:** تقرير منفصل ومركز فقط على المشاكل المكتشفة في ملفات `pine_strategies/`  
**عدد الملفات الكلي:** 113 ملف `.pine`  
**المصدر:** فحص آلي + يدوي لكل الملفات

---

## ملخص سريع

| الفئة | عدد الملفات المتأثرة | مستوى الأولوية |
|-------|-----------------------|-----------------|
| إصدار Pine غير v6 | 1 | حرج |
| ملفات مؤشرات (ليست استراتيجيات) | 3 | عالي |
| استخدام `security()` القديم | 18 | عالي |
| أنماط محتملة لـ lookahead | 13 | متوسط-عالي |
| استخدام `when=` في `strategy.entry` | 1 | عالي |
| `input()` قديم | 1 | متوسط |
| دوال `sma/ema/atr` بدون `ta.` | ~80 | منخفض-متوسط (تنظيف) |

---

## 1. ملفات بإصدار Pine غير مدعوم

**الملف الوحيد:**
- `PMax_Explorer_Arabic.pine`

**التفاصيل:**
- يبدأ بـ `//@version=4`
- يحتوي على مزيج من صيغ v4/v5.
- يعمل كـ "سكريبر" متعدد الرموز (20 رمز مختلف) وليس استراتيجية EURUSD 15m.

**اقتراحات الإصلاح:**
1. غيّر السطر الأول إلى `//@version=6`
2. حدّث جميع `input()` إلى الدوال الجديدة (`input.int()`, `input.float()`, `input.bool()`, `input.string()`).
3. استبدل `security()` بـ `request.security()`.
4. أزل أو حدّث `strategy.entry(..., when=...)` (استخدم شرط `if` قبل الدخول).
5. غيّر `sma()`, `ema()`, `atr()` إلى `ta.sma()`, `ta.ema()`, `ta.atr()`.
6. فكر في جعله `indicator()` بدلاً من `strategy()` إذا كان مجرد أداة عرض.

**مثال من الكود:**
```pinescript
//@version=4   ← غيّر إلى 6
src = input(hl2, title="المصدر")   ← غيّر إلى input.source()
atr2 = sma(tr, Periods)           ← غيّر إلى ta.sma()
strategy.entry("شراء", strategy.long, when=Timerange())  ← أزل when=
```

---

## 2. ملفات مؤشرات (ليست استراتيجيات تداول)

هذه الملفات تستخدم `indicator()` أو لا تحتوي على `strategy()` على الإطلاق:

1. `Market_Fluidity_Smart.pine`
2. `Market_Fluidity_Smart_SRC_fixed_v2.pine`
3. `Mean_Reversion_ZScore_Indicator_V1_1_EURUSD_M15_Pine_v6.pine`

**ملاحظات:**
- الملف الثالث يحتوي صراحة: `indicator(title = "Mean Reversion الإحصائي...")`
- هذه الملفات مناسبة كمؤشرات مساعدة فقط، وليست استراتيجيات رئيسية للـ backtesting أو الـ FreqAI.

**اقتراحات الإصلاح:**
- انقلها إلى مجلد منفصل (مثل `pine_indicators/`) إن أردت الاحتفاظ بها.
- أو أزلها من قائمة مرشحي التحويل (فئة A/B).
- إذا أردت تحويلها، أنشئ نسخة `strategy()` منفصلة.

---

## 3. استخدام `security()` القديم (18 ملف)

**القائمة الكاملة:**

1. FAYEZ_1_AR_SETTINGS_FIXED_v2.pine
2. ICT_SMC_CRT_ORB_Unified_v6.pine
3. ICT_Sniper_TV_Match_2025_FIXED.pine
4. Mean_Reversion_ZScore_Indicator_V1_1_EURUSD_M15_Pine_v6.pine
5. Mean_Reversion_ZScore_V1_EURUSD_M15_Pine_v6.pine
6. PMax_Explorer_Arabic.pine
7. SMC_Quant_V1_GBPUSD_M15_Pine_v6.pine
8. strategy_09_adx_ema_intraday_trend.pine
9. TrendMaster_Modified_M30_BASE_AP_Candidate_v1.pine
10. trend_pullback_h1_v2_3.pine
11. vsa_mtf_template_v3.pine
12. Wolf_Sniper_V18.pine
13. wolf_strategy-1.pine
14. Wolf_V18_Pure.pine
15. Wolf_V18_Pure_TradeFix_v6.pine
16. Wolf_V4_3_Trade_Test_Patch_Direction_Rerun.pine
17. Wolf_V4_3_Trade_Test_Patch.pine
18. استراتيجية_جنون_التداول_v2_تصحيح_خطأ_resetSequence.pine

**المشكلة:**
- `security()` هو الاسم القديم (قبل Pine v5).
- يمكن أن يسبب مشاكل في الـ repainting و lookahead في بعض الحالات.

**اقتراح الإصلاح (لكل ملف):**
```pinescript
// قديم
data = security(syminfo.tickerid, "D", close)

// جديد في v6
data = request.security(syminfo.tickerid, "D", close)
```

---

## 4. أنماط محتملة لـ Lookahead Bias (13 ملف)

**القائمة الكاملة:**

1. CRT_1AM_Strategy_V1_Pine_v6.pine
2. Market_Fluidity_Smart.pine
3. Market_Fluidity_Smart_SRC_fixed_v2.pine
4. Mean_Reversion_ZScore_Indicator_V1_1_EURUSD_M15_Pine_v6.pine
5. Mean_Reversion_ZScore_V1_EURUSD_M15_Pine_v6.pine
6. SMC_Quant_V1_GBPUSD_M15_Pine_v6.pine
7. TrendMaster_Modified_M30_BASE_AP_Candidate_v1.pine
8. trend_pullback_h1_v2_3.pine
9. Wolf_Sniper_V18.pine
10. wolf_strategy-1.pine
11. Wolf_V18_Pure.pine
12. Wolf_V18_Pure_TradeFix_v6.pine
13. استراتيجية_جنون_التداول_v2_تصحيح_خطأ_resetSequence.pine

**المشكلة الشائعة:**
- استخدام `barstate.islast` أو `barstate.ishistory` أو كود يعتمد على بيانات مستقبلية.

**اقتراح الإصلاح:**
- شغّل `lookahead-analysis` على هذه الملفات.
- استبدل `barstate.islast` بـ شروط واضحة داخل `if barstate.isconfirmed`.
- تجنب أي وصول إلى `[0]` في سياقات معينة.

---

## 5. استخدام `when=` في `strategy.entry`

**الملف الوحيد:**
- `PMax_Explorer_Arabic.pine`

**المشكلة:**
- الباراميتر `when=` مهمل ويمكن أن يسبب سلوكاً غير متوقع في الإصدارات الحديثة.

**اقتراح الإصلاح:**
```pinescript
// قديم
if buySignal
    strategy.entry("شراء", strategy.long, when=Timerange())

// جديد (موصى به)
if buySignal and Timerange()
    strategy.entry("شراء", strategy.long)
```

---

## 6. استخدام `input()` بالصيغة القديمة

**الملف الوحيد:**
- `PMax_Explorer_Arabic.pine`

**اقتراح الإصلاح:**
- استخدم:
  - `input.int()`
  - `input.float()`
  - `input.bool()`
  - `input.string()`
  - `input.source()`

---

## 7. دوال حسابية قديمة بدون بادئة `ta.`

**عدد الملفات المتأثرة:** حوالي 80 ملف

**أمثلة شائعة:**
- `sma()`, `ema()`, `wma()`, `atr()`, `linreg()`, `rsi()`, `macd()`...

**ملاحظة:** 
هذه الدوال لا تزال تعمل في v6 للتوافق، لكنها غير موصى بها.

**اقتراح الإصلاح:**
```pinescript
// قديم
ma = sma(close, 14)
atrVal = atr(14)

// جديد (مفضل)
ma = ta.sma(close, 14)
atrVal = ta.atr(14)
```

**ملاحظة:** لا يُعتبر خطأ حرجاً، لكنه يُفضل تحديثه للنظافة والتوافق المستقبلي.

---

## 8. مشاكل أخرى لم تُكتشف بكثرة

- لا يوجد أي ملف يستخدم `study()` (جيد).
- لا توجد ملفات تحتوي على `lookahead_on` صريح في معظم الحالات.
- بعض ملفات Wolf تحتوي على نسخ متعددة (Wolf_V4_3_*) قد تكون تجريبية.

---

## جدول ملخص شامل لكل الملفات المتأثرة

| الملف | v4 | بدون strategy() | security() قديم | Lookahead | when= | input قديم | ملاحظات |
|-------|----|------------------|------------------|-----------|-------|-------------|---------|
| PMax_Explorer_Arabic.pine | ✓ | - | ✓ | ✓ | ✓ | ✓ | الأسوأ |
| Market_Fluidity_Smart*.pine | - | ✓ | - | ✓ | - | - | مؤشرات |
| Mean_Reversion_ZScore_Indicator... | - | ✓ | ✓ | ✓ | - | - | مؤشر |
| strategy_09_adx_ema... | - | - | ✓ | - | - | - | request.security |
| Wolf_* (عدة) | - | - | ✓ | ✓ | - | - | - |
| ... (باقي 18 ملف security) | - | - | ✓ | بعض | - | - | - |

(القائمة الكاملة مذكورة في الأقسام أعلاه)

---

## توصيات عامة للإصلاح

1. **ابدأ بالملفات الحرجة:**
   - PMax_Explorer_Arabic.pine (إما إصلاح كامل أو إزالة من قائمة الاستراتيجيات)
   - الـ 18 ملف التي تستخدم `security()` القديم

2. **استخدم أداة التحويل التلقائي:**
   - TradingView لديه أداة "Convert to v5/v6" (لكن راجع النتائج يدوياً).

3. **أولوية الإصلاح:**
   - حرج: PMax + old security + when=
   - عالي: المؤشرات + lookahead patterns
   - متوسط: bare ta. functions

4. **بعد الإصلاح:**
   - أعد تشغيل `PINE_V6_VALIDATION_REPORT` وحدّث `pine_index.csv`
   - شغّل `lookahead-analysis` على كل ملف تم إصلاحه.

---

**تم إنشاء هذا التقرير بناءً على فحص كامل للـ 113 ملف دون أي تعديل.**

---

**هل تريد حفظ هذا التقرير في `reports/pine_migration_issues.md` الآن؟**
