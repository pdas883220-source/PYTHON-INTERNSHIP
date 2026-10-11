class Dog:
    def sound(self):
        print("Dog barks: Woof Woof!")


class Cat:
    def sound(self):
        print("Cat meows: Meow Meow!")


class Cow:
    def sound(self):
        print("Cow moos: Moo Moo!")


# Create objects
dog = Dog()
cat = Cat()
cow = Cow()

# Same method, different behavior
dog.sound()
cat.sound()
cow.sound()