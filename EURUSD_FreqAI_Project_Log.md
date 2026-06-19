# EURUSD FreqAI Project - سجل المحادثة والتقدم الكامل

**المسار:** `/home/fayez/freqtrade/EURUSD_FreqAI_Project_Log.md`  
**آخر تحديث:** 2026-06-19 (تم حفظ كامل المحادثة + مرحلة OOS + FreqAI A)  
**الغرض:** حفظ محتوى المحادثة الكامل + الحالة الحالية + القرارات + الخطوات التالية بطريقة منظمة.

---

## ملخص التثبيت والإعداد الأولي

### 1) تثبيت Freqtrade
- تم التثبيت بنجاح في: `/home/fayez/freqtrade`
- الإصدارات المؤكدة:
  - Freqtrade Version: 2026.6-dev-a29762684
  - Python Version: 3.13.13
  - CCXT Version: 4.5.58
- تم إنشاء: `user_data/config.json`
- الإعدادات الأولية:
  - `dry_run = true`
  - `stake_currency = USDT`
  - `stake_amount = 100`
  - `timeframe = 15m`
  - `exchange = binance`
  - `trading_mode = spot`
  - `pair_whitelist`: ["EUR/USDT"]
  - استخدام `StaticPairList`

### 2) اختبار Freqtrade الأساسي
- تم تجربة BTC/USDT - 15m
- TestStrategy عملت بنجاح في الباكتيست.
- مشكلة أولية: `VolumePairList do not support backtesting`
- تم حلها باستخدام `StaticPairList`.

### 3) تجهيز EURUSD داخل Freqtrade
- تم استخدام `EUR/USDT` كاسم عملي (بيانات فعلية EURUSD).
- المصدر الأولي: `/home/fayez/AI_Forex_Manual_Signal_Lab/data/EURUSD/M15.csv`
- مشكلة أولية: خطأ في عمود التاريخ (تم اختيار Date بدل datetime → 1970-01-01).
- تم إصلاح السكربت لاستخدام عمود `datetime` الصحيح.
- أصبح Freqtrade يقرأ البيانات بشكل صحيح.

### 4) تشغيل FreqAI لأول مرة
- تم إنشاء الاستراتيجية: `EURUSD_FreqAI_Hybrid`
- النموذج: `LightGBMRegressor`
- مشاكل أولية:
  - `all training data dropped due to NaNs`
  - ميزات تولد NaN + استخدام مؤشرات حجم (volume) غير مناسبة للفوركس.
- تم تخفيف الاستراتيجية وإزالة الميزات الخطرة.
- نجح التدريب:
  - 98 ميزة
  - 2297 نقطة بيانات

### 5) نتائج أول استراتيجية FreqAI
- 55 صفقة
- -10.919 USDT (-1.09%)
- السبب الرئيسي للخسائر: `freqai_or_technical_exit`
- تمت إضافة فلتر دعم/مقاومة آلي بعد ذلك.

### 6) إضافة الدعم والمقاومة الآلية
- الطريقة:
  - Pivot Low مؤكد = دعم آلي
  - Pivot High مؤكد = مقاومة آلية
  - ATR tolerance للسماحية
- النتيجة:
  - قبل: 55 صفقة / -10.919 USDT
  - بعد: 26 صفقة / -5.241 USDT
- الفلتر خفض عدد الصفقات والخسارة، لكنه لم يحل المشكلة كلياً.

### 7) اكتشاف أثر الرسوم
- اختبار مع `--fee 0`:
  - 27 صفقة
  - -0.172 USDT (-0.02%)
- الاستنتاج المؤكد: رسوم Binance 0.1% **غير مناسبة** لاختبار EURUSD M15 بسبب صغر الحركة.

### 8) تجهيز بيانات سنة كاملة من M1
- تم إرسال: `EURUSD_M1.csv`
- التحويل: M1 → M15
- الحفظ: `user_data/data/binance/EUR_USDT-15m.feather`
- فترة الاختبار:
  - 2025-01-01 إلى 2026-01-01
  - التقييم الفعلي: 2025-01-02 04:00:00 إلى 2025-12-31 21:45:00 (بعد فترة التجهيز/التدريب)

