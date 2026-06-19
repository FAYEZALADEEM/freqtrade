#!/usr/bin/env python3
"""
أداة تشغيل lookahead-analysis موحدة حسب القواعد.

الاستخدام:
    python tools/run_lookahead_analysis.py --strategy MyStrategy
"""

import argparse
import subprocess
from datetime import datetime
from pathlib import Path


REPORTS_DIR = Path("reports/lookahead")
CONFIG = "user_data/config.json"
PAIR = "EUR/USDT"
TIMEFRAME = "15m"
TIMERANGE = "20250101-20260101"
FEE = "0"


def run_lookahead(strategy_name: str) -> dict:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    output_file = REPORTS_DIR / f"{strategy_name}_lookahead.md"

    cmd = [
        "/home/fayez/freqtrade/.venv/bin/freqtrade",
        "lookahead-analysis",
        "--config",
        CONFIG,
        "--config",
        '<(echo \'{"freqai": {"enabled": false}}\')',
        "--config",
        '<(echo \'{"entry_pricing": {"price_side": "other"}, "exit_pricing": {"price_side": "other"}}\')',
        "--strategy",
        strategy_name,
        "--timeframe",
        TIMEFRAME,
        "--timerange",
        TIMERANGE,
        "--fee",
        FEE,
        "--targeted-trade-amount",
        "100",
        "-p",
        PAIR,
    ]

    print("▶ تشغيل lookahead-analysis:")
    print(" ".join(cmd))
    print("-" * 60)

    try:
        # استخدام bash لدعم process substitution للـ override
        full_cmd = " ".join(cmd)
        result = subprocess.run(
            ["bash", "-c", full_cmd], capture_output=True, text=True, timeout=3600
        )
        stdout = result.stdout
        stderr = result.stderr
        combined_output = stdout + ("\n" + stderr if stderr else "")
        return_code = result.returncode
    except Exception as e:
        return {"success": False, "error": str(e)}

    # حفظ التقرير
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# تقرير Lookahead Analysis: {strategy_name}\n\n")
        f.write(f"**التاريخ:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**الأمر:**\n```\n{' '.join(cmd)}\n```\n\n")
        f.write("## قاعدة التحقق المطبقة\n\n")
        f.write("- `targeted_trade_amount = 100` (ثابت حسب القاعدة الدائمة)\n")
        f.write("- يتم فحص حتى 100 إشارة. إذا كان عدد الإشارات أقل، يتم التوضيح.\n\n")
        f.write("## النتائج\n\n")
        f.write("```\n")
        f.write(combined_output)
        f.write("\n```\n\n")
        f.write(f"\n**رمز الخروج:** {return_code}\n")

    return {
        "success": return_code == 0 and "Lookahead Analysis" in combined_output,
        "report_path": str(output_file),
        "has_bias": "│      Yes │" in combined_output,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strategy", "-s", required=True)
    args = parser.parse_args()

    res = run_lookahead(args.strategy)
    print("\n✅ تم حفظ التقرير:" if res.get("success") else "\n❌ فشل")
    print(res.get("report_path", ""))


if __name__ == "__main__":
    main()
