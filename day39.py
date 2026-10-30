# Day 39 - Python Database Connectivity using SQLite

import sqlite3

# Connect to the database
connection = sqlite3.connect("student.db")

# Create a cursor
cursor = connection.cursor()

# Create a student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    course TEXT,
    marks INTEGER
)
""")

# Insert student records
cursor.execute(
    "INSERT INTO students (name, course, marks) VALUES (?, ?, ?)",
    ("Purnima", "BCA", 85)
)

cursor.execute(
    "INSERT INTO students (name, course, marks) VALUES (?, ?, ?)",
    ("Anjali", "BCA", 90)
)

# Save changes
connection.commit()

# Display student records
cursor.execute("SELECT * FROM students")

print("Student Records:")

for student in cursor.fetchall():
    print(student)

# Close the connection
connection.close()

print("Database connection closed.")