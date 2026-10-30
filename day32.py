# Day 32 - Python Regular Expressions

import re

# Sample text
text = "My name is Purnima. My phone number is 9876543210."

# Search for a word
result = re.search("Purnima", text)

if result:
    print("Name found:", result.group())
else:
    print("Name not found.")

# Find all numbers in the text
numbers = re.findall(r"\d+", text)
print("Numbers found:", numbers)

# Check phone number format
phone = "9876543210"

if re.fullmatch(r"\d{10}", phone):
    print("Valid phone number.")
else:
    print("Invalid phone number.")