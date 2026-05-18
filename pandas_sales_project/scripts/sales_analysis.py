import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

file_path = BASE_DIR / "data" / "sales.csv"

df = pd.read_csv(file_path)

# 1. clean missing price 
df["price"] = df["price"].fillna(df.groupby("category")["price"].median())

# 2. clean duplicate rows
df = df.drop_duplicates()

# 3. negative price
df = df[df["price"] > 0]

# 4. clean inconsistent category names
df["category"] = df["category"].str.title()

# 5. Add revenue columns
df["revenue"] = df["quantity"] * df ["price"]

print("Revenue by Category")
print(df.groupby("category")["revenue"].sum().sort_values(ascending = False))
