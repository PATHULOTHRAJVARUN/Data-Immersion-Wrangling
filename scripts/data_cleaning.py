import pandas as pd

# Paths
base_path = "data/raw"
output_path = "data/cleaned"

# Load datasets
customers = pd.read_csv(f"{base_path}/Customers.csv")
products = pd.read_csv(f"{base_path}/Products.csv")
transactions = pd.read_csv(f"{base_path}/Transactions.csv")

# -------------------------
# CLEANING
# -------------------------

# Convert date columns
customers['SignupDate'] = pd.to_datetime(
    customers['SignupDate'], errors='coerce'
)

transactions['TransactionDate'] = pd.to_datetime(
    transactions['TransactionDate'], errors='coerce'
)

# Standardize text
customers['Region'] = customers['Region'].str.strip().str.title()

# Remove duplicates
customers.drop_duplicates(inplace=True)
products.drop_duplicates(inplace=True)
transactions.drop_duplicates(inplace=True)

# Feature Engineering
transactions['OrderYear'] = transactions['TransactionDate'].dt.year
transactions['OrderMonth'] = transactions['TransactionDate'].dt.month

# Merge datasets
final_df = transactions.merge(
    customers, on='CustomerID', how='left'
).merge(
    products, on='ProductID', how='left'
)

# Save cleaned dataset
final_df.to_csv(f"{output_path}/cleaned_dataset.csv", index=False)

print("Cleaning complete ✅")
