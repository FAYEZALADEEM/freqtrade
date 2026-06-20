#!/usr/bin/env python3
"""
جمع نتائج الباكتيست وترتيبها في leaderboard.
الاستخدام: python3 collect_results.py [--results-dir path] [--output file.csv]
"""

import argparse
import json
import zipfile
from pathlib import Path


def load_result(path: Path) -> dict | None:
    try:
        if path.suffix == ".zip":
            with zipfile.ZipFile(path) as zf:
                names = [n for n in zf.namelist() if n.endswith(".json")]
                if not names:
                    return None
                with zf.open(names[0]) as f:
                    data = json.load(f)
        else:
            with path.open() as f:
                data = json.load(f)

        if "strategy" not in data:
            return None

        strat_name = next(iter(data["strategy"].keys()))
        s = data["strategy"][strat_name]
        s["_strategy_name"] = strat_name
        return s

    except Exception:
        return None


def parse_result(s: dict) -> dict:
    total = s.get("total_trades", 0)
    wins = s.get("wins", 0)
    losses = s.get("losses", 0)
    win_rate = round(wins / total * 100, 1) if total > 0 else 0.0

    profit_abs = round(s.get("profit_total_abs", 0), 2)
    profit_pct = round(s.get("profit_total", 0) * 100, 3)
    max_dd = round(s.get("max_drawdown_account", 0) * 100, 2)
    avg_profit = round(s.get("profit_mean", 0) * 100, 4)
    duration = s.get("holding_avg_s", 0)
    dur_h = f"{int(duration // 3600)}h" if duration else ""

    return {
        "strategy": s.get("_strategy_name", ""),
        "trades": total,
        "wins": wins,
        "losses": losses,
        "win_%": win_rate,
        "profit_abs": profit_abs,
        "profit_%": profit_pct,
        "avg_profit_%": avg_profit,
        "max_dd_%": max_dd,
        "avg_duration": dur_h,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", default="user_data/backtest_results")
    parser.add_argument("--output", default="reports/leaderboard_cloud.csv")
    args = parser.parse_args()

    results_dir = Path(args.results_dir)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    files = sorted(results_dir.glob("*.zip"))
    files = [f for f in files if "meta" not in f.name]
    print(f"فحص {len(files)} ملف في {results_dir} ...")

    rows = []
    for f in files:
        raw = load_result(f)
        if raw:
            rows.append(parse_result(raw))

    if not rows:
        print("لم يتم العثور على نتائج.")
        return

    rows.sort(key=lambda r: (r["profit_abs"], r["win_%"]), reverse=True)

    w = 46
    hdr = (
        f"{'#':<4} {'Strategy':<{w}} {'Trades':>6} {'Win%':>5} "
        f"{'ProfitAbs':>10} {'Profit%':>8} {'DD%':>6}"
    )
    sep = "=" * len(hdr)
    print(f"\n{sep}\n{hdr}\n{sep}")
    for i, r in enumerate(rows, 1):
        flag = " ✓" if r["profit_abs"] > 0 and r["win_%"] >= 50 else ""
        print(
            f"{i:<4} {r['strategy']:<{w}} {r['trades']:>6} {r['win_%']:>5.1f} "
            f"{r['profit_abs']:>10.2f} {r['profit_%']:>8.3f} {r['max_dd_%']:>6.2f}{flag}"
        )
    print(sep)

    profitable = sum(1 for r in rows if r["profit_abs"] > 0)
    msg = f"\nالإجمالي: {len(rows)} استراتيجية | مربحة: {profitable} | خاسرة: {len(rows) - profitable}"  # noqa: E501,RUF001
    print(msg)

    import csv

    with output_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"تم الحفظ في: {output_path}")


if __name__ == "__main__":
    main()
