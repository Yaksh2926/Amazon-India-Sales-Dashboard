# Amazon India Sales & Business Performance Analysis

An end-to-end portfolio repository for analyzing Amazon India sales and business performance. It includes the existing interactive dashboard, cleaned sales dataset, DAX measures, a Python analysis workflow, and project documentation.

## Live dashboard

**[Open the interactive Amazon India dashboard](https://yaksh2926.github.io/Amazon-India-Sales-Dashboard/)**

The root `index.html` forwards to the standalone dashboard page. The dashboard is also preserved at `Dashboard/Amazon_India_Business_Dashboard.html`.

## Project structure

```text
Amazon-India-Sales-Dashboard/
├── Dashboard/
│   └── Amazon_India_Business_Dashboard.html
├── Data/
│   └── Amazon_Sales_Cleaned.csv
├── PowerBI/
│   ├── Amazon_Dashboard_DAX_Measures.txt
│   └── POWERBI_MODEL_GUIDE.md
├── Analysis/
│   ├── analyze_sales.py
│   ├── requirements.txt
│   └── outputs/                 # generated when the script runs
├── Documentation/
│   ├── PROJECT_OVERVIEW.md
│   └── DATA_DICTIONARY.md
├── .github/workflows/pages.yml
├── Amazon_India_Business_Dashboard.html   # original path retained
├── Amazon_Sales_Cleaned.csv               # original path retained
├── Amazon_Dashboard_DAX_Measures.txt      # original path retained
├── index.html
└── README.md
```

The original root-level files are retained for compatibility; organized copies are provided in the folders above.

## Business questions

The dashboard and DAX model are designed to explore:
- Total sales, profit, order count, quantity, average order value, and profit margin.
- Product/category performance.
- Order status distribution: delivered, shipped, returned, and cancelled.
- Fulfilment and payment-method performance.
- State-wise performance.
- Return and cancellation rates.

## Dataset

The repository contains the cleaned CSV that was already part of the project: `Data/Amazon_Sales_Cleaned.csv`. It is duplicated from the original root-level file so existing links continue to work.

The existing DAX file assumes a table named **Amazon Sales** and uses fields including `Total_Sales_INR`, `Profit_INR`, `Order_ID`, `Quantity`, `Order_Status`, and `Order_Date`. Check the actual CSV header before relying on optional fields or extending the model.

**Scope note:** The repository snapshot did not contain the original raw workbook or the earlier cleaning notebook. This project therefore documents and analyzes the committed cleaned CSV; it does not claim to reproduce the original raw-to-clean transformation.

## Run the Python analysis

Python 3.10+ is recommended.

```bash
python -m pip install -r Analysis/requirements.txt
python Analysis/analyze_sales.py --input Data/Amazon_Sales_Cleaned.csv --output Analysis/outputs
```

The script creates a data profile, numeric summary, and supported business summaries. It checks for expected columns and skips unavailable breakdowns rather than guessing. Outputs are generated locally and are not committed automatically.

## Power BI / DAX

See:
- [DAX measures](PowerBI/Amazon_Dashboard_DAX_Measures.txt)
- [Model setup guide](PowerBI/POWERBI_MODEL_GUIDE.md)

The measures cover sales, profit, orders, units, average order value, profit margin, order statuses, return/cancellation rates, and a calendar table.

## Tools

- Microsoft Excel
- Python and Pandas
- Power BI / DAX
- HTML, CSS, and JavaScript
- GitHub Pages

## Interpretation notes

- Monetary values are treated according to the source field names (INR); verify the source definitions before external reporting.
- Order-status rates depend on the dataset's row grain and status definitions.
- Descriptive comparisons do not establish causal explanations.
- No Power BI `.pbix` file or raw source workbook is included in this repository snapshot.

## Author

**Yaksh Jindal** · [GitHub](https://github.com/Yaksh2926)
