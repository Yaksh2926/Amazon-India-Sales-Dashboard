# Power BI Model Setup

1. Import `Data/Amazon_Sales_Cleaned.csv` into Power BI.
2. Rename the imported table to `Amazon Sales` (or update the DAX table references consistently).
3. Confirm the data types:
   - `Order_Date`: Date
   - `Total_Sales_INR`, `Profit_INR`: Decimal number / fixed decimal as appropriate
   - `Quantity`: Whole number
   - `Order_ID`, `Order_Status`: Text
4. Create the measures in `Amazon_Dashboard_DAX_Measures.txt`.
5. Create the Calendar table and relate `Calendar[Date]` (one side) to `Amazon Sales[Order_Date]` (many side).
6. Sort `Calendar[Year-Month]` by `Calendar[Year-Month Sort]`.

Before using status metrics, verify the dataset grain. If there are multiple rows per order, distinct order-level status counts must use `DISTINCTCOUNT(Order_ID)` under the appropriate filter context. Validate category, state, payment, and fulfilment field names against the CSV before creating visuals.

No `.pbix` file is included in this repository.
