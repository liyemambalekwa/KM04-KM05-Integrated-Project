
# Thabo's Corner Store — Sales Insights System

**Occupational Certificate: Artificial Intelligence Software Developer — NQF Level 4**

Integrated project covering KM-04 (Data, Databases and Data Visualisation) and KM-05 (Programming and Python).

## 1. Project Overview

This project cleans and analyses sales data for Thabo's Corner Store. It uses Python to clean data, SQLite to store and query records, programming logic to calculate sales insights, Matplotlib to create charts, and password hashing to demonstrate basic access control.

The aim is to help the store understand product revenue, sales trends, and possible areas for improvement.

## 2. Folder Structure

```text
thabos-corner-store/
├── data/
│   ├── products.csv
│   └── sales.csv
├── starter_code/
│   ├── README.md
│   ├── requirements.txt
│   ├── main.py
│   ├── data_cleaning.py
│   ├── database.py
│   ├── analysis.py
│   ├── visualize.py
│   ├── security.py
│   ├── store.db
│   ├── revenue_per_product.png
│   └── monthly_trend.png
├── PLAN.md
└── .gitignore
```

## 3. Requirements and Setup

Requirements:
- Python 3.10 or later
- Visual Studio Code
- Git
- pandas
- matplotlib

Open a terminal in the project root and install the required packages:

```bash
python -m pip install -r starter_code/requirements.txt
```

Run the program from the `starter_code` folder:

```bash
cd starter_code
python main.py
```

The program asks for a password before displaying the reports. For this learning project, the sample password is `Thabo2026!`.

The program creates or updates `store.db` and generates two PNG chart files.

## 4. Task 2: Data Cleaning

The raw CSV files contain deliberate data-quality problems. The cleaning functions are implemented in `data_cleaning.py`.

### Product Data Cleaning

The original products file contained 16 rows. After cleaning, 12 rows remained.

The cleaning process:
- Removes records with missing product IDs, names, or prices.
- Converts product prices to numeric values.
- Removes blank product IDs and product names.
- Removes unnecessary spaces from text fields.
- Standardises category capitalisation.
- Removes exact duplicate rows.

Four product rows were removed. These included products with missing prices, a product with a missing name, and an exact duplicate.

Missing prices were not guessed because incorrect prices could lead to inaccurate revenue calculations. The product with the missing name was removed because it could not be reliably identified.

### Sales Data Cleaning

The original sales file contained 71 records. After cleaning, 43 records remained.

The cleaning process:
- Converts supported date formats to `YYYY-MM-DD`.
- Removes sales with missing or invalid dates.
- Converts quantities to numeric values.
- Removes missing, invalid, zero, negative, and non-whole-number quantities.
- Removes missing product IDs and references to products that do not exist in the cleaned product data.
- Replaces missing payment methods and customer types with `Unknown`.
- Removes exact duplicate rows.

Missing payment methods and customer types were labelled `Unknown` instead of being guessed. This preserves otherwise usable records while showing that the information was unavailable.

### Data Cleaning Verification

The program reported:
- 16 raw product rows reduced to 12 cleaned rows.
- 71 raw sales records reduced to 43 cleaned records.
- No missing values in the cleaned data.
- No exact duplicate rows in the cleaned data.
- No invalid product references in the cleaned sales data.

## 5. Task 3: Database and SQL

The database is implemented in `database.py` using SQLite.

It contains two relational tables:

### Products table

- `product_id`: primary key.
- `product_name`: product name.
- `category`: product category.
- `unit_price`: price per unit.

### Sales table

- `sale_id`: primary key.
- `product_id`: foreign key referencing the products table.
- `quantity`: number of units sold.
- `sale_date`: date of the sale.
- `payment_method`: payment method used.
- `customer_type`: type of customer.

Primary keys identify records. The foreign key links sales to existing products. SQLite foreign-key enforcement is enabled in the database connection.

### SQL Queries

The project implements five SQL query functions:

1. **Revenue per product:** Joins sales and products and calculates revenue using quantity multiplied by unit price.
2. **Best-selling product:** Calculates the total quantity sold for each product and identifies the highest quantity.
3. **Sales by payment method:** Counts transactions for each payment method.
4. **Revenue by category:** Groups products by category and calculates total revenue.
5. **Customer types in February 2026:** Counts transactions for each customer type during February.

The revenue-per-product query returned the following results in the program's test run:

| Product | Revenue |
|---|---:|
| 5kg Maize Meal | R801.00 |
| Eggs (6 pack) | R364.00 |
| Bar One Chocolate | R224.00 |
| Sugar 1kg | R220.50 |
| Coca-Cola 500ml | R148.00 |
| Airtime Voucher R10 | R140.00 |
| Simba Chips 120g | R132.00 |
| Full Cream Milk 1L | R129.00 |
| Fanta Orange 500ml | R111.00 |
| Data Bundle 1GB | R98.00 |
| Coca-Cola 500ml | R74.00 |
| White Bread 700g | R48.00 |

