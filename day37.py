# Day 37 - Python Generators

# Creating a generator function
def number_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


# Calling the generator
numbers = number_generator()

print("Generated Numbers:")

for number in numbers:
    print(number)


# Generator with a range
def even_numbers(limit):
    for number in range(2, limit + 1, 2):
        yield number


print("\nEven Numbers:")

for number in even_numbers(10):
    print(number)