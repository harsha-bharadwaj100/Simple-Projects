import pandas as pd

# Create a dictionary with the provided information
team_data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 28, 35],
    "Salary": [60000, 75000, 90000],
}

# Create a DataFrame from the dictionary
team_df = pd.DataFrame(team_data)

# Display the first 3 rows
print("First 3 rows of the team DataFrame:")
print(team_df.head(3))

# Calculate and print the average salary
average_salary = team_df["Salary"].mean()
print(f"\nAverage salary of the team: ${average_salary:.2f}")
