# أفضل ممارسات Freqtrade - تقرير مستخلص من التوثيق الرسمي

**التاريخ:** 2026-06-19  
**المصدر:** التوثيق الرسمي لـ Freqtrade (الصفحات المحددة)  
**ملاحظة:** هذا التقرير مستمد فقط من قراءة التوثيق الرسمي. لم يتم فحص أي ملفات محلية، لم يتم تعديل أي استراتيجية، لم يتم تعديل config، ولم يتم تشغيل أي أوامر (backtesting أو FreqAI).

## 1. أفضل ممارسات كتابة استراتيجية Freqtrade

- استخدم دالة `populate_indicators()` لإضافة المؤشرات فقط المستخدمة في الدخول/الخروج أو لمؤشرات أخرى (لتجنب إهدار الذاكرة والـ CPU).
- أعد دائماً الـ DataFrame كاملاً من `populate_*` functions دون إزالة أو تعديل الأعمدة الأساسية (`open`, `high`, `low`, `close`, `volume`).
- استخدم عمليات **vectorized** باستخدام pandas (مثل `dataframe.loc[(condition), 'enter_long'] = 1`). تجنب الـ loops على الصفوف والمقارنات البسيطة مثل `if dataframe['rsi'] > 30`.
- استخدم `dataframe['volume'] > 0` دائماً في شروط الدخول/الخروج لتجنب التداول في فترات بدون نشاط.
- حدد `startup_candle_count` بشكل صحيح (أكبر عدد شمعات مطلوب لحساب مؤشرات مستقرة). استخدم recursive-analysis للتحقق.
- استخدم `shift()` بدلاً من `iloc[-1]` أو الوصول المباشر للصفوف.
- استخدم `can_short = True` إذا كنت تريد الـ shorting، وحدد `enter_short` / `exit_short`.
- قم بتسمية الإشارات باستخدام `enter_tag` و `exit_tag` لتسهيل التحليل لاحقاً.
- لا تستخدم بيانات مستقبلية (future data) في populate functions.
- استخدم `INTERFACE_VERSION = 3`.
- للـ minimal_roi: استخدم قاموس يحدد الـ ROI حسب الوقت (بالدقائق). يمكن تعطيله بـ `{}`.
- للـ stoploss: حدد قيمة سالبة (مثل -0.10).
- استخدم `timeframe` بشكل صحيح (مثل "15m").

## 2. طريقة الباكتيست الصحيحة

- الأمر الأساسي: `freqtrade backtesting --strategy <StrategyName>`
- حدد `--timeframe` إذا لزم الأمر.
- استخدم `--strategy-list` لمقارنة استراتيجيات متعددة.
- حدد `--dry-run-wallet` أو `--starting-balance` للرصيد الأولي.
- استخدم `--datadir` لمصدر بيانات مختلف.
- **افتراضات التنفيذ في الباكتيست**: الإشارات تُولد عند إغلاق الشمعة، والصفقات تبدأ عند فتح الشمعة التالية.
- يجب توفر بيانات تاريخية مسبقاً (استخدم download-data).
- النتائج تُصدر افتراضياً إلى `user_data/backtest_results`.
- استخدم `--cache none` عند الحاجة لتجنب النتائج المخزنة القديمة.
- للـ dynamic pairlist: النتائج غير قابلة للتكرار دائماً، يُفضل StaticPairList.

## 3. طريقة استخدام `--timerange`

- يحدد نطاق البيانات المستخدمة في الباكتيست أو التحليل.
- أمثلة:
  - `--timerange=20190501-` : من 1 مايو 2019 فصاعداً.
  - `--timerange=-20180131` : حتى 31 يناير 2018.
  - `--timerange=20180131-20180301` : من 31 يناير إلى 1 مارس 2018.
  - `--timerange=1527595200-1527618600` : باستخدام POSIX timestamps.
- مفيد لتقليل حجم الاختبار أو اختبار فترات محددة.
- يؤثر أيضاً في backtesting-analysis و lookahead-analysis.

## 4. طريقة استخدام `--fee`

- يحدد رسوم مخصصة (override الرسوم الافتراضية من البورصة).
- القيمة كنسبة (ratio)، تُطبق مرتين (دخول + خروج).
- مثال: `--fee 0.001` لرسوم 0.1%.
- استخدم فقط عند التجربة أو عندما تكون هناك rebates غير مرئية في ccxt.
- الافتراضي: يأخذ الرسوم من معلومات السوق.

