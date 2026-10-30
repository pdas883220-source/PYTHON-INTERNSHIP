# Day 44 - Student Management System

students = []

# Add student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


# View students
def view_students():
    if not students:
        print("No student records found.")
    else:
        print("\nStudent Records:")
        for student in students:
            print("Name:", student["name"])
            print("Roll Number:", student["roll"])
            print("Marks:", student["marks"])
            print("-------------------")


# Search student
def search_student():
    roll = input("Enter roll number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("Student Found!")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


# Delete student
def delete_student():
    roll = input("Enter roll number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# Main menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice. Please try again.")