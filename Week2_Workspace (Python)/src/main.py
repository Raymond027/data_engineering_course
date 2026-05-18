import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

file_path = BASE_DIR / "data" / "sales.csv"

df = pd.read_csv(file_path, on_bad_lines="skip")

# Filtering Data
print(df[
    (df["country"] == "USA")
    & (df["revenue"] > 100)
])

# 

# # print(df.head(5))
# print(df.info()) 
# # print(df.describe())
# print(df.shape)
# print(df.columns)

#df.to_csv("../output/cleaned_sales.csv", index=False)

