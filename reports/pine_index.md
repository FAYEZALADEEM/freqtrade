# فهرس استراتيجيات Pine Script v6

**التاريخ:** 2026-06-19 02:34

**عدد الملفات:** 113

## الإحصائيات

- إجمالي الملفات: 113
- استراتيجيات (strategy): 110
- مؤشرات (indicator): 3
- تستخدم request.security: 17
- تستخدم pivothigh/pivotlow: 55
- دعم/مقاومة يدوية محتملة: 44
- قابلة للتحويل مباشرة (score >= 80): 54

## أفضل 10 ملفات قابلة للتحويل (حسب الدرجة)

| الملف | الإصدار | Strategy؟ | request.security | Pivots | Manual SR | Score | الفئة |
|-------|---------|-----------|------------------|--------|-----------|-------|-------|
| SMC_ICT_High_Frequency_Engine_v6.pine | 6 | True | False | True | False | 90 | A - قابلة مباشرة |
| SMC_ICT_Riyadh_Strategy_v6.pine | 6 | True | False | True | False | 90 | A - قابلة مباشرة |
| strategy_01_crt_thick_candle_break.pine | 6 | True | False | True | False | 90 | A - قابلة مباشرة |
| strategy_02_ict_silver_bullet_liquidity_sweep_fvg.pine | 6 | True | False | True | False | 90 | A - قابلة مباشرة |
| strategy_03_smc_liquidity_grab_imbalance_ob.pine | 6 | True | False | True | False | 90 | A - قابلة مباشرة |
| strategy_04_smc_order_block_bos.pine | 6 | True | False | True | False | 90 | A - قابلة مباشرة |
| strategy_06_breaker_block_retest.pine | 6 | True | False | True | False | 90 | A - قابلة مباشرة |
| strategy_12_rsi_divergence_reversal.pine | 6 | True | False | True | False | 90 | A - قابلة مباشرة |
| BBMA_Engulfing_Riyadh_Strategy_v6.pine | 6 | True | False | False | False | 80 | A - قابلة مباشرة |
| CRT_1AM_Strategy_V1_Pine_v6.pine | 6 | True | False | False | False | 80 | A - قابلة مباشرة |

## ملخص الفئات

- A - قابلة مباشرة: 54
- B - تحتاج تعديل بسيط (pivots/manual sr): 44
- C - تحتاج إعادة بناء: 12
- D - غير مناسبة: 3

## مشاكل التوافق مع Pine Script v6 المكتشفة (محدثة)

بعد فحص شامل، تم اكتشاف المشاكل التالية التي تؤثر على جودة التحويل:

| المشكلة                          | عدد الملفات | الملفات البارزة / ملاحظات |
|----------------------------------|--------------|-----------------------------|
| إصدار غير v6 (`@version=4`)     | 1            | `PMax_Explorer_Arabic.pine` (سكريبر متعدد الرموز) |
| ملفات مؤشرات فقط (لا `strategy()`) | 3         | Market_Fluidity_Smart*.pine + Mean_Reversion_ZScore_Indicator... |
| استخدام `security()` القديم     | 18           | Wolf strategies + بعض ICT + استراتيجية_جنون_التداول (يُفضل `request.security()`) |
| أنماط محتملة لـ lookahead       | 13           | Wolf* + CRT_1AM + TrendMaster + بعض Mean_Reversion |
| `strategy.entry(..., when=...)`  | 1            | PMax_Explorer_Arabic.pine فقط |
| `input()` بالصيغة القديمة       | 1            | PMax_Explorer_Arabic.pine |

**توصية:** راجع التقرير المفصل `reports/pine_migration_issues.md` الذي يحتوي على:
- قوائم كاملة بالملفات المتأثرة
- اقتراحات إصلاح محددة لكل نوع مشكلة
- أولويات الإصلاح قبل بدء التحويل أو FreqAI

> **ملاحظة:** هذا التحليل آلي أولي + فحص يدوي جزئي. يحتاج تحليل يدوي كامل لكل استراتيجية قبل التحويل.
