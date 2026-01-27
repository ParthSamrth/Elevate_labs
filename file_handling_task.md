# 📁 Task 8 – File Handling in Python (TXT & CSV)

## 🧠 Overview
This project demonstrates file handling in Python using both **Text (TXT)** and **CSV** files.  
It covers writing, reading, appending data, handling errors, and using Python’s built-in `csv` module.

This task was part of my **Python Developer Internship** to understand how real applications store and manage data using files.

---

## 🛠 Tools Used
- Python  
- VS Code  

---

## 📂 Files in this Repository

| File | Purpose |
|------|---------|
| [`file_handling_task.py`](./file_handling_task.py) | Python program for TXT and CSV operations |
| [`users.txt`](./users.txt) | Text file storing user data |
| [`students.csv`](./students.csv) | CSV file storing student records |
| [`README.md`](./README.md) | Project explanation |
---
## 🔹 TXT File Operations
The program performs:
- Creating a text file
- Writing user data
- Reading file content
- Appending new data
- Handling file errors using try-except
- Closing files automatically using context manager (`with`)

---

## 🔹 CSV File Operations
Using Python’s `csv` module, the program:
- Creates a CSV file
- Writes multiple rows
- Reads data from CSV
- Displays records in row format

---

## 📌 Sample Data

### users.txt
```
python
import csv

# ------------------------------
# TEXT FILE OPERATIONS
# ------------------------------

txt_file = "users.txt"

try:
    # 1. Create & Write to Text File
    with open(txt_file, "w") as file:
        file.write("Name, Age, Email\n")
        file.write("Parth, 21, parth@gmail.com\n")
        file.write("Aman, 22, aman@gmail.com\n")

    print("Text file created and data written successfully.")

    # 2. Read Text File
    print("\nReading text file:")
    with open(txt_file, "r") as file:
        print(file.read())

    # 3. Append Data
    with open(txt_file, "a") as file:
        file.write("Riya, 20, riya@gmail.com\n")

    print("Data appended successfully.")

    # 4. Read Again
    print("\nUpdated text file:")
    with open(txt_file, "r") as file:
        print(file.read())

except Exception as e:
    print("Error in text file handling:", e)


# ------------------------------
# CSV FILE OPERATIONS
# ------------------------------

csv_file = "students.csv"

try:
    # 5. Create & Write CSV
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll No", "Name", "Marks"])
        writer.writerow([1, "Parth", 89])
        writer.writerow([2, "Aman", 76])
        writer.writerow([3, "Riya", 92])

    print("CSV file created and data written successfully.")

    # 6. Read CSV File
    print("\nReading CSV file:")
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

except Exception as e:
    print("Error in CSV file handling:", e)
```
## Output
<img width="1173" height="360" alt="image" src="https://github.com/user-attachments/assets/8fe7c5e0-7fd5-4473-bbbc-02a020b19b8e" />


