# Tech Hub Kenya — Sales Analytics

## 1. Project Overview

This project analyses September sales data for Tech Hub Kenya, an electronics retailer operating across stores in Kenya.

The purpose is to calculate sales revenue, identify the top-performing stores and products, identify high-value sales, and verify the results using pandas.

## 2. Project Objectives

- Calculate total revenue.
- Calculate revenue by store and product.
- Identify the top three stores and top five products by revenue.
- Identify high-value sales using a threshold of KES 50,000.
- Count high-value sales by store.
- Calculate the mean, median, minimum, and maximum of relevant numeric values.
- Verify the standard Python results independently with pandas.
- Save the results to a text report.

## 3. Tools and Approach

The main analysis uses Python's standard library, particularly `csv` for reading CSV data and dictionaries, lists, loops, and functions for processing sales.

The analysis follows these steps:

1. Load the CSV file using `csv.DictReader`.
2. Convert quantity and unit price values into numbers.
3. Reject rows with invalid or negative numeric values according to the cleaning rules below.
4. Calculate each sale's revenue as quantity multiplied by unit price.
5. Aggregate revenue by store and product.
6. Rank stores and products by revenue.
7. identify high-value sales and count them by store.
8. Calculate summary statistics.
9. Verify the results using pandas.
10. Save the report to `output/sales_report.txt`.

## 4. Numeric Data Cleaning Rules

The `parse_number()` function applies the following rules:

- **Missing values:** `None` and empty or whitespace-only strings are rejected.
- **Commas:** Commas are removed before conversion. For example, `"45,000"` becomes `45000`.
- **Currency text:** The text `"KES"` is removed before conversion. For example, `"KES 45,000"` becomes `45000`.
- **Valid numeric values:** Values that can be converted to numbers are accepted.
- **Invalid text:** Values that cannot be converted into numbers are rejected.
- **Negative values:** Rows with a negative quantity or unit price are rejected.
- **Zero values:** Zero quantity and zero unit price are allowed because the code rejects negative values, not zero values.
- **Skipped rows:** Invalid rows are excluded from the analysis and recorded with a sale ID and a reason for rejection.

The `convert_rows()` function applies these rules to the quantity and unit price columns. Revenue is calculated only for accepted rows.

## 5. Assumptions

- Each CSV row represents one sale record.
- Revenue is calculated as quantity multiplied by unit price.
- Unit prices are assumed to be in Kenyan shillings (KES).
- A high-value sale is defined as a sale with revenue greater than or equal to KES 50,000.
- Top stores and products are ranked by total revenue, not by number of transactions.
- Zero quantities and zero prices are allowed by the current validation rules.
- The analysis assumes the source CSV contains the expected columns: `sale_id`, `sale_date`, `store`, `product`, `quantity`, `unit_price_kes`, and `payment_method`.
- No additional assumptions are made about discounts, tax, refunds, or profit because those fields are not included in the calculation.

## 6. How to Run the Project

### Requirements

- Python 3.12 or a compatible Python version.
- pandas for independent verification.
- The supplied `data/electronics_sales.csv` file.

### Setup on Windows using PowerShell

Open a terminal and navigate to the project folder:

```powershell
cd "$HOME\Desktop\day2-sales-analytics"
```

Install the required package:

```powershell
python -m pip install -r requirements.txt
```

### Run the Jupyter Notebook

Open the project in VS Code:

```powershell
code .
```

Open `sales_analysis.ipynb`, select the appropriate Python environment, and run the cells from top to bottom.

If the notebook has a different filename, open that filename instead.

### Run a Python script (if provided)

If the final project includes `sales_analysis.py`, run:

```powershell
python sales_analysis.py
```

The script and notebook should use the project's data file and write the report to the output folder.

## 7. Verification

Pandas is used to independently recalculate total revenue, revenue by store, revenue by product, and high-value sales.

The verification process should use the same numeric cleaning rules as the standard Python analysis. Results are compared to identify any discrepancies.

A `MATCH` result indicates that the compared values agree within the specified tolerance. A `MISMATCH` result requires further investigation.

## 8. Outputs

- `output/sales_report.txt` — summary of the sales analysis.
- `sales_analysis.ipynb` — the notebook containing the analysis and verification.

## 9. Project Structure

```text
day2-sales-analytics/
├── data/
│   └── electronics_sales.csv
├── output/
│   └── sales_report.txt
├── sales_analysis.ipynb
├── requirements.txt
└── README.md
```

## 10. Author

Feddy Mwanjumwa Matata 
Gitbub profile: FEDDY218

