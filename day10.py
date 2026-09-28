marks = [78, 82, 75, 88, 80]

def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average

average = calculate_average(marks)

print("Student Marks:", marks)
print("Average Marks:", average)

if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")