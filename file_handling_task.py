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
