
# Day 29 - Python JSON Handling

import json

# Create a student dictionary
student = {
    "name": "Purnima",
    "course": "BCA",
    "age": 19,
    "marks": 85
}

# Convert dictionary to JSON string
json_data = json.dumps(student, indent=4)

print("Student Data in JSON Format:")
print(json_data)

# Convert JSON string back to Python dictionary
student_data = json.loads(json_data)

print("\nStudent Information:")
print("Name:", student_data["name"])
print("Course:", student_data["course"])
print("Age:", student_data["age"])
print("Marks:", student_data["marks"])

