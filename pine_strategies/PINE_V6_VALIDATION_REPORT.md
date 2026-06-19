# تقرير تحقق Pine Script v6

| رقم | الملف | الاستراتيجية | تم إنشاؤه؟ | Pine v6؟ | Strategy؟ | Tooltips؟ | مجموعات عربية؟ | إشارات؟ | تنبيهات؟ | جاهز للنسخ؟ | ملاحظات |
| --: | ----- | ------------ | ---------- | -------- | --------- | --------- | -------------- | ------- | -------- | ----------- | ------- |
| 1 | strategy_01_crt_thick_candle_break.pine | CRT Thick Candle Break | نعم | نعم | نعم | نعم | نعم | نعم | نعم | نعم | يحتاج المستخدم لاحقًا ضبط تعريف thick candle وpivot حسب السوق. |
| 2 | strategy_02_ict_silver_bullet_liquidity_sweep_fvg.pine | ICT Silver Bullet - Liquidity Sweep + FVG Retest | نعم | نعم | نعم | نعم | نعم | نعم | نعم | نعم | FVG وliquidity sweep معرفان آليًا بتعليق واضح، وفلتر الجلسة معطل افتراضيًا. |
| 3 | strategy_03_smc_liquidity_grab_imbalance_ob.pine | SMC Liquidity Grab + Imbalance + Order Block | نعم | نعم | نعم | نعم | نعم | نعم | نعم | نعم | Order Block مبسط كآخر شمعة معاكسة قبل imbalance. |
| 4 | strategy_04_smc_order_block_bos.pine | SMC Order Block + BOS | نعم | نعم | نعم | نعم | نعم | نعم | نعم | نعم | BOS معرف كإغلاق فوق/تحت آخر pivot مؤكد. |
| 5 | strategy_05_fvg_inversion_trade.pine | FVG / FVG Inversion Trade | نعم | نعم | نعم | نعم | نعم | نعم | نعم | نعم | CE وFVG inversion معرفان دون lookahead. |
| 6 | strategy_06_breaker_block_retest.pine | Breaker Block Retest Strategy | نعم | نعم | نعم | نعم | نعم | نعم | نعم | نعم | breaker block معرف كمنطقة الشمعة السابقة للكسر. |
| 7 | strategy_07_opening_range_breakout.pine | Opening Range Breakout (ORB) | نعم | نعم | نعم | نعم | نعم | نعم | نعم | نعم | يحسب ORB من جلسة محددة، وفلتر التداول معطل افتراضيًا. |
| 8 | strategy_08_ma_pullback_trend_following.pine | Trend Following with MA Pullback | نعم | نعم | نعم | نعم | نعم | نعم | نعم | نعم | confirmation candle مبسطة كـ engulfing. |
| 9 | strategy_09_adx_ema_intraday_trend.pine | ADX-EMA Intraday Trend Strategy | نعم | نعم | نعم | نعم | نعم | نعم | نعم | نعم | يستخدم request.security بأمان مع lookahead_off لفلتر اليوم السابق الاختياري. |
| 10 | strategy_10_vwap_pullback.pine | VWAP Pullback | نعم | نعم | نعم | نعم | نعم | نعم | نعم | نعم | rejection candle عند VWAP معرف آليًا بتعليق. |
| 11 | strategy_11_one_hour_forex_reversal.pine | 1-Hour Forex Reversal Strategy | نعم | نعم | نعم | نعم | نعم | نعم | نعم | نعم | قواعد الشراء عكسية برمجيًا لأن التقرير ذكر البيع أساسًا. |
| 12 | strategy_12_rsi_divergence_reversal.pine | RSI Divergence Reversal | نعم | نعم | نعم | نعم | نعم | نعم | نعم | نعم | divergence وCHoCH مبسطان باستخدام pivots مؤكدة فقط. |

## نتيجة التحقق

- كل الملفات تبدأ بـ `//@version=6`.
- كل الملفات تستخدم `strategy()` ولا تستخدم `indicator()`.
- كل الملفات تحتوي إعدادات عربية مرقمة ومرفقة بـ `tooltip`.
- كل الملفات تحتوي تفعيل/تعطيل منفصل للشراء والبيع.
- فلتر الجلسة معطل افتراضيًا في كل الملفات.
- كل الملفات تحتوي `plotshape()` لإشارات الشراء والبيع.
- كل الملفات تحتوي `alertcondition()` للشراء والبيع.
- كل الملفات تحتوي `strategy.entry()` و`strategy.exit()` مع وقف وهدف.
- لم يتم استخدام `barstate.islast` أو `lookahead_on`.
- لا توجد ملفات Python أو Backtest Python ضمن هذا العمل.
