#!/usr/bin/env python3
"""
أداة تشغيل backtesting-analysis موحدة.

تستخدم:
- analysis-groups: 0 1 2 4 5
- --analysis-to-csv

الاستخدام:
    python tools/run_backtesting_analysis.py --strategy MyStrategy
"""

import argparse
import shutil
import subprocess
from datetime import datetime
from pathlib import Path


REPORTS_DIR = Path("reports/analysis")
CONFIG = "user_data/config.json"
GROUPS = ["0", "1", "2", "4", "5"]


def run_analysis(strategy_name: str) -> dict:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    strategy_dir = REPORTS_DIR / strategy_name
    strategy_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "/home/fayez/freqtrade/.venv/bin/freqtrade",
        "backtesting-analysis",
        "--config",
        CONFIG,
        "--analysis-groups",
        *GROUPS,
        "--analysis-to-csv",
        "--analysis-csv-path",
        str(strategy_dir),
    ]

    print("▶ تشغيل تحليل الباكتيست:")
    print(" ".join(cmd))
    print("-" * 60)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        stdout = result.stdout
        stderr = result.stderr
    except Exception as e:
        return {"success": False, "error": str(e)}

    # نسخ group_*.csv إذا كانت في مكان آخر (احتياطي)
    backtest_results = Path("user_data/backtest_results")
    for g in ["group_0.csv", "group_1.csv", "group_2.csv", "group_4.csv", "group_5.csv"]:
        src = backtest_results / g
        if src.exists():
            shutil.copy2(src, strategy_dir / g)

    # كتابة ملخص
    summary_path = strategy_dir / "analysis_summary.md"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(f"# تحليل باكتيست: {strategy_name}\n\n")
        f.write(f"**التاريخ:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**الأمر:**\n```\n{' '.join(cmd)}\n```\n\n")
        f.write("## الإخراج\n\n")
        f.write("```\n")
        f.write(stdout[-3000:] if len(stdout) > 3000 else stdout)
        f.write("\n```\n\n")
        if stderr:
            f.write("## أخطاء\n\n")
            f.write(stderr[:1000])
        f.write("\n\n**الملفات المحفوظة في:** " + str(strategy_dir) + "\n")

    return {
        "success": True,
        "summary_path": str(summary_path),
        "output_dir": str(strategy_dir),
        "stdout_tail": stdout[-1500:],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strategy", "-s", required=True)
    args = parser.parse_args()

    res = run_analysis(args.strategy)
    if res.get("success"):
        print(f"\n✅ التحليل مكتمل. الملخص: {res['summary_path']}")
    else:
        print("❌ فشل:", res.get("error"))


if __name__ == "__main__":
    main()
