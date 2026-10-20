"""
visualize.py
-------------
Task 5: Turn your analysis into charts.

This module covers KM-04 KT07: Visualising Data with AI-assisted tools.
We use matplotlib here, one of the most common Python charting
libraries (conceptually similar to the ggplot2 example from the
KM-04 slides).

You must produce AT LEAST TWO charts:
  1. A bar chart of total revenue per product (or per category)
  2. A line chart of the monthly sales trend

Save both charts as .png files — you will include them as evidence
in your submission.
"""


"""
visualize.py
-------------
Task 5: Create charts to show sales insights.
"""

import matplotlib.pyplot as plt


def bar_chart_revenue_per_product(product_names, revenues):
    """Create a bar chart showing revenue for each product."""

    plt.figure(figsize=(12, 7))

    plt.bar(product_names, revenues)

    plt.title("Revenue per Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue (R)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig("revenue_per_product.png")
    plt.close()


def line_chart_monthly_trend(monthly_trend):
    """Create a line chart showing monthly sales quantities."""

    months = list(monthly_trend.keys())
    quantities = list(monthly_trend.values())

    plt.figure(figsize=(9, 5))

    plt.plot(months, quantities, marker="o")

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Quantity Sold")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("monthly_trend.png")
    plt.close()
