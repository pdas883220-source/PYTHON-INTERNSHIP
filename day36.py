# Day 36 - Python Decorators

# Creating a decorator
def my_decorator(function):

    def wrapper():
        print("Before calling the function.")

        function()

        print("After calling the function.")

    return wrapper


# Applying the decorator
@my_decorator
def greet():
    print("Hello! Welcome to Python Programming.")


# Calling the function
greet()


# Another example
def message_decorator(function):

    def wrapper(name):
        print("Starting the program...")
        function(name)
        print("Program completed.")

    return wrapper


@message_decorator
def welcome(name):
    print("Welcome", name)


welcome("Purnima")