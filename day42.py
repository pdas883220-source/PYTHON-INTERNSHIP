# Day 42 - Python Data Visualization

import matplotlib.pyplot as plt

# Student names and marks
students = ["Amit", "Riya", "Purnima", "Anjali", "Rahul"]
marks = [75, 85, 90, 80, 70]

# Create a figure with three graphs
plt.figure(figsize=(12, 10))

# Bar Chart
plt.subplot(3, 1, 1)
plt.bar(students, marks)
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")

# Line Graph
plt.subplot(3, 1, 2)
plt.plot(students, marks, marker="o")
plt.title("Student Performance - Line Graph")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)

# Pie Chart
plt.subplot(3, 1, 3)
plt.pie(marks, labels=students, autopct="%1.1f%%")
plt.title("Student Marks - Pie Chart")

# Display all graphs
plt.tight_layout()
plt.show()