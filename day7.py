# Tuple
student_details = ("Purnima", 19, "BCA", 8.0)

print("Student Details:")
print("Name:", student_details[0])
print("Age:", student_details[1])
print("Course:", student_details[2])
print("CGPA:", student_details[3])

# Set
subjects = {"Python", "Java", "HTML", "Python", "JavaScript"}

print("\nSubjects:")
print(subjects)

print("Number of Unique Subjects:", len(subjects))

# Add a new subject
subjects.add("SQL")

print("After Adding SQL:")
print(subjects)

# Remove a subject
subjects.remove("HTML")

print("After Removing HTML:")
print(subjects)