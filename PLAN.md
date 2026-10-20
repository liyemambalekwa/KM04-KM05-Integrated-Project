# Thabo's Corner Store — Project Plan

## 1. Problem Decomposition

I will divide the project into smaller tasks to make it easier to complete. First, I will inspect and clean the product and sales CSV files. Next, I will create a relational SQLite database to store the cleaned data. Then, I will use Python to analyse sales and calculate useful information, such as revenue per product. After that, I will create charts to display the results. I will also add a password-protection system to protect the reports. Finally, I will document my work in the README file, test the complete system, and submit the project on UpSkill and GitHub.

## 2. Pattern Recognition

I expect to find missing product names, missing prices, inconsistent product categories, missing quantities, different date formats, invalid product references, and duplicate records. I will inspect the data to identify these problems and look for patterns that can help me clean the information consistently.

## 3. Abstraction

I will focus on the information needed to understand the store's sales, including product names, categories, prices, quantities sold, sale dates, and payment methods. I will not use information that is unnecessary for calculating sales or answering the business questions. I will document my decisions when handling missing or invalid data.

## 4. Algorithm Design

I will follow these steps:

1. Inspect the raw CSV files and create this project plan.
2. Clean the product and sales data using Python.
3. Create the SQLite database and insert the cleaned records.
4. Write SQL queries to answer business questions.
5. Use Python functions, loops, conditionals, lists, and dictionaries to analyse the data.
6. Create a bar chart and a line chart using Matplotlib.
7. Add password protection using SHA-256 hashing.
8. Document the cleaning decisions, query results, charts, security choices, and business insights in README.md.
9. Test the application, commit my progress to GitHub, and prepare the ZIP file for submission.

## 5. Development Approach

I will work through the project one task at a time. I will test each part before moving to the next task and use Git commits to record my progress. This approach will help me identify errors early and demonstrate my understanding of data cleaning, databases, programming, visualisation, and security.