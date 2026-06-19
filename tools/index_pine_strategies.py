#!/usr/bin/env python3
"""
أداة فهرسة استراتيجيات Pine Script v6
تقوم بفحص كل ملفات .pine في pine_strategies/ وتستخرج معلومات مهمة للتحويل.

الاستخدام:
    python tools/index_pine_strategies.py
"""

import csv
import re
from datetime import datetime
from pathlib import Path


PINE_DIR = Path("pine_strategies")
REPORTS_DIR = Path("reports")
CSV_PATH = REPORTS_DIR / "pine_index.csv"
MD_PATH = REPORTS_DIR / "pine_index.md"


def analyze_pine_file(file_path: Path) -> dict:
    """تحليل ملف Pine واحد واستخراج الخصائص المهمة."""
    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return {"error": str(e)}

    lower = content.lower()

    # إصدار Pine
    version_match = re.search(r"//@version\s*=\s*([0-9.]+)", content)
    pine_version = version_match.group(1) if version_match else "unknown"

    # نوع الملف: strategy أو indicator
    is_strategy = bool(re.search(r"\bstrategy\s*\(", content))
    is_indicator = bool(re.search(r"\bindicator\s*\(", content))

    # request.security (فريم أعلى)
    has_request_security = "request.security" in lower

    # pivothigh / pivotlow
    has_pivothigh = bool(re.search(r"\bpivothigh\b", lower))
    has_pivotlow = bool(re.search(r"\bpivotlow\b", lower))
    has_pivots = has_pivothigh or has_pivotlow

    # دعم/مقاومة يدوي محتمل (خطوط، var، أسماء شائعة)
    manual_sr_indicators = [
        "line.new",
        "line.set",
        "support",
        "resistance",
        "sr_level",
        "manual_support",
        "manual_resistance",
        "plotshape.*support",
        "plotshape.*resistance",
    ]
    has_manual_sr = any(ind in lower for ind in manual_sr_indicators) or bool(
        re.search(r"\bvar\b.*(support|resistance|sr)", lower)
    )

    # long / short
    has_long = "long" in lower or "buy" in lower or "strategy.entry" in lower
    has_short = "short" in lower or "sell" in lower or "strategy.exit" in lower

    # strategy.entry / strategy.exit
    has_strategy_entry = "strategy.entry" in lower
    has_strategy_exit = "strategy.exit" in lower
    has_entry_exit = has_strategy_entry or has_strategy_exit

    # وجود request.security مع higher timeframe
    uses_higher_tf = has_request_security

    # تقدير درجة قابلية التحويل (0-100)
    score = 80
    if has_request_security:
        score -= 20
    if has_manual_sr:
        score -= 25
    if has_pivots:
        score += 10  # pivots جيدة للتحويل إلى آلية
    if not has_entry_exit:
        score -= 15
    if not is_strategy:
        score -= 10
    if uses_higher_tf:
        score -= 10
    score = max(0, min(100, score))

    # اقتراح نوع التحويل
    if score >= 80:
        conversion = "A - قابلة مباشرة"
    elif score >= 60:
        conversion = "B - تحتاج تعديل بسيط (pivots/manual sr)"
    elif score >= 40:
        conversion = "C - تحتاج إعادة بناء"
    else:
        conversion = "D - غير مناسبة"

    return {
        "file": file_path.name,
        "path": str(file_path),
        "pine_version": pine_version,
        "is_strategy": is_strategy,
        "is_indicator": is_indicator,
        "has_request_security": has_request_security,
        "has_pivothigh": has_pivothigh,
        "has_pivotlow": has_pivotlow,
        "has_manual_sr": has_manual_sr,
        "has_long": has_long,
        "has_short": has_short,
        "has_strategy_entry": has_strategy_entry,
        "has_strategy_exit": has_strategy_exit,
        "conversion_category": conversion,
        "convertibility_score": score,
    }


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    pine_files = sorted(PINE_DIR.glob("*.pine"))
    if not pine_files:
        print("لم يتم العثور على أي ملفات .pine")
        return

    results = []
    for f in pine_files:
        info = analyze_pine_file(f)
        results.append(info)
        print(f"✓ تم تحليل: {f.name} (score={info.get('convertibility_score', 0)})")

    # كتابة CSV
    if results:
        fieldnames = list(results[0].keys())
        with open(CSV_PATH, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print(f"\nتم حفظ CSV: {CSV_PATH}")

    # كتابة تقرير MD
    with open(MD_PATH, "w", encoding="utf-8") as md:
        md.write("# فهرس استراتيجيات Pine Script v6\n\n")
        md.write(f"**التاريخ:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        md.write(f"**عدد الملفات:** {len(results)}\n\n")

        # إحصائيات
        strategies = sum(1 for r in results if r.get("is_strategy"))
        indicators = sum(1 for r in results if r.get("is_indicator"))
        has_security = sum(1 for r in results if r.get("has_request_security"))
        has_pivots = sum(1 for r in results if r.get("has_pivothigh") or r.get("has_pivotlow"))
        has_manual = sum(1 for r in results if r.get("has_manual_sr"))
        high_score = sum(1 for r in results if r.get("convertibility_score", 0) >= 80)

        md.write("## الإحصائيات\n\n")
        md.write(f"- إجمالي الملفات: {len(results)}\n")
        md.write(f"- استراتيجيات (strategy): {strategies}\n")
        md.write(f"- مؤشرات (indicator): {indicators}\n")
        md.write(f"- تستخدم request.security: {has_security}\n")
        md.write(f"- تستخدم pivothigh/pivotlow: {has_pivots}\n")
        md.write(f"- دعم/مقاومة يدوية محتملة: {has_manual}\n")
        md.write(f"- قابلة للتحويل مباشرة (score >= 80): {high_score}\n\n")

        # جدول مختصر
        md.write("## أفضل 10 ملفات قابلة للتحويل (حسب الدرجة)\n\n")
        sorted_results = sorted(
            results, key=lambda x: x.get("convertibility_score", 0), reverse=True
        )
        md.write(
            "| الملف | الإصدار | Strategy؟ | request.security | Pivots | Manual SR | Score | الفئة |\n"
        )
        md.write(
            "|-------|---------|-----------|------------------|--------|-----------|-------|-------|\n"
        )
        for r in sorted_results[:10]:
            md.write(
                f"| {r['file']} | {r['pine_version']} | {r['is_strategy']} | {r['has_request_security']} | {r['has_pivothigh'] or r['has_pivotlow']} | {r['has_manual_sr']} | {r['convertibility_score']} | {r['conversion_category']} |\n"
            )

        md.write("\n## ملخص الفئات\n\n")
        for cat in [
            "A - قابلة مباشرة",
            "B - تحتاج تعديل بسيط (pivots/manual sr)",
            "C - تحتاج إعادة بناء",
            "D - غير مناسبة",
        ]:
            count = sum(1 for r in results if r.get("conversion_category") == cat)
            md.write(f"- {cat}: {count}\n")

        md.write(
            "\n> **ملاحظة:** هذا التحليل آلي أولي. يحتاج تحليل يدوي لكل استراتيجية قبل التحويل.\n"
        )

    print(f"تم حفظ التقرير: {MD_PATH}")
    print(f"\nإجمالي الملفات المفهرسة: {len(results)}")


if __name__ == "__main__":
    main()
