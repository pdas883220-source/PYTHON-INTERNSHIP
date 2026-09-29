with open("student.txt", "w") as file:
    file.write("Name: Purnima\n")
    file.write("Course: BCA\n")
    file.write("Marks: 80\n")

print("Student data written successfully.")

# Read data from the file
with open("student.txt", "r") as file:
    data = file.read()

print("\nStudent Information:")
print(data)


