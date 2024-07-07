import csv

branchName = "Computer Science"
with open("pgms\student_db.csv") as csvFile:
    reader = csv.DictReader(csvFile)
    print(reader)
    for item in reader:
        if item["Branch"] == branchName:
            print(item["Name"], item["Roll Number"], item["Branch"])
