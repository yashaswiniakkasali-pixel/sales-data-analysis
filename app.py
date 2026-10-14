
import os
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "sales_analysis"),
        port=int(os.getenv("DB_PORT", "3306"))
    )



# Fetch data from MySQL
def fetch_data(query):
    connection = get_connection()
    try:
        return pd.read_sql(query, connection)
    finally:
        connection.close()


# Option 1: Total Revenue and Chart
def show_total_revenue():
    query = """
        SELECT SUM(quantity * unit_price) AS total_revenue
        FROM order_items
    """

    data = fetch_data(query)
    revenue = data.iloc[0]["total_revenue"]

    print("\n===== TOTAL REVENUE =====")
    print("Total Revenue: ₹", revenue)

    if pd.isna(revenue):
        print("No sales data available.")
        return

    plt.figure(figsize=(6, 4))
    plt.bar(["Total Revenue"], [revenue])
    plt.title("Overall Sales Revenue")
    plt.ylabel("Revenue (₹)")
    plt.ticklabel_format(axis="y", style="plain")
    plt.tight_layout()
    plt.savefig("total_revenue_chart.png", bbox_inches="tight")
    plt.show()
    plt.close()


# Option 2: Monthly Sales and Chart
def show_monthly_sales():
    query = """
        SELECT DATE_FORMAT(o.order_date, '%Y-%m') AS month,
               SUM(oi.quantity * oi.unit_price) AS revenue
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY DATE_FORMAT(o.order_date, '%Y-%m')
        ORDER BY month
    """

    data = fetch_data(query)

    print("\n===== MONTHLY SALES =====")
    print(data.to_string(index=False))

    if data.empty:
        print("No monthly sales data found.")
        return

    data.plot(
        x="month",
        y="revenue",
        kind="bar",
        legend=False,
        title="Monthly Sales Revenue"
    )

    plt.xlabel("Month")
    plt.ylabel("Revenue (₹)")
    plt.tight_layout()
    plt.savefig("monthly_sales_chart.png", bbox_inches="tight")
    plt.show()
    plt.close()


# Option 3: Top Products and Chart
def show_top_products():
    query = """
        SELECT p.product_name,
               SUM(oi.quantity) AS units_sold,
               SUM(oi.quantity * oi.unit_price) AS revenue
        FROM products p
        JOIN order_items oi ON p.product_id = oi.product_id
        GROUP BY p.product_id, p.product_name
        ORDER BY revenue DESC
    """

    data = fetch_data(query)

    print("\n===== TOP PRODUCTS =====")
    print(data.to_string(index=False))

    if data.empty:
        print("No product sales data found.")
        return

    data.plot(
        x="product_name",
        y="revenue",
        kind="bar",
        legend=False,
        title="Revenue by Product"
    )

    plt.xlabel("Product")
    plt.ylabel("Revenue (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("top_products_chart.png", bbox_inches="tight")
    plt.show()
    plt.close()


# Option 4: Customer Spending and Chart
def show_customer_spending():
    query = """
        SELECT c.customer_name,
               SUM(oi.quantity * oi.unit_price) AS total_spending
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY c.customer_id, c.customer_name
        ORDER BY total_spending DESC
    """

    data = fetch_data(query)

    print("\n===== CUSTOMER SPENDING =====")
    print(data.to_string(index=False))

    if data.empty:
        print("No customer spending data found.")
        return

    data.plot(
        x="customer_name",
        y="total_spending",
        kind="bar",
        legend=False,
        title="Customer Spending Analysis"
    )

    plt.xlabel("Customer Name")
    plt.ylabel("Total Spending (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("customer_spending_chart.png", bbox_inches="tight")
    plt.show()
    plt.close()


# Main menu
def main():
    while True:
        print("\n===== SALES DATA ANALYSIS SYSTEM =====")
        print("1. Total Revenue and Chart")
        print("2. Monthly Sales and Chart")
        print("3. Top Products and Chart")
        print("4. Customer Spending and Chart")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                show_total_revenue()

            elif choice == "2":
                show_monthly_sales()

            elif choice == "3":
                show_top_products()

            elif choice == "4":
                show_customer_spending()

            elif choice == "5":
                print("Thank you for using Sales Data Analysis System!")
                break

            else:
                print("Please enter a number from 1 to 5.")

        except mysql.connector.Error as error:
            print("MySQL error:", error)

        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
