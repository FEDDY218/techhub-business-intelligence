# Tech Hub Kenya — Sales Analytics

## Project Overview
This project analyses September sales data for Tech Hub Kenya, an electronics retailer operating across multiple stores in Kenya.

## Objectives
- Calculate total sales revenue.
- Identify top-performing stores and products.
- Identify high-value sales.
- Summarise high-value sales by store.
- Verify results using pandas.

## Tools
- Python 3.12
- Python standard library (`csv`, `pathlib`)
- pandas for verification
- Jupyter Notebook / VS Code

## Project Structure
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

## How to Run
1. Clone or download the repository.
2. Install the dependencies listed in `requirements.txt`.
3. Open `sales_analysis.ipynb` in VS Code or Jupyter Notebook.
4. Run the notebook cells from top to bottom.

## Data Cleaning
- Convert quantities and unit prices into numeric values.
- Exclude missing, invalid, or negative quantities and prices.
- Calculate revenue as quantity multiplied by unit price.

## Outputs
The sales report is saved to `output/sales_report.txt`.

## Verification
Pandas is used to independently verify headline results from the standard Python analysis.

## Author
Feddy Mwanjumwa Matata
