def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


def check_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"


name = "Purnima"
marks = [78, 82, 75, 88, 80]

average = calculate_average(marks)
result = check_result(average)

print("Student Name:", name)
print("Marks:", marks)
print("Average:", average)
print("Result:", result)