#!/usr/bin/env python3
"""Analyze Amazon India transaction data from the original Excel workbook or a CSV."""
from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd

REQUIRED = ["Order_ID","Order_Date","Category","Product","Quantity","Unit_Price_INR",
            "Discount_Pct","Total_Sales_INR","Profit_INR","Payment_Method",
            "Fulfillment","Order_Status","Ship_State"]

def load_data(path: Path) -> pd.DataFrame:
    if path.suffix.lower() in {".xlsx", ".xls"}:
        df = pd.read_excel(path, sheet_name="Sheet1")
    else:
        df = pd.read_csv(path, low_memory=False)
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    return df

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input",type=Path,required=True)
    ap.add_argument("--output",type=Path,default=Path("Analysis/outputs"))
    args=ap.parse_args()
    df=load_data(args.input)
    args.output.mkdir(parents=True,exist_ok=True)
    df["Order_Date"]=pd.to_datetime(df["Order_Date"],errors="coerce")
    for c in ["Order_ID","Category","Product","Payment_Method","Fulfillment","Order_Status","Ship_State"]:
        df[c]=df[c].astype("string").str.strip()
    profile=pd.DataFrame({"column":df.columns,"dtype":[str(df[c].dtype) for c in df],
        "missing":[int(df[c].isna().sum()) for c in df],
        "distinct":[int(df[c].nunique(dropna=True)) for c in df]})
    profile.to_csv(args.output/"column_profile.csv",index=False)
    df.to_csv(args.output/"Amazon_Sales_Cleaned.csv",index=False,date_format="%Y-%m-%d")
    kpis={
        "records":len(df),"unique_orders":df.Order_ID.nunique(),
        "total_sales_inr":df.Total_Sales_INR.sum(),"total_profit_inr":df.Profit_INR.sum(),
        "units_sold":df.Quantity.sum(),
        "average_order_value_inr":df.Total_Sales_INR.sum()/df.Order_ID.nunique(),
        "profit_margin_pct":df.Profit_INR.sum()/df.Total_Sales_INR.sum()*100,
        "average_discount_pct":df.Discount_Pct.mean()*100,
        "exact_duplicate_rows":int(df.duplicated().sum())}
    pd.Series(kpis,name="value").to_csv(args.output/"kpi_summary.csv",header=True)
    for name,group in {
        "sales_by_category":df.groupby("Category").agg(orders=("Order_ID","nunique"),sales_inr=("Total_Sales_INR","sum"),profit_inr=("Profit_INR","sum"),units=("Quantity","sum")),
        "sales_by_state":df.groupby("Ship_State").agg(orders=("Order_ID","nunique"),sales_inr=("Total_Sales_INR","sum"),profit_inr=("Profit_INR","sum")),
        "sales_by_fulfilment":df.groupby("Fulfillment").agg(orders=("Order_ID","nunique"),sales_inr=("Total_Sales_INR","sum"),profit_inr=("Profit_INR","sum")),
        "sales_by_payment":df.groupby("Payment_Method").agg(orders=("Order_ID","nunique"),sales_inr=("Total_Sales_INR","sum")),
        "order_status":df.groupby("Order_Status").agg(orders=("Order_ID","nunique"),sales_inr=("Total_Sales_INR","sum")),
        "top_products":df.groupby("Product").agg(orders=("Order_ID","nunique"),units=("Quantity","sum"),sales_inr=("Total_Sales_INR","sum"),profit_inr=("Profit_INR","sum")).sort_values("sales_inr",ascending=False)
    }.items():
        group.to_csv(args.output/f"{name}.csv")
    monthly=df.set_index("Order_Date").resample("MS").agg(orders=("Order_ID","nunique"),sales_inr=("Total_Sales_INR","sum"),profit_inr=("Profit_INR","sum"))
    monthly.to_csv(args.output/"monthly_trend.csv")
    print(pd.Series(kpis).to_string())
    print(f"\nOutputs saved to {args.output.resolve()}")

if __name__=="__main__":
    main()
