# Data Dictionary

Source: `Amazon Sales Data India.xlsx`, sheet `Sheet1`.

| Column | Meaning / use | Type |
|---|---|---|
| Order_ID | Unique order identifier | Text |
| Order_Date | Order date | Date |
| Category | Product category | Text |
| Product | Product name | Text |
| Quantity | Units in order record | Integer |
| Unit_Price_INR | Unit price in INR | Decimal |
| Discount_Pct | Discount fraction (e.g. 0.25 = 25%) | Decimal |
| Total_Sales_INR | Recorded sales amount in INR | Decimal |
| Profit_INR | Recorded profit amount in INR | Decimal |
| Payment_Method | Payment method | Text |
| Fulfillment | Fulfilment channel | Text |
| Order_Status | Delivered / Shipped / Returned / Cancelled | Text |
| Ship_State | Destination state | Text |

The source transaction table has 10,000 rows and 10,000 distinct Order_ID values. No missing values or exact duplicate rows were detected in the inspected data. Date coverage: 2024-01-01 to 2026-08-30.
