"""
data_cleaning.py
-----------------
Task 2: Load the raw CSV files and clean them.

This module covers KM-04 topics: Introduction to Data (data types,
errors of omission) and Data in Spreadsheets.

The raw files in data/products.csv and data/sales.csv contain REAL
data-quality problems on purpose, so you get practice fixing them:

  products.csv issues to find and fix:
    - Some products are missing a unit_price
    - One product is missing its product_name
    - Category text is inconsistently capitalised (e.g. "beverages" vs "Beverages")
    - One exact duplicate row

  sales.csv issues to find and fix:
    - sale_date is written in at least FOUR different formats
    - Some rows have a missing sale_date (an error of omission)
    - Some rows have a missing quantity
    - Some rows have a missing payment_method
    - A few rows reference a product_id that does not exist in products.csv
    - One exact duplicate row

You must handle every one of these before the data moves on to the
database in database.py. Document the decisions you make (e.g. "rows
with a missing sale_date were dropped because we cannot analyse sales
trends without a date") in your README findings section.
"""


"""
Task 2: Load and clean the raw CSV files.

This module cleans missing values, inconsistent categories and dates,
duplicate rows, and invalid product references.
"""


"""
data_cleaning.py
-----------------
Task 2: Load and clean the raw CSV files.

This module handles missing values, inconsistent categories and dates,
duplicate rows, invalid quantities, and invalid product references.
"""

import pandas as pd


def load_raw_data(products_path: str, sales_path: str):
    """
    Load products.csv and sales.csv.

    Returns:
        A tuple containing the raw products and sales DataFrames.
    """
    products_df = pd.read_csv(products_path)
    sales_df = pd.read_csv(sales_path)

    return products_df, sales_df


def clean_products(products_df: "pd.DataFrame") -> "pd.DataFrame":
    """
    Clean the products DataFrame without changing the original.

    Removes products with missing IDs, names, or prices.
    Standardises category capitalisation and removes exact duplicates.
    """
    products = products_df.copy()

    # Remove unnecessary spaces from text columns.
    for column in ["product_id", "product_name", "category"]:
        if column in products.columns:
            products[column] = products[column].map(
                lambda value: value.strip()
                if isinstance(value, str)
                else value
            )

    # Convert prices to numbers. Invalid prices become missing values.
    products["unit_price"] = pd.to_numeric(
        products["unit_price"], errors="coerce"
    )

    # Remove products without a usable ID, name, or price.
    products = products.dropna(
        subset=["product_id", "product_name", "unit_price"]
    )

    # Remove blank product IDs and names.
    products = products[
        products["product_id"].astype(str).str.strip().ne("")
        & products["product_name"].astype(str).str.strip().ne("")
    ]

    # Standardise category names, e.g. "beverages" becomes "Beverages".
    products["category"] = (
        products["category"].astype("string").str.strip().str.title()
    )

    # Remove exact duplicate rows.
    products = products.drop_duplicates()

    return products.reset_index(drop=True)


def clean_sales(
    sales_df: "pd.DataFrame", valid_product_ids
) -> "pd.DataFrame":
    """
    Clean sales dates, quantities, payment methods, customer types,
    and product references.
    """
    sales = sales_df.copy()

    # Standardise product IDs for comparison with the products table.
    sales["product_id"] = sales["product_id"].map(
        lambda value: str(value).strip()
        if pd.notna(value)
        else pd.NA
    )

    valid_ids = {
        str(value).strip()
        for value in valid_product_ids
        if pd.notna(value)
    }

    # Support several common date formats.
    date_formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%d %b %Y",
        "%d %B %Y",
    ]

    def parse_date(value):
        if pd.isna(value) or str(value).strip() == "":
            return pd.NaT

        date_text = str(value).strip()

        for date_format in date_formats:
            try:
                return pd.to_datetime(
                    date_text,
                    format=date_format,
                    errors="raise"
                )
            except (ValueError, TypeError):
                continue

        # Try to parse other recognisable date formats.
        return pd.to_datetime(
            date_text,
            errors="coerce",
            dayfirst=True
        )

    # Convert dates to pandas datetime values.
    sales["sale_date"] = sales["sale_date"].apply(parse_date)

    # Drop rows with missing or invalid dates.
    sales = sales.dropna(subset=["sale_date"])

    # Standardise dates to YYYY-MM-DD.
    sales["sale_date"] = sales["sale_date"].dt.strftime("%Y-%m-%d")

    # Convert quantities to numbers.
    sales["quantity"] = pd.to_numeric(
        sales["quantity"], errors="coerce"
    )

    # Drop rows with missing quantities.
    sales = sales.dropna(subset=["quantity"])

    # Keep only positive whole-number quantities.
    sales = sales[
        (sales["quantity"] > 0)
        & (sales["quantity"] % 1 == 0)
    ]

    sales["quantity"] = sales["quantity"].astype(int)

    # Remove missing product IDs.
    sales = sales.dropna(subset=["product_id"])

    # Remove sales that refer to products that do not exist.
    sales = sales[sales["product_id"].isin(valid_ids)]

    # Fill missing payment methods with "Unknown".
    sales["payment_method"] = (
        sales["payment_method"]
        .astype("string")
        .str.strip()
        .replace("", pd.NA)
        .fillna("Unknown")
    )

    # Fill missing customer types with "Unknown".
    # This preserves valid sales without guessing the customer type.
    sales["customer_type"] = (
        sales["customer_type"]
        .astype("string")
        .str.strip()
        .replace("", pd.NA)
        .fillna("Unknown")
    )

    # Remove exact duplicate rows.
    sales = sales.drop_duplicates()

    return sales.reset_index(drop=True)


def cleaning_summary(
    raw_df: "pd.DataFrame",
    clean_df: "pd.DataFrame",
    name: str
) -> str:
    """
    Summarise the number of rows before and after cleaning.
    """
    raw_count = len(raw_df)
    clean_count = len(clean_df)
    removed_count = raw_count - clean_count

    return (
        f"{name}: {raw_count} raw rows -> "
        f"{clean_count} clean rows ({removed_count} removed)"
    )
