# Grade Calculator Program
# This program takes marks as input and assigns a grade using conditional statements

def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid marks! Please enter marks between 0 and 100."

    if marks >= 90:
        return "Grade A+ : Excellent performance"
    elif marks >= 80 and marks < 90:
        return "Grade A : Very good"
    elif marks >= 70 and marks < 80:
        return "Grade B : Good"
    elif marks >= 60 and marks < 70:
        return "Grade C : Average"
    elif marks >= 50 and marks < 60:
        return "Grade D : Needs improvement"
    else:
        return "Grade F : Fail"


# Taking input from user
try:
    marks = int(input("Enter your marks (0 - 100): "))
    result = calculate_grade(marks)
    print(result)
except ValueError:
    print("Invalid input! Please enter numeric values only.")
