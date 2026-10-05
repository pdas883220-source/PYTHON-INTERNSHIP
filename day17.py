# Day 17 - Python List Comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original List:", numbers)

# Create a list of even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print("Even Numbers:", even_numbers)

# Create a list of squares
squares = [num * num for num in numbers]

print("Squares:", squares)