import csv


# Read the student database file (assuming it's a CSV)
def read_student_database(file_path):
    students = []
    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            students.append(row)
    return students


# Search for students by branch
def search_students_by_branch(students, target_branch):
    matching_students = []
    for student in students:
        if student["Branch"] == target_branch:
            matching_students.append(student)
    return matching_students


# Example usage
if __name__ == "__main__":
    database_file = "pgms\student_db.csv"  # Replace with your actual file path
    all_students = read_student_database(database_file)

    branch_to_search = input("Enter the branch name: ")
    matching_students = search_students_by_branch(all_students, branch_to_search)

    if matching_students:
        print("Matching students:")
        for student in matching_students:
            print(f"Name: {student['Name']}, Roll Number: {student['Roll Number']}")
    else:
        print("No students found for the given branch.")
