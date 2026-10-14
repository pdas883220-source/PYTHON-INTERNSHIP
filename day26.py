class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    else:
        print("Eligible to register!")


try:
    age = int(input("Enter your age: "))
    check_age(age)

except ValueError:
    print("Error: Please enter a valid number.")

except InvalidAgeError as error:
    print("Error:", error)

finally:
    print("Program execution completed.")