The revenue figures are calculated from the cleaned sales records and product prices. The two Coca-Cola entries should be checked against their product IDs to confirm whether they represent separate product records.

## 6. Task 4: Python Analysis

The analysis functions are implemented in `analysis.py`. They demonstrate functions, loops, conditionals, lists, dictionaries, and calculations.

The program performs these tasks:
- Counts the cleaned sales records.
- Identifies products that meet the low-stock alert conditions.
- Calculates the total quantity sold in each month.
- Classifies transactions as Single, Multiple, Bulk, or Invalid.
- Calculates the average quantity per sales record.

### Verified Analysis Results

| Measurement | Result |
|---|---:|
| Cleaned sales records | 43 |
| January 2026 quantity sold | 52 |
| February 2026 quantity sold | 44 |
| Average quantity per sales record | 2.23 |
| Low-stock alert | Data Bundle 1GB |

The average basket size is calculated as the average quantity per sales record. It is not a monetary average of customer spending.

The monthly trend is based on quantities sold, not revenue.

## 7. Task 5: Data Visualisation

The chart functions are implemented in `visualize.py` using Matplotlib.

### Revenue per Product

File: `revenue_per_product.png`

This bar chart compares the revenue generated by each product. In the verified output, 5kg Maize Meal generated the highest displayed product revenue at R801.00. This can help the store identify products that contribute strongly to sales revenue.

### Monthly Sales Trend

File: `monthly_trend.png`

This line chart shows the total quantity sold in each month.

The analysis reported:
- January 2026: 52 units.
- February 2026: 44 units.

The quantity sold decreased by 8 units from January to February. The store could investigate whether this change relates to product availability, customer demand, or other factors.

Both charts were generated successfully when `python main.py` was tested.

## 8. Task 6: Security and the CIA Triad

The security functions are implemented in `security.py`.

The program uses Python's `hashlib` library to create a SHA-256 hash of the sample password. When a user enters a password, the program hashes the attempt and compares the resulting hash with the stored hash. The login gate allows up to three attempts.

The security functions were tested successfully: the correct sample password returned `True`, an incorrect password returned `False`, and the hash contained 64 hexadecimal characters.

### CIA Triad Reflection

**Confidentiality:** Confidentiality means that information should only be available to authorised people. The password gate helps protect the sales reports by requiring a password before the program displays them. Hashing means that the sample password is not stored directly as plain text. However, this simple gate is only a learning demonstration and is not complete protection for a real business system.

**Integrity:** Integrity means that data remains accurate and is not changed incorrectly or without permission. The database supports integrity through primary keys, which identify records, and a foreign key that links each sale to an existing product. Required fields and suitable data types also help reduce invalid records. More validation and controlled database permissions would improve protection further.

**Availability:** Availability means that authorised users can access information when they need it. If the laptop is damaged, stolen, or infected with malware, the database and reports could become unavailable. Regular backups stored in a separate secure location would reduce this risk. The backups should also be tested to confirm that the data can be restored.

## 9. Business Insights

The cleaned data provides a clearer view of the store's sales. The original files contained missing information, duplicate records, invalid dates, and sales linked to product IDs that were not valid. After cleaning, the project retained 12 product records and 43 sales records. This gives the analysis a more reliable starting point.

The revenue-per-product query showed that 5kg Maize Meal generated the highest displayed revenue, at R801.00. Eggs (6 pack) followed at R364.00, while Bar One Chocolate generated R224.00. The store could make sure that popular products remain available and monitor whether their prices and costs support good profit margins. Revenue alone does not show profit because the cost of buying each product is not included.

The monthly analysis recorded 52 units sold in January 2026 and 44 units in February 2026. This is a decrease of eight units. The owner could compare future months to see whether this is a continuing pattern. Two months of data are not enough to prove a long-term decline.

The average quantity per sales record was 2.23 units. This may help the owner understand how many units are sold per transaction, but it does not show average spending per customer. The program also flagged Data Bundle 1GB for a low-stock alert under the current analysis rules. The owner should verify the stock information before ordering more.

Overall, the system demonstrates how cleaning data, using a relational database, analysing records, and creating charts can support better store decisions. Adding stock counts, product costs, and more months of sales would allow more detailed analysis.

## 10. Final Submission Checklist

Before submitting, check the project brief and confirm that the submission contains:

- [ ] `PLAN.md`
- [ ] The complete `starter_code/` folder
- [ ] Updated `starter_code/README.md`
- [ ] `revenue_per_product.png`
- [ ] `monthly_trend.png`
- [ ] `store.db`
- [ ] `SUBMISSION.txt`
- [ ] A ZIP file containing the required submission files
- [ ] A GitHub repository with at least eight meaningful commits

The final ZIP should contain the required project files and generated outputs. Check the project brief for any additional submission instructions.