## 5. طريقة استخدام `--export signals`

- يُستخدم لتصدير الإشارات والصفقات للتحليل اللاحق.
- الأمر: `--export signals`
- ينتج ملفات مثل `backtest-result-*.pkl` (signals و exited).
- ضروري قبل تشغيل `backtesting-analysis`.
- يمكن تحديد `--backtest-directory` لمسار مخصص.
- استخدم `--cache none` قبل التشغيل التالي لتجنب الكاش.

## 6. طريقة استخدام `backtesting-analysis`

- الأمر: `freqtrade backtesting-analysis --analysis-groups 0 1 2 3 4 5`
- يقرأ آخر نتائج باكتيست.
- مجموعات التحليل:
  - 0: ملخص عام winrate/profit حسب enter_tag.
  - 1: حسب enter_tag.
  - 2: حسب enter_tag + exit_tag.
  - 3: حسب pair + enter_tag.
  - 4: حسب pair + enter_tag + exit_tag (قد يكون كبيراً).
  - 5: حسب exit_tag.
- خيارات مفيدة:
  - `--enter-reason-list` و `--exit-reason-list` لتصفية التاجات.
  - `--indicator-list` لعرض قيم المؤشرات على شمعات الإشارة (مثل rsi ema).
  - `--entry-only` / `--exit-only`.
  - `--rejected-signals` لعرض الإشارات المرفوضة.
  - `--analysis-to-csv` لتصدير إلى CSV.
  - `--timerange` لتصفية التواريخ.
  - `--backtest-filename` لتحليل نتيجة قديمة محددة.
- يساعد في تحليل أداء الـ tags وتعديل المؤشرات بدقة.

## 7. طريقة استخدام `lookahead-analysis`

- الأمر: `freqtrade lookahead-analysis --strategy <Name> ...`
- يكشف عن **lookahead bias** (استخدام بيانات مستقبلية).
- يقوم بباكتيست كامل ثم باكتيستات مقطوعة لكل إشارة ويقارن.
- خيارات خاصة:
  - `--minimum-trade-amount` و `--targeted-trade-amount`.
  - `--lookahead-analysis-exportfilename`.
  - `--allow-limit-orders` (يُفضل تجنبه لتجنب false positives).
- يُجبر بعض الإعدادات (cache=none، market orders، إلخ) لتجنب false positives.
- يدعم FreqAI أيضاً.

## 8. قواعد منع `lookahead bias`

- **لا تستخدم** `shift(-n)` أبداً (ينظر إلى المستقبل).
- **لا تستخدم** `df.iloc[-1]` أو الوصول المباشر لصفوف محددة في populate functions.
- تجنب for-loops غير المتحكم بها جيداً.
- تجنب دوال التجميع مثل `.mean()` / `.min()` / `.max()` بدون `rolling()` (تحسب على كامل الـ dataframe).
- تجنب `ta.MACD(dataframe, 12, 26, 1)` (signalperiod=1 يسبب bias).
- استخدم `rolling(window)` للحسابات التاريخية.
- استخدم `lookahead-analysis` دائماً قبل الـ dry/live.
- في الـ backtesting تمرر كل البيانات دفعة واحدة → يجب الحذر الشديد.
- استخدم recursive-analysis للتحقق من الـ startup indicators.

## 9. قواعد FreqAI

- **الميزات (features)**: يجب أن تبدأ بـ `%` (مثل `dataframe["%-rsi-period"] = ...`). هذا يميزها لـ FreqAI.
- **الأهداف (targets)**: يجب أن تبدأ بـ `&` (مثل `dataframe["&-s_close"] = ...`).
- استخدم الدوال الخاصة:
  - `feature_engineering_expand_all()`: تُوسع تلقائياً على `indicator_periods_candles` + timeframes + shifted + corr pairs.
  - `feature_engineering_expand_basic()`: توسع على timeframes + shifted + corr (بدون periods).
  - `feature_engineering_standard()`: تُستدعى مرة واحدة على الـ base timeframe (للميزات الخاصة مثل يوم الأسبوع).
  - `set_freqai_targets()`: **مطلوبة** لتعريف الـ targets.
- استخدم `metadata` داخل الدوال (`metadata["pair"]`, `metadata["tf"]`, `metadata["period"]`) للتحكم الدقيق.
- في الـ config:
  - `"include_timeframes"`, `"include_corr_pairlist"`, `"include_shifted_candles"`, `"indicator_periods_candles"`, `"label_period_candles"`.
