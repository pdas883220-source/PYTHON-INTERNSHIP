marks = [78, 82, 75, 88, 80]

print("Student Marks:")

# For loop
for mark in marks:
    print(mark)

# Find total using a loop
total = 0

for mark in marks:
    total = total + mark

print("Total Marks:", total)

# Find passed marks
passed_marks = []

for mark in marks:
    if mark >= 40:
        passed_marks.append(mark)

print("Passed Marks:", passed_marks)

# While loop
count = 1

print("Counting:")

while count <= 5:
    print(count)
    count = count + 1