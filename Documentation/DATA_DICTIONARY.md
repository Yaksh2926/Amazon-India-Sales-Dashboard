# Data Dictionary and Model Assumptions

The committed DAX measures assume a model table named `Amazon Sales` and explicitly reference the following columns:

| Field | Used for |
|---|---|
| `Total_Sales_INR` | Total sales |
| `Profit_INR` | Total profit |
| `Order_ID` | Distinct order count |
| `Quantity` | Units sold |
| `Order_Status` | Delivered, shipped, returned, and cancelled counts |
| `Order_Date` | Calendar table and date relationship |

The dashboard business brief also refers to product category, state, payment method, and fulfilment dimensions. Their precise column names are not asserted here because they are not defined in the DAX measures file.

## Validate before analysis
1. Read the CSV header and confirm exact column names.
2. Check data types, null counts, duplicate rows, and the row grain.
3. Confirm whether one row represents an order, order line, or product line.
4. Confirm the business meaning of sales, profit, returns, and cancellations.
5. Do not calculate order-status rates from row counts until the row grain is confirmed.
