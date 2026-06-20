# أفضل ممارسات Freqtrade - تقرير المرحلة 1

**التاريخ:** 2026-06-19  
**المصدر:** التوثيق الرسمي لـ Freqtrade (backtesting.md، strategy-customization.md، advanced-backtesting.md، lookahead-analysis.md، freqai-feature-engineering.md، freqai-developers.md، ومراجع أوامر CLI).

## 1. أفضل ممارسات كتابة استراتيجية Freqtrade

- استخدم `populate_indicators()` لإضافة المؤشرات المستخدمة فعلياً في `populate_entry_trend()` أو `populate_exit_trend()` أو لإنشاء مؤشرات أخرى فقط (تجنب إضافة مؤشرات غير ضرورية لتوفير الذاكرة والـ CPU).
- أعد الـ DataFrame كاملاً من دوال `populate_*` دون إزالة أو تعديل الأعمدة الأساسية (`open`, `high`, `low`, `close`, `volume`).
- استخدم عمليات **vectorized** عبر pandas (مثل `dataframe.loc[(condition), 'enter_long'] = 1`). تجنب الحلقات (`for`) على الصفوف والمقارنات المباشرة على الـ Series.
- أضف شرط `(dataframe['volume'] > 0)` دائماً في شروط الدخول والخروج.
- حدد `startup_candle_count` بدقة (أكبر عدد شمعات مطلوب لحساب مؤشرات مستقرة). استخدم `recursive-analysis` للتحقق.
- استخدم `shift()` بدلاً من `iloc[-1]` أو الوصول المباشر للصفوف داخل دوال `populate_*`.
- عيّن `INTERFACE_VERSION = 3`.
- استخدم `enter_tag` و `exit_tag` لتسمية الإشارات وتسهيل التحليل لاحقاً.
- للـ shorting: عيّن `can_short = True` واستخدم `enter_short` / `exit_short`.
- `minimal_roi`: استخدم قاموس يحدد النسب حسب الدقائق منذ فتح الصفقة. عطّله بـ `{}`.
- `stoploss`: قيمة سالبة (مثال: `-0.10`).
- حدد `timeframe` بشكل صحيح (مثال: `"15m"`).

## 2. طريقة الباكتيست الصحيحة

- الأمر الأساسي: `freqtrade backtesting --strategy <StrategyName>`.
- حدد `--timeframe` إذا لزم (أو عبر `--strategy-list`).
- استخدم `--strategy-list` لمقارنة استراتيجيات متعددة.
- حدد الرصيد الأولي عبر `--dry-run-wallet` أو `--starting-balance`.
- تأكد من توفر البيانات التاريخية (استخدم `download-data` إذا لزم).
- النتائج تُصدر افتراضياً إلى `user_data/backtest_results`.
- استخدم `--cache none` عند إعادة التشغيل بعد تعديلات لتجنب النتائج المخزنة القديمة.
- للحصول على نتائج قابلة لإعادة الإنتاج: استخدم `StaticPairList` (الـ dynamic pairlists غير مضمونة التكرار).
- الإشارات تُولّد عند إغلاق الشمعة، والتنفيذ يحدث عند افتتاح الشمعة التالية.
- استخدم `--export trades` أو `signals` حسب الحاجة للتحليل اللاحق.

## 3. طريقة استخدام `--timerange`

- يحدد نطاق البيانات المستخدمة في الباكتيست والتحليل.
- أمثلة:
  - `--timerange=20190501-` : من 1 مايو 2019 فصاعداً.
  - `--timerange=-20180131` : حتى 31 يناير 2018.
  - `--timerange=20180131-20180301` : من 31 يناير إلى 1 مارس 2018.
  - `--timerange=1527595200-1527618600` : باستخدام POSIX timestamps.
- مفيد لتقليل حجم الاختبار أو اختبار فترات محددة (In-Sample / OOS).
- ينطبق على `backtesting` و `backtesting-analysis` و `lookahead-analysis`.

## 4. طريقة استخدام `--fee`

- يحدد نسبة رسوم مخصصة (تتجاوز الرسوم الافتراضية من البورصة).
- تُطبق مرتين (دخول + خروج).
- مثال: `--fee 0.001` (0.1%).
- استخدمه فقط للتجربة أو عند وجود rebates غير مرئية في ccxt.
- الافتراضي: يجلب الرسوم من معلومات السوق.

## 5. طريقة استخدام `--export signals`

- `--export signals` (مع `freqtrade backtesting`).
- يُنتج ملفات إضافية (`backtest-result-*.pkl` تحتوي signals و exited) بالإضافة إلى ملفات التداولات.
- ضروري لتشغيل `backtesting-analysis` وتحليل الـ tags والمؤشرات على شمعات الإشارة.
- قبل إعادة الباكتيست: احذف النتائج القديمة أو استخدم `--cache none`.

## 6. طريقة استخدام `backtesting-analysis`

- الأمر: `freqtrade backtesting-analysis --analysis-groups 0 1 2 3 4 5`.
- يقرأ آخر نتائج باكتيست (أو حدد `--backtest-filename` / `--backtest-directory`).
- مجموعات التحليل:
  - 0: ملخص عام winrate/profit حسب enter_tag.
  - 1: حسب enter_tag.
  - 2: حسب enter_tag + exit_tag.
  - 3: حسب pair + enter_tag.
  - 4: حسب pair + enter_tag + exit_tag (قد يكون كبيراً).
  - 5: حسب exit_tag.
