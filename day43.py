# Day 43 - Python Data Analysis using Pandas

import pandas as pd

# Create student data
data = {
    "Name": ["Purnima", "Anjali", "Riya", "Amit", "Rahul"],
    "Course": ["BCA", "BCA", "BCA", "BCA", "BCA"],
    "Marks": [85, 90, 78, 92, 70],
    "Attendance": [90, 95, 85, 92, 80]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Student Records:")
print(df)

# Calculate average marks
average = df["Marks"].mean()
print("\nAverage Marks:", average)

# Find highest marks
highest = df["Marks"].max()
print("Highest Marks:", highest)

# Find lowest marks
lowest = df["Marks"].min()
print("Lowest Marks:", lowest)

# Filter students scoring above 80
print("\nStudents Scoring Above 80:")
print(df[df["Marks"] > 80])

# Sort students by marks
print("\nStudents Sorted by Marks:")
print(df.sort_values(by="Marks", ascending=False))