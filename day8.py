student_name = "Purnima Das"
course = "BCA Python Internship"

print("Student Name:", student_name)
print("Course:", course)

# Convert to uppercase and lowercase
print("Uppercase:", student_name.upper())
print("Lowercase:", student_name.lower())

# Find length
print("Name Length:", len(student_name))

# Replace text
updated_course = course.replace("Python", "Programming")
print("Updated Course:", updated_course)

# Split the name
name_parts = student_name.split()
print("Name Parts:", name_parts)

# Check whether a word exists
if "Purnima" in student_name:
    print("Name Found: Yes")
else:
    print("Name Found: No")