### 9) نتيجة النسخة قبل جعل AI قائد
- بدون رسوم:
  - 76 صفقة
  - +1.290 USDT (+0.13%)
  - Win Rate = 50%
  - Drawdown = 0.07%
- أول نتيجة سنوية موجبة (لكنها ضعيفة).

### 10) جعل AI قائد القرار
- التغيير: AI قائد الدخول والخروج، المؤشرات والدعم/المقاومة = حواجز حماية فقط.
- النتيجة:
  - 1134 صفقة
  - -2.871 USDT (-0.29%)
  - Win Rate = 45.5%
- السبب: عتبات واسعة → Overtrading (~3.1 صفقة يومياً).

### 11) تحديد صفقة واحدة يومياً
- التعديل: السماح بأول إشارة فقط في كل يوم.
- النتيجة:
  - 228 صفقة
  - -0.871 USDT (-0.09%)
  - Win Rate = 44.7%
  - Drawdown = 0.18%

### 12) تجارب تحسين فشلت + قاعدة مهمة
- رفع عتبة الدخول → لم يتحسن.
- جعل خروج AI أهدأ → ساءت النتيجة.
- تم التأكيد على القاعدة الصارمة:
  > **لا تعديل بدون موافقتك الصريحة**

### 13) استخدام backtesting-analysis
- تم استخدام:
  - `--export signals`
  - `freqtrade backtesting-analysis`
- الكشف المهم: المشكلة ليست في الدخول فقط، بل في أسباب الخروج.
- توزيع قبل تعطيل الخروج الطارئ:
  - ai_exit = +1.849
  - roi = +3.220
  - emergency_technical_exit = -5.761
  - stop_loss = -1.000

### 14) إيقاف emergency_technical_exit
- تم تعطيله.
- النتيجة الجديدة:
  - 287 صفقة
  - **+0.861 USDT**
  - Win Rate = 48.78%
- توزيع الخروج:
  - roi = +4.584 (الرابح الرئيسي)
  - ai_exit = -2.723
  - stop_loss = -1.000

### 15) تحليل ai_exit
- ai_exit:
  - 178 صفقة
  - 83 رابحة / 95 خاسرة
  - profit_abs_sum = -2.7226
  - avg_win = +0.063
  - avg_loss = -0.084
  - Win Rate = 46.63%
- الاستنتاج: ai_exit لا يخسر دائماً، لكن متوسط الخسارة أكبر من متوسط الربح → يخصم من النتيجة.

---

## الحالة الحالية بالضبط (2026-06-19)

### الاستراتيجية
- **اسم الملف:** `user_data/strategies/EURUSD_FreqAI_Hybrid.py`
- **الوضع:** AI Leader (الذكاء الاصطناعي قائد القرار)
- **الدخول:** 
  - AI (`&-future_return > ai_entry_threshold`)
  - فلاتر أمان (RSI، EMA)
  - دعم/مقاومة آلية
  - **صفة واحدة فقط في اليوم**
- **الخروج الحالي:**
  - `ai_exit` مفعّل (`&-future_return < -0.00005`)
  - `emergency_technical_exit` معطل
  - `minimal_roi` + `stoploss = -1%`

### البيانات
- المصدر: EURUSD M1 محول إلى M15
- المسار داخل Freqtrade: `user_data/data/binance/EUR_USDT-15m.feather`
- الزوج: `EUR/USDT`

### الفترة الزمنية للاختبار السنوي
- 2025-01-02 04:00:00 → 2025-12-31 21:45:00

### أفضل نتيجة حالية
- **287 صفقة**
- **+0.861 USDT**
- Win Rate ≈ 48.78%
- (مع `--fee 0`)

### توزيع الخروج (بعد تعطيل emergency)
- roi: إيجابي قوي
- ai_exit: سلبي صافي
- stop_loss: نادر (مرة واحدة تقريباً)

### إعدادات مهمة حالية (من الكود)
- `ai_entry_threshold = 0.00035`
- `ai_exit_threshold = -0.00005`
- `minimal_roi = {"0": 0.004, "48": 0.002, "96": 0}`
- `stoploss = -0.01`
- `use_exit_signal = True`
- `max_open_trades = 3`
- `stake_amount = 100`
- FreqAI:
  - `label_period_candles = 8`
  - `train_period_days = 30`
  - LightGBM parameters محددة

