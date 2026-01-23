# 📦 Task 6 – Lists, Tuples & Sets (Python Internship)

This project is part of **Python Developer Internship – Task 6**.  
It demonstrates how to work with **Lists, Tuples, and Sets** in Python.

---

## 📌 Objective
To understand:
- List operations
- Tuple (immutable data)
- Set (unique elements)
- Removing duplicates
- Set operations
- Mutable vs Immutable

---

## 🛠 Concepts Used
- List
- Tuple
- Set
- Iteration
- Sorting
- Formatting output

---

## ▶ How to Run

1. Create a file named `collections_demo.py`
2. Copy the code below into it
3. Run:
```bash
python collections_demo.py
```
```
python
# -------- LIST --------
students = ["Parth", "Amit", "Neha", "Riya", "Amit"]

print("Original List:", students)

# Add a student
students.append("Rahul")
print("After Adding Rahul:", students)

# Remove a student
students.remove("Neha")
print("After Removing Neha:", students)

# Sort list
students.sort()
print("Sorted List:", students)


# -------- TUPLE --------
# Tuple for fixed data (immutable)
college_info = ("ABC Engineering College", 2025)
print("\nCollege Info (Tuple):", college_info)


# -------- SET --------
# Convert list to set to remove duplicates
student_set = set(students)
print("\nSet (Duplicates Removed):", student_set)

# Another set
new_students = {"Riya", "Karan", "Amit"}

# Set operations
print("\nUnion:", student_set.union(new_students))
print("Intersection:", student_set.intersection(new_students))
print("Difference:", student_set.difference(new_students))


# -------- ITERATION --------
print("\nIterating over student set:")
for s in student_set:
    print(s)


# -------- MUTABLE vs IMMUTABLE --------
print("\nMutable vs Immutable")
print("List is mutable (can change)")
students.append("Sonal")
print("Updated List:", students)

print("Tuple is immutable (cannot change)")
# college_info[0] = "XYZ College"   # This will give an error


# -------- FORMATTED OUTPUT --------
print("\nFormatted Output:")
print(f"Total Students in List: {len(students)}")
print(f"Total Unique Students: {len(student_set)}")
```
## Output
<img width="914" height="641" alt="image" src="https://github.com/user-attachments/assets/5127399e-b255-4d77-bb7e-5a68b92840db" />
