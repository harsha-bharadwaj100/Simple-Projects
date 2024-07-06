# A company decided to give bonus of 5% to employee if his/her year of service is more
# than 5 years. Ask user for their salary and year of service and print the net bonus amount.
# salary = float(input("Enter salary: "))
# yos = int(input("Years of Service: "))

# if yos > 5:
#     bonus = salary * 0.05
#     salary += bonus

# print(salary)

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
import pandas as pd

data = np.array(
    [
        [170, 65, 30],
        [175, 70, 35],
        [180, 75, 40],
        [165, 60, 25],
        [168, 63, 28],
        [172, 68, 32],
        [178, 73, 38],
        [162, 58, 22],
        [166, 62, 27],
        [182, 77, 42],
    ]
)

col = ["height", "weight", "age"]
df = pd.DataFrame(data, columns=col)
print(df)
median_height = df["height"].median()
median_weight = df["weight"].median()
median_age = df["age"].median()

print("Median Height:", median_height)
print("Median Weight:", median_weight)
print("Median Age:", median_age)
