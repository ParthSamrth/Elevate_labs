"""
Task 2: Variables, Data Types & Type Conversion
Python Developer Internship
"""

# 1. Declaring variables of different data types
age = 21                  # int
height = 5.9              # float
name = "Parth"            # string
is_student = True         # boolean

# 2. Printing values and their types
print("Age:", age, "Type:", type(age))
print("Height:", height, "Type:", type(height))
print("Name:", name, "Type:", type(name))
print("Is Student:", is_student, "Type:", type(is_student))

print("-" * 40)

# 3. Arithmetic operations
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("-" * 40)

# 4. Type conversion from string input
user_input = input("Enter a number: ")

try:
    # Converting string to integer
    num_int = int(user_input)
    print("Integer value:", num_int)

    # Converting string to float
    num_float = float(user_input)
    print("Float value:", num_float)

except ValueError:
    print("Invalid input! Please enter a numeric value.")

print("-" * 40)

# 5. Concatenating strings and numbers
marks = 85

# Correct way using str() conversion
print("Your marks are " + str(marks))

# Using f-string (recommended)
print(f"Your marks are {marks}")

print("-" * 40)

# 6. Demonstrating dynamic typing
value = 100
print("Value:", value, "Type:", type(value))

value = "Now I am a string"
print("Value:", value, "Type:", type(value))

value = 99.99
print("Value:", value, "Type:", type(value))