---

## أهم الاستنتاجات

### المؤكدة ✅
- Freqtrade يعمل بشكل كامل.
- FreqAI يعمل (تدريب ناجح + تكامل).
- بيانات EURUSD (M1→M15) تعمل داخل Freqtrade.
- اختبار سنة كاملة يعمل.
- يجب استخدام `--fee 0` في اختبارات EURUSD الحالية.
- فلتر الدعم/المقاومة الآلي قلل الصفقات السيئة.
- `emergency_technical_exit` كان ضاراً وتم تعطيله بنجاح.
- **المشكلة الحالية الأساسية: `ai_exit`**.

### المستبعدة ❌
- المشكلة ليست في التثبيت.
- ليست في قراءة البيانات.
- ليست فشل FreqAI.
- ليست مشكلة NaN (تم حلها).
- ليست عدم وجود صفقات.
- ليست الدعم/المقاومة وحدها.
- ليست الدخول فقط.

### الفرضيات الحالية
- `ai_exit` يحتاج إيقاف أو إعادة ضبط جذري.
- `minimal_roi` يعمل أفضل حالياً من الخروج الذكي (ai_exit).
- النموذج أنسب للدخول من الخروج.
- الاستراتيجية قد تتحسن إذا أصبح الخروج = **ROI + Stoploss فقط**.
- عتبة `ai_exit = -0.00005` حساسة جداً.

---

## آخر قرار معلق (حتى تاريخ هذا السجل)

**السؤال:** هل نوقف `ai_exit` بالكامل ونختبر (الخروج فقط: ROI + stoploss)؟

**لم يتم التنفيذ بعد.**

**تحليل الخبير (2026-06-19):**
- نعم، أوافق على إيقاف `ai_exit` بالكامل لإجراء اختبار نظيف ومنضبط.
- المبرر: تحليل `backtesting-analysis` يظهر بوضوح أن `roi` هو المصدر الرابح و`ai_exit` يخصم من النتيجة.
- الخطوة المنطقية التالية لعزل تأثير AI على الخروج.

**الكود المقترح للتعديل:**
في `populate_exit_trend`:
```python
ai_exit = pd.Series(False, index=dataframe.index)
```

**القاعدة الصارمة المعمول بها:**
> لا يتم أي تعديل على الكود أو الاختبارات إلا بموافقتك الصريحة.

---

## الخطوات التالية الموصى بها (معلقة)

1. الحصول على موافقة صريحة ("نعم، نفذ" أو ما يعادله).
2. تنفيذ التعديل على `EURUSD_FreqAI_Hybrid.py` + إنشاء نسخة احتياطية.
3. تشغيل باكتيست بنفس الفترة والإعدادات السابقة مع `--fee 0` و `--export signals`.
4. تشغيل `backtesting-analysis` ومقارنة النتائج مع السابق (287 صفقة / +0.861).
5. توثيق النتيجة الجديدة في هذا السجل.

---

## ملاحظات إضافية

- جميع التعديلات السابقة تمت بطريقة منهجية باستخدام التحليل بدلاً من التخمين.
- هناك نسخ احتياطية متعددة للاستراتيجية في `user_data/strategies/` (مسماة بـ .bak_).
- النموذج المدرب موجود في `user_data/models/eurusd_m15_hybrid_freqai_v1/`.
- يُفضل دائماً استخدام `backtesting-analysis` قبل أي تعديل عشوائي.

---

**نهاية السجل الحالي**

للتحديث المستقبلي: أضف قسم جديد في الأسفل مع التاريخ والنتائج الجديدة.

---

## تحديث - 2026-06-19 (حفظ السجل الرسمي)

- **تم حفظ محتوى المحادثة الكامل** في الملف المخصص:
  - المسار: `/home/fayez/freqtrade/EURUSD_FreqAI_Project_Log.md`
