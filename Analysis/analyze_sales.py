#!/usr/bin/env python3
"""Profile the committed Amazon cleaned-sales CSV and summarize known metrics."""
from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd

EXPECTED = ["Total_Sales_INR", "Profit_INR", "Order_ID", "Quantity", "Order_Status", "Order_Date"]

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Path to cleaned CSV")
    parser.add_argument("--output", type=Path, default=Path("Analysis/outputs"))
    args = parser.parse_args()

    if not args.input.exists():
        parser.error(f"Input file not found: {args.input}")

    df = pd.read_csv(args.input, low_memory=False)
    args.output.mkdir(parents=True, exist_ok=True)

    profile = pd.DataFrame({
        "column": df.columns,
        "dtype": [str(df[c].dtype) for c in df.columns],
        "missing": [int(df[c].isna().sum()) for c in df.columns],
        "missing_pct": [round(float(df[c].isna().mean() * 100), 2) for c in df.columns],
        "distinct": [int(df[c].nunique(dropna=True)) for c in df.columns],
    })
    profile.to_csv(args.output / "column_profile.csv", index=False)

    numeric = df.select_dtypes(include="number")
    numeric.describe().T.to_csv(args.output / "numeric_summary.csv")

    present = [c for c in EXPECTED if c in df.columns]
    missing = [c for c in EXPECTED if c not in df.columns]
    kpis = []
    if "Total_Sales_INR" in df:
        kpis.append(("Total Sales (INR)", pd.to_numeric(df["Total_Sales_INR"], errors="coerce").sum()))
    if "Profit_INR" in df:
        kpis.append(("Total Profit (INR)", pd.to_numeric(df["Profit_INR"], errors="coerce").sum()))
    if "Order_ID" in df:
        kpis.append(("Distinct Orders", df["Order_ID"].nunique(dropna=True)))
    if "Quantity" in df:
        kpis.append(("Units Sold", pd.to_numeric(df["Quantity"], errors="coerce").sum()))
    if "Total_Sales_INR" in df and "Profit_INR" in df:
        sales = pd.to_numeric(df["Total_Sales_INR"], errors="coerce").sum()
        profit = pd.to_numeric(df["Profit_INR"], errors="coerce").sum()
        kpis.append(("Profit Margin (%)", (profit / sales * 100) if sales else float("nan")))

    pd.DataFrame(kpis, columns=["metric", "value"]).to_csv(args.output / "kpi_summary.csv", index=False)

    if "Order_Status" in df:
        status = df["Order_Status"].fillna("(missing)").value_counts(dropna=False).rename_axis("order_status").reset_index(name="row_count")
        status.to_csv(args.output / "order_status_rows.csv", index=False)

    report = [
        f"Rows: {len(df):,}",
        f"Columns: {len(df.columns):,}",
        f"Exact duplicate rows: {int(df.duplicated().sum()):,}",
        f"Expected fields found: {', '.join(present) if present else 'None'}",
        f"Expected fields not found: {', '.join(missing) if missing else 'None'}",
        "",
        "Note: Order status row counts are row counts, not necessarily distinct order counts.",
        "Confirm dataset grain and definitions before interpreting status rates."
    ]
    (args.output / "run_summary.txt").write_text("\n".join(report), encoding="utf-8")
    print("\n".join(report))
    print(f"\nOutputs written to: {args.output.resolve()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
