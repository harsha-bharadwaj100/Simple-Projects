import pandas as pd

dl = [
    [89, 95, 91, 88],
    [99, 90, 87, 91],
    [98, 97, 92, 92],
]

data = {
    "Student1": [89, 95, 91, 88],
    "Student2": [99, 90, 87, 91],
    "Student3": [98, 97, 92, 92],
}
sts = ["s1", "s2", "s3"]
subjects = ["Math", "Science", "English", "Social"]
df = pd.DataFrame(data, index=subjects)
dfdl = pd.DataFrame(dl, columns=subjects, index=sts)
print(dfdl)
print(df)
students_avg = df.mean(axis=0)
print("students_avg:")
print(students_avg)
print(students_avg.idxmax(), students_avg.idxmin())
subjects_avg = df.mean(axis=1)
print("subjects_avg:")
print(subjects_avg)
print(subjects_avg.idxmax(), subjects_avg.idxmin())
