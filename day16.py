student = ("Purnima", "BCA", 19, 80)

print("Student Tuple:", student)

print("Name:", student[0])
print("Course:", student[1])
print("Age:", student[2])
print("Marks:", student[3])

# Tuple length
print("Number of elements:", len(student))

# Check if an item exists
if "BCA" in student:
    print("BCA is present in the tuple.")
else:
    print("BCA is not present in the tuple.")