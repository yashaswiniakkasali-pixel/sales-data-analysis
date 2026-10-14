
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NewPass123!",
    database="sales_analysis"
)

query = """
SELECT
    p.product_name,
    SUM(oi.quantity) AS total_quantity_sold,
    SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_revenue DESC
LIMIT 5;
"""

df = pd.read_sql(query, conn)

print(df.to_string(index=False))

plt.bar(df["product_name"], df["total_revenue"])
plt.title("Top 5 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

conn.close()
