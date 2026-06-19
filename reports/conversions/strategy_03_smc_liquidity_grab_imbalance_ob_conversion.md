# تقرير تحويل الاستراتيجية

**اسم الاستراتيجية الأصلية:** strategy_03_smc_liquidity_grab_imbalance_ob.pine  
**الملف الجديد:** user_data/strategies/SMC_LiquidityGrab_ImbalanceOB.py  
**تاريخ التحويل:** 2026-06-19  

## ما تم تحويله
- Liquidity Sweep + Imbalance (FVG + impulse candle body > ATR*mult)
- Trend filter EMA (افتراضي مفعل)
- SL = max(pips, ATR*0.5) تقريبي
- RR = 2.0
- enter_tag smc_grab_long/short

## ملاحظات
- تم تخفيف شرط لون الشمعة السابقة للحصول على إشارات (كان يعطي صفر صفقات)
- can_short = False
- لا lookahead

## الخطوات
تم الباكتيست + analysis + lookahead.
