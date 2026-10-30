
# Day 30 - Python CSV File Handling

import csv

# Student records
students = [
    ["Name", "Course", "Marks"],
    ["Purnima", "BCA", 85],
    ["Anjali", "BCA", 90],
    ["Riya", "BCA", 88]
]

# Write data into a CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("Student data written successfully.")

# Read data from the CSV file
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    print("\nStudent Records:")
    for row in reader:
        print(row)