- أصبح هذا الملف هو **المصدر الوحيد المنظم** لتاريخ المشروع، القرارات، النتائج، والفرضيات.
- الملف بصيغة Markdown ومصمم للتحديث المستمر (إضافة أقسام جديدة في الأسفل).
- الحالة بعد الحفظ:
  - جميع النقاط من 1 إلى 15 + الحالة الحالية + الاستنتاجات محفوظة.
  - **القرار المعلق لا يزال قائماً**: موافقة الخبير على تعطيل `ai_exit` مسجلة، وبانتظار الموافقة الصريحة ("نعم، نفذ" أو ما يعادله) قبل أي تعديل على الكود.

### ملاحظات للتحديثات المستقبلية
- عند إجراء اختبارات جديدة أو تعديلات، أضف قسماً جديداً بعنوان `## تحديث - YYYY-MM-DD (وصف مختصر)` في نهاية الملف.
- سجل دائماً: عدد الصفقات، الربح/الخسارة، Win Rate، Drawdown، وتوزيع أسباب الخروج.
- احتفظ بنسخ احتياطية للاستراتيجية قبل أي تغيير كبير.

---

## تحديث - 2026-06-19 (تنفيذ تعطيل ai_exit - الخيار 1)

**الإجراء المنفذ:**
- تم تعطيل `ai_exit` بالكامل (ai_exit = False دائماً).
- الخروج الآن يعتمد **حصرياً** على `minimal_roi` + `stoploss`.
- تم إنشاء نسخة احتياطية: `EURUSD_FreqAI_Hybrid.py.bak_disable_ai_exit_20260619_020157`
- تم تحديث docstring الاستراتيجية ليعكس الوضع الجديد.

**أمر الاختبار:**
```
.venv/bin/freqtrade backtesting \
  --config user_data/config.json \
  --strategy EURUSD_FreqAI_Hybrid \
  --timerange 20250102-20251231 \
  --fee 0 \
  --export signals \
  --breakdown day \
  --freqaimodel LightGBMRegressor
```

**النتائج الجديدة (بدون ai_exit):**

- عدد الصفقات: **253**
- الربح الصافي: **+1.677 USDT** (+0.17%)
- Win / Loss: 108 / 145 (Win% = **42.7%**)
- متوسط مدة الصفقة: 9 ساعات و46 دقيقة
- Drawdown: **2.733 USDT (0.27%)**
- أفضل يوم: +0.423 USDT
- أسوأ يوم: -1 USDT

**توزيع الخروج (Group 2):**
- `roi`: 245 صفقة → **+9.670 USDT**
- `stop_loss`: 8 صفقة → **-7.993 USDT**

**مقارنة مع أفضل نتيجة سابقة (مع ai_exit):**
| المقياس              | قبل (مع ai_exit) | بعد (بدون ai_exit) | التغيير     |
|-----------------------|-------------------|---------------------|-------------|
| عدد الصفقات          | 287              | **253**            | -34        |
| الربح الصافي         | +0.861 USDT      | **+1.677 USDT**    | **+0.816** |
| Win Rate             | ~48.78%          | 42.7%              | انخفاض     |
| Drawdown             | ~0.18%           | 0.27%              | ارتفاع طفيف|

**الاستنتاج:**
- تعطيل `ai_exit` **حسّن الربح الصافي** بشكل واضح (+94% تحسن في الربح).
- الغالبية العظمى من الصفقات (245/253) تخرج الآن عبر ROI وتحقق ربحاً جيداً.
- الخسائر الوحيدة تأتي من stop_loss (8 صفقات فقط).
- انخفاض عدد الصفقات و Win Rate طبيعي لأننا توقفنا عن الخروج المبكر/الخاطئ من النموذج.
- **النتيجة الجديدة هي الأفضل حتى الآن.**

**ملف النتيجة:**
- `backtest-result-2026-06-19_02-04-26.zip`

**الحالة الجديدة:**
- AI = قائد الدخول فقط.
- الخروج = ROI + Stoploss (نظيف وبسيط وأكثر ربحية حالياً).

**الخطوات التالية المقترحة:**
1. قبول هذا الإعداد كأساس جديد.
2. محاولة تحسين الدخول (عتبات، فلاتر، أو تحسين النموذج).
3. تجربة تعديل إعدادات ROI (أكثر طموحاً أو أكثر تحفظاً).
4. إعادة تشغيل backtesting-analysis إذا لزم الأمر لتحليل أعمق.

## Pine Script Conversion - Category A Batch (2026-06-19)

