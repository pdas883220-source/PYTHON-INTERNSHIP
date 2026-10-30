# Day 33 - Python Exception Handling

# Example 1: Handling division by zero
try:
    a = 10
    b = 0
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Example 2: Handling invalid input
try:
    number = int("abc")
    print("Number:", number)

except ValueError:
    print("Error: Invalid input.")

# Example 3: Using else and finally
try:
    x = 20
    y = 5
    result = x / y

except ZeroDivisionError:
    print("Division error.")

else:
    print("Division result:", result)

finally:
    print("Program execution completed.")