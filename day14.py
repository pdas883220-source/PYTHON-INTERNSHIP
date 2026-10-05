# Day 14 - Python Dictionary

student = {
    "name": "Purnima",
    "course": "BCA",
    "age": 19,
    "marks": 80
}

print("Student Information:")
print("Name:", student["name"])
print("Course:", student["course"])
print("Age:", student["age"])
print("Marks:", student["marks"])

# Add a new item
student["city"] = "Bhubaneswar"

print("\nUpdated Student Information:")
print(student)