- خيارات مفيدة: `--enter-reason-list`، `--exit-reason-list`، `--indicator-list`، `--entry-only`، `--exit-only`، `--rejected-signals`، `--analysis-to-csv`، `--timerange`.

## 7. طريقة استخدام `lookahead-analysis`

- الأمر: `freqtrade lookahead-analysis --strategy <Name>`.
- يكشف **lookahead bias** عن طريق مقارنة باكتيست كامل مع باكتيستات مقطوعة لكل إشارة.
- يفرض إعدادات معينة تلقائياً لتقليل الـ false positives: `--cache none`، market orders، max_open_trades كبير، wallet كبير، protections معطلة.
- خيارات إضافية: `--minimum-trade-amount`، `--targeted-trade-amount`، `--lookahead-analysis-exportfilename`، `--allow-limit-orders` (يُفضل تجنبه).
- يدعم استراتيجيات FreqAI.

## 8. قواعد منع lookahead bias

- لا تستخدم `shift(-n)` أبداً (ينظر إلى المستقبل).
- لا تستخدم `dataframe.iloc[-1]` أو أي indexing مطلق داخل دوال `populate_*`.
- تجنب الحلقات (`for`) غير المحكمة جيداً.
- تجنب دوال التجميع مثل `.mean()` / `.min()` / `.max()` على كامل العمود (استخدم `rolling(window)` بدلاً منها).
- تجنب `ta.MACD(dataframe, 12, 26, 1)` (signalperiod=1 يسبب bias).
- استخدم `merge_informative_pair()` لدمج الـ timeframes الإضافية.
- شغّل `lookahead-analysis` + `recursive-analysis` دائماً قبل أي dry-run أو live.
- في الباكتيست يُمرر كامل الـ DataFrame دفعة واحدة، لذا يجب الحذر الشديد من أي وصول مستقبلي.

## 9. قواعد FreqAI (features تبدأ بـ %، targets تبدأ بـ &، feature_engineering_*، set_freqai_targets)

- **الميزات (features)**: يجب أن تبدأ بـ `%` (مثال: `dataframe["%-rsi-period"] = ...`).
- **الأهداف (targets)**: يجب أن تبدأ بـ `&` (مثال: `dataframe["&-s_close"] = ...`).
- الدوال الإلزامية/الأساسية:
  - `feature_engineering_expand_all()`: توسع على `indicator_periods_candles` + timeframes + shifted + corr pairs.
  - `feature_engineering_expand_basic()`: توسع على timeframes + shifted + corr (بدون periods).
  - `feature_engineering_standard()`: تُستدعى مرة واحدة على الـ base timeframe (للميزات غير القابلة للتوسع مثل يوم الأسبوع).
  - `set_freqai_targets()`: **مطلوبة** لتعريف الـ targets.
- استخدم `metadata` داخل الدوال (`metadata["pair"]`، `metadata["tf"]`، `metadata["period"]`).
- في الـ config: حدد `feature_parameters` (`include_timeframes`، `include_corr_pairlist`، `include_shifted_candles`، `indicator_periods_candles`، `label_period_candles`).
- الـ targets عادة تستخدم `shift(-label_period_candles)` مع `rolling().mean()`.

## 10. أخطاء يجب تجنبها عند تحويل Pine Script إلى Freqtrade

- Pine غالباً يعتمد على repainting (استخدام بيانات الشمعة غير المكتملة أو `barstate.islast`)؛ Freqtrade يعمل على الشمعات المغلقة فقط وينفذ الصفقات عند افتتاح الشمعة التالية.
- Pine ينفذ منطقاً لكل شمعة (per-bar)؛ يجب تحويله إلى عمليات vectorized كاملة عبر pandas.
- تجنب نقل أي وصول للبيانات المستقبلية (shift سالب، aggregates بدون rolling، iloc).
- تجنب مؤشرات Pine التي تستخدم `security()` / `request.security()` بدون إعداد lookahead صحيح؛ استخدم `informative_pairs()` + `merge_informative_pair()` بدلاً منها.
- حدد `startup_candle_count` بدقة ليغطي أطول فترة مطلوبة (مثل 200 لـ SMA200).
- لا تترجم أوامر الرسم (`plot`) مباشرة؛ استخدم `enter_tag` / `exit_tag`.
- بعد كل تحويل: شغّل `lookahead-analysis` فوراً.
- تأكد من شرط `volume > 0` ومن تطابق الـ timeframe تماماً.

## ملاحظات هامة للمشروع

- شغّل `lookahead-analysis` + `recursive-analysis` بعد **كل** تعديل على الاستراتيجية وقبل أي اختبار OOS أو dry-run.
- استخدم دائماً `--export signals` + `backtesting-analysis` لتحليل أداء الـ tags والمؤشرات قبل اتخاذ قرارات تحسين.
- التزم الصارم بـ vectorized operations + `shift()` فقط داخل `populate_*` (لا iloc، لا loops، لا future data).
- استخدم StaticPairList و `--cache none` لضمان إعادة إنتاج النتائج في الباكتيست والـ validation.
- عند تحويل Pine: لا تنقل أي repainting logic، وتحقق من `volume > 0` و `startup_candle_count` و lookahead-analysis في كل خطوة.

---
**نهاية التقرير**
