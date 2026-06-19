#!/usr/bin/env python3
"""
أداة تشغيل باكتيست موحدة حسب القواعد:
- pair: EUR/USDT
- timeframe: 15m
- timerange: 20250101-20260101
- fee: 0
- export: signals
- cache: none

الاستخدام:
    python tools/run_strategy_backtest.py --strategy MyStrategy
"""

import argparse
import subprocess
from datetime import datetime
from pathlib import Path


REPORTS_DIR = Path("reports/backtests")
CONFIG = "user_data/config.json"
PAIR = "EUR/USDT"
TIMEFRAME = "15m"
TIMERANGE = "20250101-20260101"
FEE = "0"


def run_backtest(strategy_name: str) -> dict:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    cmd = [
        "/home/fayez/freqtrade/.venv/bin/freqtrade",
        "backtesting",
        "--config",
        CONFIG,
        "--config",
        '<(echo \'{"freqai": {"enabled": false}}\')',
        "--strategy",
        strategy_name,
        "--timeframe",
        TIMEFRAME,
        "--timerange",
        TIMERANGE,
        "--fee",
        FEE,
        "--export",
        "signals",
        "--cache",
        "none",
        "-p",
        PAIR,
    ]

    print("▶ تشغيل الأمر:")
    print(" ".join(cmd))
    print("-" * 60)

    try:
        full_cmd = " ".join(cmd)
        result = subprocess.run(
            ["bash", "-c", full_cmd],
            capture_output=True,
            text=True,
            timeout=3600,
        )
        stdout = result.stdout
        stderr = result.stderr
        return_code = result.returncode
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "انتهت المهلة الزمنية (1 ساعة)",
            "command": " ".join(cmd),
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "command": " ".join(cmd),
        }

    # حفظ الإخراج الكامل
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = REPORTS_DIR / f"{strategy_name}_{timestamp}.log"
    log_file.write_text(stdout + "\n\nSTDERR:\n" + stderr, encoding="utf-8")

    # استخراج ملخص بسيط
    summary_lines = []
    for line in stdout.splitlines():
        if any(
            kw in line
            for kw in ["BACKTESTING REPORT", "TOTAL", "Trades", "Win", "Profit", "Drawdown", "Win%"]
        ):
            summary_lines.append(line)

    summary_text = (
        "\n".join(summary_lines)
        if summary_lines
        else "لم يتم استخراج ملخص واضح. راجع الملف الكامل."
    )

    # كتابة ملخص
    summary_path = REPORTS_DIR / f"{strategy_name}_summary.md"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(f"# ملخص باكتيست: {strategy_name}\n\n")
        f.write(f"**التاريخ:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**الأمر المستخدم:**\n```\n{' '.join(cmd)}\n```\n\n")
        f.write("## النتائج الرئيسية\n\n")
        f.write("```\n")
        f.write(summary_text)
        f.write("\n```\n\n")
        f.write(f"**رمز الخروج:** {return_code}\n")
        f.write(f"**ملف السجل الكامل:** {log_file}\n\n")
        f.write("---\n")
        f.write("**ملاحظة:** استخدم أداة run_backtesting_analysis.py بعد هذا التشغيل.\n")

    return {
        "success": return_code == 0,
        "command": " ".join(cmd),
        "summary_path": str(summary_path),
        "log_path": str(log_file),
        "stdout_head": stdout[:2000],
    }


def main():
    parser = argparse.ArgumentParser(description="تشغيل باكتيست موحد لاستراتيجية")
    parser.add_argument("--strategy", "-s", required=True, help="اسم كلاس الاستراتيجية")
    args = parser.parse_args()

    print(f"بدء باكتيست للاستراتيجية: {args.strategy}")
    res = run_backtest(args.strategy)

    if res.get("success"):
        print("\n✅ تم الباكتيست بنجاح")
        print(f"ملخص محفوظ في: {res['summary_path']}")
    else:
        print("\n❌ فشل الباكتيست")
        print(res.get("error", "خطأ غير معروف"))
        print("راجع السجل.")

    if "stdout_head" in res:
        print("\n--- بداية الإخراج ---")
        print(res["stdout_head"][:1500])
        print("... (انظر الملف الكامل)")


if __name__ == "__main__":
    main()
