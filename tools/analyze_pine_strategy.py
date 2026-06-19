#!/usr/bin/env python3
"""
أداة تحليل مفصل لاستراتيجية Pine Script واحدة.

الاستخدام:
    python tools/analyze_pine_strategy.py --file pine_strategies/strategy_01_crt_thick_candle_break.pine
    أو
    python tools/analyze_pine_strategy.py pine_strategies/xxx.pine
"""

import argparse
import re
from datetime import datetime
from pathlib import Path


REPORTS_DIR = Path("reports/pine_analysis")


def extract_inputs(content: str) -> list:
    """استخراج المدخلات (inputs)."""
    inputs = re.findall(r"(\w+)\s*=\s*input\.[a-z]+\s*\(([^)]+)\)", content, re.IGNORECASE)
    return [f"{name} = input...({params.strip()})" for name, params in inputs]


def extract_indicators(content: str) -> list:
    """استخراج المؤشرات الشائعة."""
    indicators = []
    patterns = [
        r"(ta\.[a-z_]+|ta\.[a-z]+\([^)]+\))",
        r"(rsi|ema|sma|macd|atr|bb|bollinger|vwap|adx|stoch|cci|momentum)\s*\(",
    ]
    for p in patterns:
        matches = re.findall(p, content, re.IGNORECASE)
        indicators.extend(matches)
    # إزالة التكرارات مع الحفاظ على الترتيب
    seen = set()
    unique = []
    for i in indicators:
        if i not in seen:
            seen.add(i)
            unique.append(i)
    return unique[:25]  # حد أقصى


def extract_entry_conditions(content: str) -> list:
    """محاولة استخراج شروط الدخول."""
    conditions = []
    # ابحث عن أجزاء تحتوي strategy.entry أو long أو buy
    entry_blocks = re.findall(
        r"(strategy\.entry[^}]+|if\s+[^:]+:\s*\n[^}]+?(?:long|buy|enter))",
        content,
        re.IGNORECASE | re.DOTALL,
    )
    for block in entry_blocks[:5]:
        clean = " ".join(block.split())[:300]
        conditions.append(clean)
    return conditions or ["لم يتم استخراج شروط دخول واضحة (تحقق يدوي مطلوب)"]


def extract_exit_conditions(content: str) -> list:
    """استخراج شروط الخروج."""
    exits = []
    exit_blocks = re.findall(
        r"(strategy\.exit[^}]+|if\s+[^:]+:\s*\n[^}]+?(?:exit|close|sell|short))",
        content,
        re.IGNORECASE | re.DOTALL,
    )
    for block in exit_blocks[:5]:
        clean = " ".join(block.split())[:300]
        exits.append(clean)
    return exits or ["لم يتم استخراج شروط خروج واضحة"]


def analyze_file(pine_path: Path) -> dict:
    content = pine_path.read_text(encoding="utf-8", errors="ignore")
    lower = content.lower()

    name = pine_path.stem

    version_match = re.search(r"//@version\s*=\s*([0-9.]+)", content)
    pine_version = version_match.group(1) if version_match else "?"

    is_strategy = bool(re.search(r"\bstrategy\s*\(", content))

    inputs = extract_inputs(content)
    indicators = extract_indicators(content)
    entry_conds = extract_entry_conditions(content)
    exit_conds = extract_exit_conditions(content)

    has_security = "request.security" in lower
    has_pivots = bool(re.search(r"pivothigh|pivotlow", lower))
    has_manual_sr = bool(re.search(r"line\.new|support|resistance|var .*sr", lower))
    has_var = "var " in lower

    has_long = "long" in lower or "strategy.entry" in lower
    has_short = "short" in lower and "strategy" in lower

    # مخاطر محتملة
    risks = []
    if has_security:
        risks.append("request.security - يحتاج تحويل إلى informative_pairs")
    if has_manual_sr:
        risks.append("دعم/مقاومة يدوية - يفضل استبدال بـ Pivot + ATR")
    if has_var:
        risks.append("var / حالة محفوظة - قد تحتاج logic معقدة في Python")
    if re.search(r"shift\s*\(\s*-\s*\d", lower):
        risks.append("shift سلبي محتمل - خطر lookahead!")

    # أعمدة مطلوبة محتملة
    required_cols = ["open", "high", "low", "close", "volume"]
    if has_pivots:
        required_cols += ["pivot_high", "pivot_low"]
    if "atr" in str(indicators).lower():
        required_cols.append("atr")

    return {
        "name": name,
        "file": pine_path.name,
        "pine_version": pine_version,
        "is_strategy": is_strategy,
        "inputs": inputs,
        "indicators": indicators,
        "entry_conditions": entry_conds,
        "exit_conditions": exit_conds,
        "has_request_security": has_security,
        "has_pivots": has_pivots,
        "has_manual_sr": has_manual_sr,
        "has_var": has_var,
        "has_long": has_long,
        "has_short": has_short,
        "risks": risks,
        "suggested_columns": list(set(required_cols)),
        "enter_tag_suggestion": f"pine_{name.lower()[:20]}",
        "exit_tag_suggestion": f"exit_pine_{name.lower()[:20]}",
    }


