import pandas as pd

file_path = r'C:\Users\prema\Desktop\Pandas Test\simple-pyton-project\orders.csv'


# Step 1: Load the dataset
orders = pd.read_csv(file_path)
# print("Data Loaded Successfully!\n")

# Step 2: Preview the data
print("Preview of the Dataset:")
print(orders.head(), "\n")


# Step 3: Check for missing values
# print("Missing Values in Each Column:")
# print(orders.isnull().sum(), "\n")