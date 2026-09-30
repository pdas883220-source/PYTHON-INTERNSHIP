marks = [78, 82, 75, 88, 80]

try:
    index = int(input("Enter a mark index (0-4): "))
    print("Selected Mark:", marks[index])

except ValueError:
    print("Error: Please enter a valid number.")

except IndexError:
    print("Error: Index must be between 0 and 4.")

finally:
    print("Program execution completed.")