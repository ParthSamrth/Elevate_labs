# Grade Calculator using Python

This project is a simple **Grade Calculator** built using Python.  
It is created as part of **Task 3: Conditional Statements & Logical Flow** for the Python Developer Internship.

The main goal of this task is to understand how **if-elif-else**, **logical operators**, and **nested conditions** work in real-life scenarios.

---

## 🔧 Tools Used
- Python
- VS Code

---

## 📌 What This Program Does
- Takes marks as input from the user
- Checks for invalid input (less than 0 or greater than 100)
- Uses conditional statements to calculate grades
- Displays appropriate messages for each grade
- Uses logical operators like `and`, `or`
- Handles runtime input errors

---

## 🧠 Logic Used
- `if-elif-else` for grade decision
- Logical conditions to define grade ranges
- Separate function to improve readability
- Error handling using `try-except`

---

## 🧪 Grade Rules
| Marks Range | Grade |
|------------|-------|
| 90 – 100   | A+    |
| 80 – 89    | A     |
| 70 – 79    | B     |
| 60 – 69    | C     |
| 50 – 59    | D     |
| Below 50   | F     |

---

## 💻 Code

```python
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
```
## Output
<img width="643" height="140" alt="image" src="https://github.com/user-attachments/assets/5114d2a5-492f-436b-a70c-23af9fbc73d9" />

