"""
database.py
------------
Task 3: Build a relational database from your cleaned data.

This module covers KM-04 topics: Introduction to Databases (DBMS,
components, characteristics) and Structured Query Language (SQL).

You will use Python's built-in `sqlite3` module — no extra install
needed. SQLite stores the whole database in a single file, which makes
it perfect for a student project (and easy to include as evidence).

By the end of this file you must be able to:
  1. Create a database file (store.db) with two related tables.
  2. Insert your cleaned data into those tables.
  3. Run at least FIVE meaningful SQL queries against the data,
     including at least one JOIN and one aggregation (SUM, COUNT, AVG).
"""

import sqlite3


def get_connection(db_path: str = "store.db") -> sqlite3.Connection:
    """Open or create the SQLite database file."""
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_tables(conn: sqlite3.Connection) -> None:
    """Create the products and sales tables with primary and foreign keys."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id TEXT PRIMARY KEY,
            product_name TEXT NOT NULL,
            category TEXT,
            unit_price REAL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            sale_id TEXT PRIMARY KEY,
            product_id TEXT,
            quantity INTEGER,
            sale_date TEXT,
            payment_method TEXT,
            customer_type TEXT,
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    """)

    conn.commit()


def insert_products(conn: sqlite3.Connection, products_df) -> None:
    """Insert cleaned product records into the products table."""
    sql = """
        INSERT OR IGNORE INTO products
        (product_id, product_name, category, unit_price)
        VALUES (?, ?, ?, ?)
    """

    rows = products_df[
        ["product_id", "product_name", "category", "unit_price"]
    ].itertuples(index=False, name=None)

    conn.executemany(sql, rows)
    conn.commit()


def insert_sales(conn: sqlite3.Connection, sales_df) -> None:
    """Insert cleaned sales records into the sales table."""
    sql = """
        INSERT OR IGNORE INTO sales
        (sale_id, product_id, quantity, sale_date,
         payment_method, customer_type)
        VALUES (?, ?, ?, ?, ?, ?)
    """

    rows = sales_df[
        ["sale_id", "product_id", "quantity", "sale_date",
         "payment_method", "customer_type"]
    ].itertuples(index=False, name=None)

    conn.executemany(sql, rows)
    conn.commit()


# ---------------------------------------------------------------------
# SQL QUERIES
# ---------------------------------------------------------------------

def query_total_revenue_per_product(conn: sqlite3.Connection):
    """
    Business question: How much revenue did each product generate?

    Uses JOIN, SUM, GROUP BY, and ORDER BY.
    """
    sql = """
        SELECT
            p.product_name,
            SUM(s.quantity * p.unit_price) AS total_revenue
        FROM sales AS s
        JOIN products AS p
            ON s.product_id = p.product_id
        GROUP BY p.product_id, p.product_name
        ORDER BY total_revenue DESC
    """
    return conn.execute(sql).fetchall()


def query_best_selling_product(conn: sqlite3.Connection):
    """
    Business question: Which product sold the highest total quantity?
    """
    sql = """
        SELECT
            p.product_name,
            SUM(s.quantity) AS total_quantity_sold
        FROM sales AS s
        JOIN products AS p
            ON s.product_id = p.product_id
        GROUP BY p.product_id, p.product_name
        ORDER BY total_quantity_sold DESC
        LIMIT 1
    """
    return conn.execute(sql).fetchall()


def query_sales_by_payment_method(conn: sqlite3.Connection):
    """
    Business question: How many sales transactions used each payment method?
    """
    sql = """
        SELECT
            payment_method,
            COUNT(*) AS number_of_transactions
        FROM sales
        GROUP BY payment_method
        ORDER BY number_of_transactions DESC
    """
    return conn.execute(sql).fetchall()


def query_custom_one(conn: sqlite3.Connection):
    """
    Business question: Which product category generates the most revenue?
    """
    sql = """
        SELECT
            p.category,
            SUM(s.quantity * p.unit_price) AS total_revenue
        FROM sales AS s
        JOIN products AS p
            ON s.product_id = p.product_id
        GROUP BY p.category
        ORDER BY total_revenue DESC
    """
    return conn.execute(sql).fetchall()


def query_custom_two(conn: sqlite3.Connection):
    """
    Business question: How many transactions were made by each customer type
    during February 2026?
    """
    sql = """
        SELECT
            customer_type,
            COUNT(*) AS number_of_transactions
        FROM sales
        WHERE sale_date >= '2026-02-01'
          AND sale_date < '2026-03-01'
        GROUP BY customer_type
        ORDER BY number_of_transactions DESC
    """
    return conn.execute(sql).fetchall()