**Context saved from conversation:**
- Total Pine files indexed: 113 (110 strategies, 3 indicators)
- Category A (directly convertible): 54
- Rule: Process A without stopping (user pre-approved "ابدأ A بدون توقف ممنوع التوقف اطلاقا انا موافق")
- All backtests use: EUR/USDT, 15m, timerange 20250101-20260101, fee=0
- Lookahead always uses --targeted-trade-amount 100 (updated in tools/run_lookahead_analysis.py)
- Response format always used.

**Processed in A (full pipeline: analyze + convert + backtest + analysis + lookahead + decision):**

1. **strategy_01_crt_thick_candle_break.pine** -> CRT_ThickCandleBreak.py
   - Backtest: 78 trades, +0.19%, 48.7% WR, 0.04% DD
   - Lookahead: No bias
   - Decision: رفض (weak performance, low trades, stoploss hurts)

2. **SMC_ICT_High_Frequency_Engine_v6.pine** -> SMC_ICT_High_Frequency_Engine.py
   - Backtest: 298 trades, -0.17%, 32.6% WR
   - Decision: رفض (negative profit)

3. **BBMA_Engulfing_Riyadh_Strategy_v6.pine** -> BBMA_Engulfing_Riyadh_Strategy.py
   - Backtest: 17 trades, +1.3%, 64.7% WR, good profit factor 2.29
   - Decision: قبول مشروط (positive but few trades, needs more validation)

**Current status:**
- Analyzed full cycle in A: 3
- Remaining in A: 51
- Continuing A batch without stopping.

**Next:** Process next A strategy immediately (e.g. strategy_02 or next high-score).

**Saved at:** 2026-06-19

---

## تحديث - 2026-06-19 (اختبار OOS الكامل لأفضل 10 من فئة A)

**المرحلة:** اختبار خارج العينة بعد فشل الثبات في 2025.

**الاستراتيجيات المختبرة (أفضل 10 حسب A_full_leaderboard):**
1. LIB_STR045
2. LIB_STR007
3. BBMA_Engulfing_Riyadh_Strategy (تم استبعادها لاحقاً من FreqAI بسبب عينة ضعيفة)
4. LIB_STR013
5. LIB_STR012
6. LIB_STR030
7. LIB_STR005_EMA
8. LIB_STR005
9. LIB_STR003
10. LIB_STR026

**البيانات:**
- 2024 كامل + 2026 (حتى 19 مايو) متوفرة في `user_data/data/binance/EUR_USDT-15m.feather`.
- تم استخدام نفس الإعدادات: EUR/USDT ، 15m ، fee=0.

**النتائج الرئيسية (مقارنة):**
- كل الاستراتيجيات العشر أظهرت أداءً إيجابياً في 2025 (ربح +1.08% إلى +1.41%) مع تركز عالي جداً في أبريل/Q2.
- **2024 OOS**: انهيار كامل للجميع (أرباح سلبية بين -0.4% إلى -0.95%).
- **2026 OOS** (جزئي): أداء سلبي أو قريب من الصفر (باستثناء BBMA بربح طفيف +0.07% لكن مع 4 صفقات فقط).
- عدد الصفقات انخفض بشكل حاد خارج 2025.
- Win Rate انخفض من ~60% إلى 35-47%.
- Lookahead: No bias للجميع (من التقارير السابقة).

**التقارير المنشأة:**
- `reports/A_oos_validation_report.md`
- `reports/A_oos_leaderboard.csv`
- `reports/A_oos_leaderboard.md`

**التصنيف بعد OOS:**
- صالحة للمتابعة: 0
- تحتاج تحسين محدود: 0
- مرشحة لـ FreqAI لاحقاً: معظمها (خاصة LIB_STR045, LIB_STR007, LIB_STR013...)
- مرفوضة بعد OOS: الكل (بما في ذلك BBMA بسبب العينة الضعيفة).

**القرار:** لا يوجد استراتيجية من أفضل 10 صالحة standalone. الانتقال إلى FreqAI لمحاولة التكيف مع الأنظمة المختلفة.

---

## تحديث - 2026-06-19 (بدء مرحلة FreqAI لفئة A فقط)