def generate_report(data: dict, output_path: Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# تحليل Pine Script: {data['name']}\n\n")
        f.write(f"**الملف الأصلي:** {data['file']}\n")
        f.write(f"**الإصدار:** Pine v{data['pine_version']}\n")
        f.write(f"**نوع:** {'Strategy' if data['is_strategy'] else 'Indicator'}\n")
        f.write(f"**تاريخ التحليل:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")

        f.write("## 1. المدخلات (Inputs)\n\n")
        if data["inputs"]:
            for inp in data["inputs"]:
                f.write(f"- `{inp}`\n")
        else:
            f.write("لا توجد مدخلات واضحة.\n")

        f.write("\n## 2. المؤشرات المستخدمة\n\n")
        for ind in data["indicators"][:15]:
            f.write(f"- {ind}\n")

        f.write("\n## 3. شروط الدخول (Long/Short)\n\n")
        for c in data["entry_conditions"]:
            f.write(f"```\n{c}\n```\n")

        f.write("\n## 4. شروط الخروج\n\n")
        for c in data["exit_conditions"]:
            f.write(f"```\n{c}\n```\n")

        f.write("\n## 5. المخاطر والعناصر الصعبة في التحويل\n\n")
        if data["risks"]:
            for r in data["risks"]:
                f.write(f"- ⚠️ {r}\n")
        else:
            f.write("- لا توجد مخاطر واضحة في التحليل الآلي.\n")

        f.write("\n## 6. معلومات إضافية\n\n")
        f.write(f"- يستخدم `request.security`: {data['has_request_security']}\n")
        f.write(f"- يستخدم pivothigh/pivotlow: {data['has_pivots']}\n")
        f.write(f"- دعم/مقاومة يدوية محتملة: {data['has_manual_sr']}\n")
        f.write(f"- يستخدم `var`: {data['has_var']}\n")
        f.write(f"- يدعم Long: {data['has_long']}\n")
        f.write(f"- يدعم Short: {data['has_short']}\n")

        f.write("\n## 7. الأعمدة المقترحة في DataFrame\n\n")
        f.write(", ".join(data["suggested_columns"]) + "\n")

        f.write("\n## 8. enter_tag / exit_tag المقترحة\n\n")
        f.write(f"- enter_tag: `{data['enter_tag_suggestion']}`\n")
        f.write(f"- exit_tag: `{data['exit_tag_suggestion']}`\n")

        f.write("\n## 9. ملاحظات التحويل\n\n")
        f.write("- استبدل pivothigh/pivotlow بـ `ta.pivothigh` / `ta.pivotlow` مع تأكيد (bars).\n")
        f.write("- حوّل request.security إلى `informative_pairs` + merge أو FreqAI.\n")
        f.write("- الدعم/المقاومة اليدوية → استخدم rolling max/min + ATR tolerance.\n")
        f.write("- تجنب أي shift سلبي أو iloc مستقبلي.\n\n")

        f.write("---\n")
        f.write(
            "**تحذير:** هذا التحليل آلي جزئي. يجب مراجعة الكود الأصلي يدويًا قبل كتابة الاستراتيجية في Python.\n"
        )


def main():
    parser = argparse.ArgumentParser(description="تحليل مفصل لملف Pine Script")
    parser.add_argument("file", nargs="?", help="مسار ملف .pine")
    parser.add_argument("--file", dest="file_flag", help="مسار ملف .pine")
    args = parser.parse_args()

    pine_file = args.file or args.file_flag
    if not pine_file:
        print("الرجاء تحديد مسار الملف: python tools/analyze_pine_strategy.py --file <path>")
        return

    pine_path = Path(pine_file)
    if not pine_path.exists():
        print(f"الملف غير موجود: {pine_path}")
        return

    print(f"جاري تحليل: {pine_path.name} ...")
    data = analyze_file(pine_path)

    output_file = REPORTS_DIR / f"{pine_path.stem}.md"
    generate_report(data, output_file)

    print(f"✅ تم إنشاء التقرير: {output_file}")


if __name__ == "__main__":
    main()
