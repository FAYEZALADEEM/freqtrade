# تقرير حالة المشروع - Freqtrade

**التاريخ:** 2026-06-19  
**الغرض:** فحص بنية المشروع الحالي فقط (قراءة بدون تعديل)

## 1. حالة config

- الملف الرئيسي: `user_data/config.json`
- `timeframe`: `"15m"`
- `exchange.name`: `"binance"`
- `pair_whitelist`: `["EUR/USDT"]`
- `trading_mode`: `"spot"`
- `stake_amount`: 100, `max_open_trades`: 3, `dry_run_wallet`: 1000
- **FreqAI مفعّل بالكامل**:
  - `"enabled": true`
  - `identifier`: `"eurusd_m15_hybrid_freqai_v1"`
  - `train_period_days`: 30, `backtest_period_days`: 7
  - يستخدم LightGBM (من الإعدادات)
- يوجد **عدة نسخ احتياطية** (config.json.bak_* كثيرة من تواريخ مختلفة في 18-19 يونيو).
- `dataformat_ohlcv`: `"feather"`
- لم يتم استخدام timerange ثابت في الـ config (يُحدد في سطر الأوامر).

## 2. الزوج والفريم المستخدمين

- الزوج الرئيسي: **EUR/USDT**
- الفريم: **15m**
- يطابق المتطلبات المحددة (EUR/USDT + 15m).

## 3. هل `EUR_USDT-15m.feather` موجود؟

**نعم** — موجود في:
- `/home/fayez/freqtrade/user_data/data/binance/EUR_USDT-15m.feather` (حجم ~2.4 ميجا، نوع feather)
- يوجد نسخ احتياطية أيضًا (`.bak_*`)
- ملفات أخرى: `BTC_USDT-15m.feather`

## 4. هل FreqAI مفعل؟

**نعم** — مفعّل في الـ config ومستخدم في الاستراتيجية الرئيسية.
- الـ identifier الحالي: `eurusd_m15_hybrid_freqai_v1`
- مجلد النماذج: `user_data/models/eurusd_m15_hybrid_freqai_v1/` (يحتوي مئات الملفات: pkl, json, feather).
- الاستراتيجية تستخدم `feature_engineering_expand_all`، `feature_engineering_expand_basic`، `feature_engineering_standard`، `set_freqai_targets`، و `self.freqai.start()`.

## 5. الاستراتيجيات الموجودة

في `user_data/strategies/`:
- **EURUSD_FreqAI_Hybrid.py** (الاستراتيجية الرئيسية والنشطة)
  - اسم الكلاس: `EURUSD_FreqAI_Hybrid`
  - `timeframe = "15m"`, `can_short = False`
  - تستخدم AI للدخول + ROI + stoploss للخروج (hybrid)
  - تحتوي على دعم/مقاومة آلية (auto SR بـ pivots + ATR)
  - يوجد **الكثير من النسخ الاحتياطية** (أكثر من 8 ملفات .bak_* بتواريخ مختلفة اليوم).
- `sample_strategy.py`
- `TestStrategy.py`
- مجلد `__pycache__/`

لا توجد استراتيجيات Pine-converted عادية (غير FreqAI) حالياً.

## 6. آخر نتائج backtest إن وجدت

- **أحدث backtest**: `backtest-result-2026-06-19_02-04-26.zip` + `.meta.json`
  - الاستراتيجية: **EURUSD_FreqAI_Hybrid**
  - الفريم: 15m
  - عدد الصفقات (total_trades): **253**
  - الربح الإجمالي: **0.001677** (~0.17%)
  - Win Rate: **42.69%**
  - Max Drawdown abs: **~2.733**
  - أفضل/أسوأ زوج: EUR/USDT (الوحيد)
  - متوسط مدة الصفقة: ~9:46:00
- يوجد العديد من ملفات الباكتيست السابقة اليوم (من 23:25 إلى 02:04).
- بعض التشغيلات استخدمت `--export signals` (يوجد signals.pkl + exited.pkl).

