# Sales Data Analysis System

## Project Overview
The Sales Data Analysis System is a Python-based project connected to a MySQL database. It analyses sales information and generates reports and charts to help understand business performance.

## Technologies Used
- Python
- MySQL
- Pandas
- Matplotlib
- SQL

## Features
1. Calculate total sales revenue.
2. Analyse monthly sales revenue.
3. Identify top-selling products by revenue.
4. Analyse customer spending.
5. Generate charts for sales analysis.
6. Display reports through a menu-driven application.

## Database Tables
- `customers` — stores customer information.
- `products` — stores product information.
- `orders` — stores order information.
- `order_items` — stores product quantities and prices for orders.

## Project Structure
- `app.py` — main Python application.
- `README.md` — project documentation.
- `total_revenue_chart.png` — total revenue chart.
- `monthly_sales_chart.png` — monthly sales chart.
- `top_products_chart.png` — product revenue chart.
- `customer_spending_chart.png` — customer spending chart.

## How to Run

1. Install Python and MySQL.
2. Install the required Python libraries:

   `pip install mysql-connector-python pandas matplotlib`

3. Create the `sales_analysis` database and its required tables in MySQL.
4. Configure your MySQL connection credentials in the Python application.
5. Run the application from the project folder:

   `python app.py`

6. Select a menu option to view a report and chart.

## Learning Outcomes
- Connecting Python with a MySQL database.
- Writing SQL queries using JOIN, GROUP BY, and aggregate functions.
- Analysing data using Pandas.
- Visualising sales information using Matplotlib.