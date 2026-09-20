name = "Purnima"
age = 19
marks = [78, 82, 75, 88, 80]

print("Name:", name)
print("Age:", age)

total = sum(marks)
average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)

if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
    