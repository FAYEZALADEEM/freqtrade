# تقرير تحويل الاستراتيجية

**اسم الاستراتيجية الأصلية:** CRT_1AM_Strategy_V1_Pine_v6.pine  
**الملف الجديد:** user_data/strategies/CRT_1AM.py  
**تاريخ التحويل:** 2026-06-19  

## ما تم تحويله
- منطق CRT 1AM: نطاق 01:00 + sweep في 02:00 + إشارة عند نهاية sweep
- محاكاة توقيت NY (GMT-5) عبر ny_hour = (hour - 5) % 24
- swept_low / swept_high مع فلتر close inside و double sweep reject
- وقف خلف الـ purge + buffer
- أهداف mid + opposite (approximated في custom_exit)
- مرة واحدة يومياً (تقريبي)

## ملاحظات
- التوقيت حساس جداً. على بيانات Binance 15m قد يكون الـ hour mapping غير مثالي.
- لا partial position في هذه النسخة.
- can_short = False

## النتائج الأولية
93 trades, -0.1%, WR 48.4%
