import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD THE DATA
df = pd.read_csv("online_shop_sales.csv")

print("=== Preview of Data ===")
print(df.head())
print("\nShape of data (rows, columns):", df.shape)

# 2. CREATE A NEW COLUMN (UNIQUE TOUCH)
# Revenue = Quantity * Price
df["Revenue"] = df["Quantity"] * df["Price"]
print("\n=== Data with Revenue column added ===")
print(df[["OrderID", "Product", "Quantity", "Price", "Revenue"]].head())

# 3. BASIC STATISTICS
print("\n=== Basic Statistics ===")
print("Average Quantity per order:", df["Quantity"].mean())
print("Average Price of products:", df["Price"].mean())
print("Average Revenue per order:", df["Revenue"].mean())
print("Average Rating:", df["Rating"].mean())

# Group-wise analysis: total revenue by category
revenue_by_category = df.groupby("Category")["Revenue"].sum()
print("\n=== Total Revenue by Category ===")
print(revenue_by_category)

# 4. VISUALIZATIONS

# (a) BAR CHART – Total Revenue by Category
plt.figure()
revenue_by_category.plot(kind="bar")
plt.title("Total Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue (₹)")
plt.tight_layout()
plt.savefig("bar_revenue_by_category.png")  # also saved as image
plt.show()

# (b) SCATTER PLOT – Price vs Rating
plt.figure()
plt.scatter(df["Price"], df["Rating"])
plt.title("Price vs Rating")
plt.xlabel("Price (₹)")
plt.ylabel("Customer Rating")
plt.tight_layout()
plt.savefig("scatter_price_rating.png")
plt.show()

# (c) HEATMAP – Correlation between numeric features
plt.figure()
numeric_cols = ["Quantity", "Price", "Revenue", "Rating"]
corr_matrix = df[numeric_cols].corr()
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("heatmap_correlations.png")
plt.show()