class Student:
    def __init__(self, name, course, marks):
        self.name = name
        self.course = course
        self.marks = marks

    def display_details(self):
        print("Student Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)


# Create a student object
student1 = Student("Purnima", "BCA", 80)

# Display student details
student1.display_details()