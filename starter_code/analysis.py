"""
analysis.py
------------
Task 4: Programming logic — functions, loops, conditionals and arrays.

This module covers KM-05 topics: Programming Basics (data types,
conditionals, loops, arrays/lists, functions) and Introduction to
Algorithms.

IMPORTANT: For this file, use plain Python (for-loops, if/else,
lists and dictionaries) even where pandas could do it in one line.
The point of this section is to demonstrate the programming
fundamentals from KM-05, not just pandas shortcuts.
"""

def total_sales_records(sales_rows: list) -> int:
    """Count sales records using a loop."""
    count = 0

    for row in sales_rows:
        count += 1

    return count


def low_stock_alert(products_rows: list, threshold: int = 5) -> list:
    """
    Return product names that need re-ordering.

    If a product has an in_stock field set to False, flag it.
    If it has a stock_count field, flag it when stock is at or
    below the threshold. The current dataset may not have these
    fields, so products without them are not automatically flagged.
    """
    alerts = []

    for product in products_rows:
        if product.get("in_stock") is False:
            alerts.append(product["product_name"])
        elif product.get("in_stock") == "False":
            alerts.append(product["product_name"])
        elif "stock_count" in product:
            if product["stock_count"] <= threshold:
                alerts.append(product["product_name"])

    return alerts


def monthly_sales_trend(sales_rows: list) -> dict:
    """Calculate the total quantity sold in each month."""
    trend = {}

    for row in sales_rows:
        sale_date = row.get("sale_date")
        quantity = row.get("quantity")

        if sale_date and quantity is not None:
            month = str(sale_date)[:7]

            if month in trend:
                trend[month] += int(quantity)
            else:
                trend[month] = int(quantity)

    return dict(sorted(trend.items()))


def classify_transaction_size(quantity: int) -> str:
    """Classify a transaction based on its quantity."""
    if quantity >= 5:
        return "Bulk"
    elif quantity >= 2:
        return "Multiple"
    elif quantity == 1:
        return "Single"
    else:
        return "Invalid"


def average_basket_size(sales_rows: list) -> float:
    """Calculate the average quantity per sales record."""
    total = 0
    count = 0

    for row in sales_rows:
        quantity = row.get("quantity")

        if quantity is not None:
            total += int(quantity)
            count += 1

    if count == 0:
        return 0.0

    return round(total / count, 2)
