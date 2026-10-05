# Day 15 - Python Sets

numbers = {10, 20, 30, 40, 50}

print("Original Set:", numbers)

# Add an element
numbers.add(60)
print("After adding 60:", numbers)

# Remove an element
numbers.remove(20)
print("After removing 20:", numbers)

# Check if an element exists
if 30 in numbers:
    print("30 is present in the set.")
else:
    print("30 is not present in the set.")

# Find the number of elements
print("Number of elements:", len(numbers))