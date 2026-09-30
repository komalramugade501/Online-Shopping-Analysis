import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/shopping_data.csv")
df["Revenue"] = df["Quantity"] * df["Price"]

print("Dataset:")
print(df.to_string(index=False))
print("\nTotal Revenue:", df["Revenue"].sum())
print("Average Order Value:", round(df["Revenue"].mean(), 2))

customer_sales = df.groupby("Customer")["Revenue"].sum().sort_values(ascending=False)
print("\nRevenue by Customer:")
print(customer_sales)

plt.figure(figsize=(8, 5))
customer_sales.plot(kind="bar")
plt.title("Revenue by Customer")
plt.xlabel("Customer")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("customer_revenue.png", dpi=150)
plt.show()
