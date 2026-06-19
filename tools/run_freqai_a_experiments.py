#!/usr/bin/env python3
"""
tools/run_freqai_a_experiments.py

Automates FreqAI experiments for selected Class A strategies.

- Creates/ensures _FreqAI.py (manual pre-creation recommended)
- Runs backtests for 2025 ref, 2024 OOS, 2026 partial OOS using config overrides (no main config touch)
- Runs backtesting-analysis + lookahead-analysis (--targeted-trade-amount 100)
- Saves logs + results to reports/freqai_experiments/<STRAT>/
- Builds freqai_leaderboard.csv / .md + freqai_summary.md

Usage (start small):
  python tools/run_freqai_a_experiments.py --strats LIB_STR045 LIB_STR012

Full later:
  python tools/run_freqai_a_experiments.py

Requires: FreqAI strategies *_FreqAI.py already in user_data/strategies/
"""

import argparse
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path("/home/fayez/freqtrade")
FREQTRADE_BIN = ROOT / ".venv/bin/freqtrade"
USER_CONFIG = ROOT / "user_data/config.json"
BASE_OVERRIDE = ROOT / "reports/freqai_experiments/tmp_configs/freqai_base_override.json"
EXPERIMENTS_DIR = ROOT / "reports/freqai_experiments"

# Periods
PERIODS = [
    ("2025_REF", "20250101-20260101"),
    ("2024_OOS", "20240101-20250101"),
    ("2026_OOS", "20260101-20260520"),
]

# Target strategies (start with these two)
DEFAULT_STRATS = [
    "LIB_STR045",
    "LIB_STR012",
    # Add more later:
    # "LIB_STR007", "LIB_STR013", "LIB_STR030", "LIB_STR005_EMA", "LIB_STR005", "LIB_STR003", "LIB_STR026"
]

PAIR = "EUR/USDT"
TIMEFRAME = "15m"
FEE = "0"
MODEL = "LightGBMRegressor"


