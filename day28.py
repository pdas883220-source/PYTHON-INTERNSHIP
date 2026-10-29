# Day 28 - Python Random Module

import random

# Generate a random number
number = random.randint(1, 100)
print("Random Number:", number)

# Select a random fruit
fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Random Fruit:", random.choice(fruits))

# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled List:", numbers)