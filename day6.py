student = {
    "name": "Purnima",
    "age": 19,
    "course": "BCA",
    "marks": 80
}

print("Student Information")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])

# Update marks
student["marks"] = 85

print("Updated Marks:", student["marks"])

# Add a new item
student["result"] = "Pass"

print("Result:", student["result"])