# Day 34 - Python File Handling

# Write data into a file
with open("student_info.txt", "w") as file:
    file.write("Name: Purnima\n")
    file.write("Course: BCA\n")
    file.write("Marks: 85\n")

print("Data written successfully.")

# Read data from the file
with open("student_info.txt", "r") as file:
    print("\nStudent Information:")
    print(file.read())

# Append new data to the file
with open("student_info.txt", "a") as file:
    file.write("College: Centurion University\n")

print("New data added successfully.")

# Read updated data
with open("student_info.txt", "r") as file:
    print("Updated Student Information:")
    print(file.read())