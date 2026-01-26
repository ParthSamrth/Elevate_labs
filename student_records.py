import json

# 1. Store student details using dictionary
students = {
    101: {"name": "Parth", "age": 21, "course": "B.Tech", "marks": 85},
    102: {"name": "Riya", "age": 20, "course": "BCA", "marks": 90},
    103: {"name": "Aman", "age": 22, "course": "B.Sc", "marks": 78}
}

print("\n--- Original Student Records ---")
for roll, data in students.items():
    print(roll, ":", data)

# 2. Access keys and values
print("\nAccessing Keys:", students.keys())
print("Accessing Values:", students.values())

# 3. Update an entry
students[101]["marks"] = 88

# 4. Delete an entry
del students[103]

# 5. Loop through dictionary
print("\n--- Updated Student Records ---")
for roll, info in students.items():
    print(f"Roll No: {roll}")
    for key, value in info.items():
        print(f"   {key}: {value}")

# 6. Convert dictionary to JSON
json_data = json.dumps(students, indent=4)

# 7. Save JSON to file
with open("students.json", "w") as file:
    file.write(json_data)

print("\nData saved to students.json")

# 8. Read JSON back into Python
with open("students.json", "r") as file:
    data_from_json = json.load(file)

# 9. Print clean formatted output
print("\n--- Data Read From JSON File ---")
for roll, info in data_from_json.items():
    print(f"Roll No: {roll}")
    for key, value in info.items():
        print(f"   {key}: {value}")