- استخدم pipeline مخصص إذا لزم (DataSieve).
- للـ targets: استخدم `shift(-label_period_candles)` مع rolling mean.
- يمكن إرجاع قيم إضافية عبر `dk.data['extra_returns_per_train']`.
- Weighting: استخدم `weight_factor` لإعطاء وزن أكبر للبيانات الحديثة.

## 10. الأخطاء التي يجب تجنبها عند تحويل Pine Script إلى Freqtrade

- Pine يعتمد غالباً على "repainting" (استخدام بيانات غير مكتملة) — Freqtrade لا يسمح بذلك (فقط شمعات مكتملة).
- تجنب الاعتماد على `barstate.islast` أو الوصول للمستقبل.
- في Pine غالباً حسابات على bar واحد — في Freqtrade يجب vectorization على كامل الـ dataframe.
- لا تستخدم مؤشرات تبدو إلى الأمام (مثل بعض security calls بدون تأخير).
- الفرق في الـ execution: Pine قد ينفذ على close، لكن Freqtrade يفترض تنفيذ على next open.
- تجنب الحسابات التي تشمل الشمعة الحالية غير المكتملة.
- في التحويل: تأكد من أن كل شرط يستخدم بيانات حتى الـ close السابق فقط.
- لا تترجم "plot" مباشرة؛ استخدم enter/exit tags بدلاً من ذلك.
- الـ volume و liquidity يختلفان (خاصة في forex مثل EURUSD).

## 11. ملاحظات خاصة بتحويل Pine Script v6 إلى Freqtrade Python

- Pine v6 لديه تحسينات في security() و request.security() — تحتاج محاكاة دقيقة بـ informative pairs أو `merge_informative_pair`.
- تجنب `ta.macd(..., signal=1)` أو أي param يسبب lookahead.
- في v6 بعض الـ functions تستخدم barstate — يجب استبدالها بـ shift أو conditions على الـ dataframe.
- استخدم `qtpylib` أو pandas_ta أو ta-lib لمحاكاة المؤشرات.
- تأكد من `startup_candle_count` يغطي أطول فترة مطلوبة (مثل sma 200 = 200 شمعة).
- في Pine v6 هناك `barstate` و `request.security` مع lookahead — يجب تجنبها تماماً.
- استخدم `feature_engineering_*` إذا كنت تستخدم FreqAI.
- الاختبار: استخدم lookahead-analysis بعد كل تحويل.
- الـ timeframe في Pine vs Freqtrade: تأكد من التطابق.

## 12. ملاحظات خاصة باختبار EURUSD داخل Freqtrade باسم `EUR/USDT`

- استخدم الزوج كـ `"EUR/USDT"` في config (pair_whitelist).
- البيانات عادة تُحمل تحت `user_data/data/binance/` أو exchange المحدد (حتى لو كانت forex).
- قد يؤثر "حجم" البيانات (volume) على بعض المؤشرات — تأكد من أن الاستراتيجية لا تعتمد عليه بشكل أساسي إذا كانت البيانات محضرة.
- استخدم `--pairs EUR/USDT` في الأوامر.
- timerange و fee=0 شائعان في مثل هذه الاختبارات.
- تأكد من `trading_mode: spot` (أو futures إذا لزم).
- في FreqAI: تأكد من `include_timeframes` مناسب للـ M15.
- الـ slippage والـ fees: استخدم --fee 0 للاختبار النقي.
- الـ pairlist: StaticPairList هو الأفضل لإعادة الإنتاج.
- تحقق من توفر البيانات بـ download-data إذا لزم.
- في التحليل: استخدم backtesting-analysis مع --pairs EUR/USDT.

## ملاحظات عامة إضافية

- **دائماً**: شغّل lookahead-analysis + recursive-analysis قبل أي dry/live.
- استخدم `--export signals` + backtesting-analysis لفهم الـ tags والمؤشرات.
- في FreqAI: الميزات `%` والأهداف `&` إلزامية.
- تجنب الـ future data في كل الأوقات.
- التوثيق يؤكد: الباكتيست ليس ضماناً — استخدم dry-run دائماً أولاً.

هذا التقرير يلخص أهم النقاط من التوثيق الرسمي للاستخدام في المراحل القادمة (تحويل Pine إلى Freqtrade).

---

**نهاية التقرير**
