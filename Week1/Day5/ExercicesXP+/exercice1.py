#Exercise 1 : Student Grade Summary
"""
Instructions

You are given a dictionary containing student names as keys and lists of their grades as values. Your task is to create a summary report that calculates the average grade for each student, assigns a letter grade, and determines the class average.

"""

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

student_averages = {}
student_letter_grades = {}

for student, grades in student_grades.items():
    avg = sum(grades) / len(grades)
    student_averages[student] = avg

    if avg >= 90:
        letter = "A"
    elif avg >= 80:
        letter = "B"
    elif avg >= 70:
        letter = "C"
    elif avg >= 60:
        letter = "D"
    else:
        letter = "F"
    student_letter_grades[student] = letter

class_average = sum(student_averages.values()) / len(student_averages)


for student in student_grades:
    print(f"{student}: Average = {student_averages[student]:.2f}, Letter Grade = {student_letter_grades[student]}")

print(f"\nClass Average: {class_average:.2f}")
    