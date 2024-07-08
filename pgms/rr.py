# import numpy as np

# # Create a 2D array (3x3 matrix)
# my_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # Access individual elements
# print(f"Element at row 1, column 2: {my_matrix[1, 2]}")  # 6
# print(f"Element at row 2, column 0: {my_matrix[2, 0]}")  # 7
import pandas as pd

# # Create a DataFrame from a dictionary
# data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 22]}
# df = pd.DataFrame(data)

# print(df)

# # Create a Series
# ages = pd.Series([25, 30, 22], name="Age")
# print(ages)

# Create two DataFrames
df1 = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Alice", "Bob", "Charlie"]})
df2 = pd.DataFrame({"ID": [2, 3, 4], "Salary": [50000, 60000, 70000]})
print(df1)
print(df2)
# Merge based on 'ID'
result = pd.merge(df1, df2, on="ID", how="inner")
print(result)
