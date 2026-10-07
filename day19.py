# Lambda function for addition
add = lambda a, b: a + b

# Lambda function for square
square = lambda x: x * x

# Lambda function to check even number
is_even = lambda x: x % 2 == 0

num1 = 10
num2 = 5

print("First Number:", num1)
print("Second Number:", num2)
print("Addition:", add(num1, num2))
print("Square of First Number:", square(num1))

if is_even(num1):
    print(num1, "is an even number.")
else:
    print(num1, "is an odd number.")