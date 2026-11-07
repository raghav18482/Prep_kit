# Multilevel inheritance: Animal -> Dog -> GermanShepherd.


class Animal:
    def __init__(self):
        self.age = 0
        self.weight = 0
        print("I am base class")

    def speak(self):
        print("Speaking")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("I am dog")


class GermanShepherd(Dog):
    def __init__(self):
        super().__init__()
        print("I am german dog")


g = GermanShepherd()
g.speak()
print([cls.__name__ for cls in GermanShepherd.__mro__])  # lookup order