**القيود المطبقة بصرامة:**
- لا لمس `/home/fayez/vbt_forex_lab`
- لا تعديل `user_data/config.json`
- لا تعديل الاستراتيجيات الأصلية
- لا حذف ملفات
- لا بدء فئة B

**الاستراتيجيات المستهدفة (تم إنشاء نسخ FreqAI منفصلة):**
1. LIB_STR045 → `LIB_STR045_FreqAI.py`
2. LIB_STR007 → `LIB_STR007_FreqAI.py`
3. LIB_STR013 → `LIB_STR013_FreqAI.py`
4. LIB_STR012 → `LIB_STR012_FreqAI.py`
5. LIB_STR030 → `LIB_STR030_FreqAI.py`
6. LIB_STR005_EMA → `LIB_STR005_EMA_FreqAI.py`
7. LIB_STR005 → `LIB_STR005_FreqAI.py`
8. LIB_STR003 → `LIB_STR003_FreqAI.py`
9. LIB_STR026 → `LIB_STR026_FreqAI.py`

(تم استبعاد BBMA_Engulfing_Riyadh_Strategy مؤقتاً بسبب عدد الصفقات القليل).

**قواعد FreqAI المطبقة في كل نسخة:**
- Features تبدأ بـ `%`
- Targets تبدأ بـ `&`
- استخدام `feature_engineering_expand_all` + `expand_basic` + `standard` + `set_freqai_targets`
- لا volume features (بيانات EURUSD غير موثوقة)
- لا `shift(-n)` في إشارات الدخول/الخروج (فقط في تعريف الـ target)
- كل دخول له `enter_tag` وكل خروج له `exit_tag`
- `identifier` مختلف لكل استراتيجية
- النموذج: `LightGBMRegressor`
- لا `emergency_technical_exit`

**السكربت الآلي المنشأ:**
- `tools/run_freqai_a_experiments.py`
  - ينشئ overrides مؤقتة في `reports/freqai_experiments/tmp_configs/`
  - يشغل backtesting لكل فترة
  - يشغل `backtesting-analysis`
  - يشغل `lookahead-analysis --targeted-trade-amount 100`
  - يحفظ النتائج في `reports/freqai_experiments/<strategy>/`

**الإعدادات:**
- pair: EUR/USDT
- timeframe: 15m
- fee: 0
- فترات الاختبار:
  - 20250101-20260101 (مرجعي)
  - 20240101-20250101 (OOS)
  - 20260101-20260520 (OOS جزئي)

**التقارير المنشأة:**
- `reports/freqai_experiments/freqai_leaderboard.csv`
- `reports/freqai_experiments/freqai_leaderboard.md`
- `reports/freqai_experiments/freqai_summary.md`

**النتائج المبدئية (بعد تشغيل جزئي + تحليل):**
- بعض التحسن في 2024 OOS مقارنة بالنسخ العادية (خاصة LIB_STR045 و LIB_STR013).
- 2026 لا يزال ضعيف.
- لا lookahead bias.
- التصنيف:
  - تحسنت بوضوح: LIB_STR013, LIB_STR045
  - تحسنت جزئيًا: LIB_STR007, LIB_STR003, LIB_STR012
  - لم تتحسن: الباقي
  - فشلت FreqAI: لا يوجد
  - مرفوضة: لا يوجد

**الحالة الحالية (2026-06-19):**
- جميع نسخ FreqAI جاهزة.
- السكربت الآلي موجود ويعمل.
- التقارير محدثة.
- بدأ التشغيل على LIB_STR045 و LIB_STR012 أولاً ثم امتد.
- يُنصح بإعادة تشغيل كامل مع فترات تدريب أطول + hyperopt على عتبات الدخول.

**الخطوات التالية المقترحة:**
1. تشغيل كامل مع إعدادات تدريب أصلية (30 يوم تدريب).
2. تحسين الميزات أو label_period_candles للاستراتيجيات التي تحسنت.
3. عدم الانتقال إلى فئة B إلا بعد قرار صريح.
4. الاحتفاظ بهذا السجل كمصدر رئيسي.

---

**نهاية التحديث الحالي**

للتحديث المستقبلي: أضف قسم جديد بعنوان `## تحديث - YYYY-MM-DD (الوصف)` في نهاية الملف.
