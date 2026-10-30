# Day 35 - Python *args and **kwargs

# Example 1: Using *args
def add_numbers(*args):
    total = 0

    for number in args:
        total += number

    print("Sum:", total)


add_numbers(10, 20, 30, 40)


# Example 2: Using **kwargs
def student_details(**kwargs):
    print("\nStudent Details:")

    for key, value in kwargs.items():
        print(key, ":", value)


student_details(
    name="Purnima",
    course="BCA",
    marks=85,
    college="Centurion University"
)


# Example 3: Using both
def display_info(*args, **kwargs):
    print("\nSubjects:", args)
    print("Other Information:", kwargs)


display_info("Python", "Java", name="Purnima", semester=3)