ملاحظة: بعض التحليلات السابقة أظهرت نتائج سلبية صغيرة.

## 7. آخر نتائج `group_*.csv` إن وجدت

**نعم** — الملفات موجودة في `user_data/backtest_results/`:
- `group_0.csv`
- `group_1.csv`
- `group_2.csv`
- `group_4.csv`
- `group_5.csv`

أمثلة من المحتوى (من تشغيل سابق اليوم):
- enter_reason شائع: `ai_leader_one_trade_per_day` (178 صفقة في عينة)
- exit_reason: `ai_exit`
- أرقام ربح إجمالي سلبية صغيرة في بعض الـ groups (مثال -2.72 على 178 صفقة في تحليل سابق).
- تم إنشاؤها بـ `--analysis-to-csv` و `--analysis-groups`.

يوجد أيضًا `last_ai_exit_disabled_run.log`.

## 8. الملفات الحساسة التي لا يجب تعديلها

- `user_data/config.json` (والعديد من .bak_*)
- `user_data/strategies/EURUSD_FreqAI_Hybrid.py` (وكل .bak_*)
- `user_data/data/binance/EUR_USDT-15m.feather` (والبيانات)
- `user_data/models/eurusd_m15_hybrid_freqai_v1/` (كل النماذج)
- `user_data/backtest_results/` (جميع الـ zip و الـ group_*.csv و الـ logs)
- `user_data/strategies/` ككل

**ممنوع التعديل** إلا بعد خطة + موافقة صريحة.

## 9. المخاطر الحالية

- الاستراتيجية الرئيسية **FreqAI hybrid** بالفعل (يخالف قاعدة "لا تضف FreqAI مباشرة قبل نجاح النسخة العادية").
- الكثير من التعديلات التجريبية السريعة (ملفات .bak كثيرة اليوم) → صعوبة تتبع النسخ النظيفة.
- نتائج الباكتيست الحديثة ضعيفة (Win Rate ~43%، ربح ضئيل أو سلبي في بعض التشغيلات، عدد صفقات معقول لكن أداء ضعيف).
- البيانات محملة تحت `binance/` رغم أن الزوج EURUSD (فوركس)، قد يؤثر على جودة الحجم.
- لا يوجد baseline نظيف لاستراتيجية عادية (غير FreqAI) حالياً.
- العديد من الباكتيستات الأخيرة لم تستخدم بالضبط الـ timerange المطلوب `20250101-20260101` + fee=0 دائمًا.
- خطر الـ lookahead في التطوير السريع (خاصة مع FreqAI + SR الآلي).
- pine_strategies يحتوي على 113 ملف .pine (معظمها استراتيجيات v6) لكن لم يتم تحويل أي منها بعد.

## ملخص سريع

| العنصر                  | الحالة                  | ملاحظات |
|-------------------------|-------------------------|--------|
| config                  | FreqAI مفعل            | + باكات كثيرة |
| الزوج/الفريم            | EUR/USDT 15m            | مطابق |
| بيانات EUR_USDT-15m     | موجودة                   | feather جيد |
| استراتيجيات             | FreqAI Hybrid رئيسية    | + عينات |
| آخر باكتيست             | 253 صفقة، +0.17%، WR 42.7% | DD ~2.73 |
| group_*.csv             | موجودة                    | من تحليلات حديثة |
| pine_strategies         | 113 ملف .pine            | + تقرير تحقق |

**تم الفحص بالقراءة فقط. لا تعديلات تمت.**

---

**المصادر التي تمت قراءتها:**
- user_data/config.json
- user_data/strategies/EURUSD_FreqAI_Hybrid.py (جزئياً)
- user_data/backtest_results/ (meta + zips + group_*.csv + log)
- user_data/data/binance/
- user_data/models/
- pine_strategies/ (تعداد + تقرير التحقق)

**التوصية:** لا تبدأ أي تحويل أو تعديل قبل مراجعة هذا التقرير والموافقة على المراحل التالية (خاصة إنشاء الأدوات في المرحلة 3).
