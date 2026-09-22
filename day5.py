marks = [78, 82, 75, 88, 80]

print("Student Marks:", marks)

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

passed_marks = [mark for mark in marks if mark >= 40]

print("Passed Marks:", passed_marks)