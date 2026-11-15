# Amazon India Sales & Business Performance Analysis

An end-to-end data analytics project built from the original Amazon India Excel workbook. It includes the transaction dataset, cleaned CSV, exploratory analysis notebook, reproducible Python profiling script, interactive dashboard, DAX measures, and a PDF report.

## Live dashboard

**[Open the interactive Amazon India dashboard](https://yaksh2926.github.io/Amazon-India-Sales-Dashboard/)**

## Project structure

```text
Amazon-India-Sales-Dashboard/
├── Dashboard/
│   └── Amazon_India_Business_Dashboard.html
├── Data/
│   ├── Amazon Sales Data India.xlsx
│   └── Amazon_Sales_Cleaned.csv
├── Analysis/
│   ├── Amazon_India_Sales_Analysis.ipynb
│   ├── analyze_sales.py
│   └── requirements.txt
├── PowerBI/
│   ├── Amazon_Dashboard_DAX_Measures.txt
│   └── POWERBI_MODEL_GUIDE.md
├── Documentation/
│   ├── PROJECT_OVERVIEW.md
│   └── DATA_DICTIONARY.md
├── Reports/
│   └── Amazon_India_Sales_Analysis_Report.pdf
└── README.md
```

The original root-level dashboard, CSV, DAX, and index files are retained for compatibility with existing links. The new organized folders contain the supporting project assets.

## Dataset overview

The supplied workbook contains four sheets:
- `Sheet1`: 10,000 transaction records and 13 columns; used as the main analysis table.
- `Category-wise sales`: category summary.
- `Top10 Products`: product sales summary.
- `Sheet3`: order status counts.

The transaction table covers **1 January 2024 to 30 August 2026**. It contains 10,000 unique Order_ID values, no exact duplicate rows, and no missing values in the inspected 13 columns.

## Key findings from the original workbook

| KPI | Result |
|---|---:|
| Total orders / records | 10,000 |
| Total sales | ₹155,789,893.89 |
| Total profit | ₹33,167,008.49 |
| Units sold | 24,926 |
| Average order value | ₹15,578.99 |
| Aggregate profit margin | 21.29% |
| Average discount | 8.56% |

- **Electronics & Mobiles** is the largest category, with approximately ₹123.57 million in sales (about 79.3% of total sales).
- **Amazon (FBA)** is the largest fulfilment channel by sales.
- **UPI** is the most frequently used payment method.
- **Maharashtra** leads the state sales ranking.
- Delivered orders account for 81.47% of the transaction records.

These are descriptive findings from the supplied file, not causal conclusions or forecasts.

## Reproduce the analysis

Use Python 3.10 or newer:

```bash
python -m pip install -r Analysis/requirements.txt
python Analysis/analyze_sales.py --input "Data/Amazon Sales Data India.xlsx" --output Analysis/outputs
```

Open `Analysis/Amazon_India_Sales_Analysis.ipynb` to see the full notebook workflow. The notebook reads the `Sheet1` transaction table, profiles data quality, prepares fields, calculates KPIs, and explores category, status, fulfilment, payment, state, product, and monthly performance.

## Power BI / DAX

See `PowerBI/Amazon_Dashboard_DAX_Measures.txt` and `PowerBI/POWERBI_MODEL_GUIDE.md` for measures and model setup notes.

## Tools

- Microsoft Excel
- Python, Pandas, NumPy, Matplotlib
- Jupyter Notebook
- Power BI / DAX
- HTML, CSS, JavaScript
- GitHub Pages

## Data preparation and limitations

The cleaned CSV is produced from the original workbook by parsing `Order_Date`, trimming text fields, and coercing numeric columns to numeric types. No rows were removed or imputed because the inspected transaction sheet contained no missing values or exact duplicate rows.

The dataset does not contain a customer identifier. Profit margin is calculated as total profit divided by total sales. Order status metrics use the transaction-level table; because Order_ID is unique in the supplied sheet, row counts and distinct order counts match in this file. Results describe the provided dataset and should be checked against business definitions before operational decisions.

## Author

**Yaksh Jindal** · [GitHub](https://github.com/Yaksh2926)
