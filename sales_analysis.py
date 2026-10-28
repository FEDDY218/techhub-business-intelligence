
import csv
from pathlib import Path 


def read_sales(path):

    # we read sales records from csv file 
    with open(path, mode="r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        # Reading each CSV row as a dictionary.
        rows = list(reader)

        # Getting the column names from the CSV header.
        columns = reader.fieldnames

    print(f"Number of rows: {len(rows)}")
    print(f"Column names: {columns}")

    return rows


# Building the path to our CSV file.
data_path = Path("data") / "electronics_sales.csv"

# Loading the sales records.
sales = read_sales(data_path)



