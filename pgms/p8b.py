import numpy as np

# Create a sample 2D array (rows represent students, columns represent subjects)
student_scores = np.array(
    [
        [85, 88, 93],  # Student 1: Maths, Science, English
        [90, 100, 97],  # Student 2: Maths, Science, English
        [50, 68, 73],  # Student 3: Maths, Science, English
        # Add more rows for other students if needed
    ]
)

# Calculate the average score for each subject (column-wise)
subject_averages = np.mean(student_scores, axis=0)

# Find the index of the subject with the highest average
strongest_subject_index = np.argmax(subject_averages)

# Get the subject name based on the index (e.g., 0 for Maths, 1 for Science, 2 for English)
subjects = ["Maths", "Science", "English"]
strongest_subject = subjects[strongest_subject_index]

print(f"The subject with the highest average score is {strongest_subject}.")