def run_cmd(cmd: list, log_file: Path, cwd=ROOT):
    """Run command, tee to log_file + console, return exit code."""
    log_file.parent.mkdir(parents=True, exist_ok=True)
    print(f"[RUN] {' '.join(map(str, cmd))}")
    with open(log_file, "a") as lf:
        lf.write(f"\n=== {datetime.now().isoformat()} ===\n")
        lf.write("CMD: " + " ".join(map(str, cmd)) + "\n")
        lf.flush()
        proc = subprocess.Popen(
            cmd,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        for line in proc.stdout:
            print(line, end="")
            lf.write(line)
        proc.wait()
        lf.write(f"\nEXIT_CODE={proc.returncode}\n")
    return proc.returncode


def make_override_for_strat(strat: str, version: str = "v1") -> Path:
    """Create a per-strat override json with unique identifier."""
    with open(BASE_OVERRIDE) as f:
        cfg = json.load(f)

    ident = f"{strat.lower()}_fai_{version}"
    cfg["freqai"]["identifier"] = ident

    # Make 15m specific (override some)
    cfg["freqai"]["feature_parameters"]["include_timeframes"] = ["15m"]
    cfg["freqai"]["feature_parameters"]["label_period_candles"] = 12
    cfg["freqai"]["feature_parameters"]["indicator_periods_candles"] = [8, 12, 20, 50]

    out_path = ROOT / f"reports/freqai_experiments/tmp_configs/override_{strat}_{version}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(cfg, f, indent=2)
    return out_path, ident


def backtest_cmd(strat_class: str, timerange: str, override: Path, export_dir: Path) -> list:
    cmd = [
        str(FREQTRADE_BIN),
        "backtesting",
        "--config",
        str(USER_CONFIG),
        "--config",
        str(override),
        "--strategy",
        strat_class,
        "--freqaimodel",
        MODEL,
        "--timeframe",
        TIMEFRAME,
        "--timerange",
        timerange,
        "--fee",
        FEE,
        "-p",
        PAIR,
        "--cache",
        "none",
        "--export",
        "trades",
        "--backtest-directory",
        str(export_dir),
    ]
    return cmd


def analysis_cmd(export_dir: Path) -> list:
    return [
        str(FREQTRADE_BIN),
        "backtesting-analysis",
        "--config",
        str(USER_CONFIG),
        "--backtest-directory",
        str(export_dir),
        "--analysis-groups",
        "0",
        "1",
        "2",
    ]


def lookahead_cmd(strat_class: str, timerange: str, override: Path, export_dir: Path) -> list:
    return [
        str(FREQTRADE_BIN),
        "lookahead-analysis",
        "--config",
        str(USER_CONFIG),
        "--config",
        str(override),
        "--strategy",
        strat_class,
        "--freqaimodel",
        MODEL,
        "--timeframe",
        TIMEFRAME,
        "--timerange",
        timerange,
        "--fee",
        FEE,
        "-p",
        PAIR,
        "--cache",
        "none",
        "--targeted-trade-amount",
        "100",
        "--backtest-directory",
        str(export_dir),
    ]


def parse_backtest_log_for_metrics(log_path: Path) -> dict:
    """Very basic parser for TOTAL line and profit."""
    metrics = {"trades": None, "profit_pct": None, "abs_profit": None, "wr": None, "raw": ""}
    if not log_path.exists():
        return metrics
    content = log_path.read_text(errors="ignore")
    metrics["raw"] = content[-2000:]  # tail
    # Look for TOTAL row like: │    TOTAL │     56 │         0.25 │          14.087 │         1.41 │ ...
    m = re.search(r"TOTAL\s*│\s*(\d+)\s*│\s*([-\d.]+)\s*│\s*([-\d.]+)\s*│\s*([-\d.]+)", content)
    if m:
        metrics["trades"] = int(m.group(1))
        metrics["profit_pct"] = m.group(4)
        metrics["abs_profit"] = m.group(3)
    # Win rate rough
    wr = re.search(r"(\d+\.?\d*)\s*\|\s*$", content.split("Win%")[-1] if "Win%" in content else "")
    if wr:
        metrics["wr"] = wr.group(1) + "%"
    return metrics


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--strats",
        nargs="*",
        default=DEFAULT_STRATS,
        help="Strategies to process (class names without _FreqAI)",
    )
    parser.add_argument(
        "--full", action="store_true", help="Run all defined instead of default starters"
    )
    args = parser.parse_args()

    strats = (
        args.strats
        if not args.full
        else [
            "LIB_STR045",
            "LIB_STR007",
            "LIB_STR013",
            "LIB_STR012",
            "LIB_STR030",
            "LIB_STR005_EMA",
            "LIB_STR005",
            "LIB_STR003",
            "LIB_STR026",
        ]
    )

    EXPERIMENTS_DIR.mkdir(parents=True, exist_ok=True)

    leaderboard_rows = []

    for base_name in strats:
        strat_class = f"{base_name}_FreqAI"
        strat_dir = EXPERIMENTS_DIR / base_name
        strat_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n=== Processing {base_name} ({strat_class}) ===")

        for period_name, timerange in PERIODS:
            override_path, ident = make_override_for_strat(base_name, version=period_name.lower())
            log_path = strat_dir / f"backtest_{period_name}.log"
            export_dir = strat_dir / f"backtest_results_{period_name}"
            export_dir.mkdir(parents=True, exist_ok=True)

            # 1. Backtest
            cmd = backtest_cmd(strat_class, timerange, override_path, export_dir)
            rc = run_cmd(cmd, log_path)
            if rc != 0:
                print(f"[WARN] Backtest failed for {base_name} {period_name} (rc={rc})")
                continue

            # 2. backtesting-analysis (on the export dir)
            analysis_log = strat_dir / f"analysis_{period_name}.log"
            cmd_a = analysis_cmd(export_dir)
            run_cmd(cmd_a, analysis_log)

            # 3. lookahead-analysis
            la_log = strat_dir / f"lookahead_{period_name}.log"
            cmd_la = lookahead_cmd(strat_class, timerange, override_path, export_dir)
            run_cmd(cmd_la, la_log)

            # Collect basic metrics from backtest log
            m = parse_backtest_log_for_metrics(log_path)
            row = {
                "strategy": base_name,
                "period": period_name,
                "timerange": timerange,
                "trades": m.get("trades"),
                "profit_pct": m.get("profit_pct"),
                "abs_profit": m.get("abs_profit"),
                "wr": m.get("wr"),
                "identifier": ident,
            }
            leaderboard_rows.append(row)

            print(f"  {period_name}: trades={row['trades']} profit%={row['profit_pct']}")

    # Build leaderboard
    if leaderboard_rows:
        # CSV
        csv_path = EXPERIMENTS_DIR / "freqai_leaderboard.csv"
        with open(csv_path, "w") as f:
            f.write("strategy,period,timerange,trades,profit_pct,abs_profit,wr,identifier\n")
            for r in leaderboard_rows:
                f.write(
                    f"{r['strategy']},{r['period']},{r['timerange']},{r['trades']},{r['profit_pct']},{r['abs_profit']},{r['wr']},{r['identifier']}\n"
                )

        # MD
        md_path = EXPERIMENTS_DIR / "freqai_leaderboard.md"
        with open(md_path, "w") as f:
            f.write("# FreqAI A Experiments Leaderboard\n\n")
            f.write("| strategy | period | trades | profit% | abs | WR | identifier |\n")
            f.write("|----------|--------|--------|---------|-----|----|------------|\n")
            for r in leaderboard_rows:
                f.write(
                    f"| {r['strategy']} | {r['period']} | {r['trades']} | {r['profit_pct']} | {r['abs_profit']} | {r['wr']} | {r['identifier']} |\n"
                )

        print(f"\nLeaderboards written to {EXPERIMENTS_DIR}")

    # Simple summary stub
    summary_path = EXPERIMENTS_DIR / "freqai_summary.md"
    with open(summary_path, "w") as f:
        f.write("# FreqAI Experiments Summary (A class starters)\n\n")
        f.write(f"Date: {datetime.now().isoformat()}\n\n")
        f.write("Processed: " + ", ".join(strats) + "\n\n")
        f.write(
            "See freqai_leaderboard.* and individual <STRAT>/ logs for full results and analysis.\n"
        )
        f.write("\n## Notes\n")
        f.write(
            "- All runs used config overrides only (no modification to user_data/config.json)\n"
        )
        f.write("- Features % prefixed, no volume, targets only in set_freqai_targets\n")
        f.write("- Lookahead used --targeted-trade-amount 100\n")
        f.write("- Classification will be filled after full review of logs.\n")

    print(f"Summary: {summary_path}")
    print("Done. Check reports/freqai_experiments/")


if __name__ == "__main__":
    main()
