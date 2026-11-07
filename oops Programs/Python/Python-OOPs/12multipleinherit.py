# Multiple inheritance. When both parents define walk(), Python picks the first
# class in the MRO (Method Resolution Order, C3 linearisation). No ambiguity error
# like C++; call a specific parent with ClassName.method(self).


class Animal:
    def __init__(self):
        print("I am Animal class")

    def bark(self):
        print("Barking")

    def walk(self):
        print("Animal is walking")


class Human:
    def __init__(self):
        print("I am Human")

    def speak(self):
        print("Speaking")

    def walk(self):
        print("human is walking")


class Hybrid(Animal, Human):
    def __init__(self):
        Animal.__init__(self)        # explicit: both parents' constructors
        Human.__init__(self)
        print("I am human and animal")


obj1 = Hybrid()
obj1.speak()
obj1.bark()
obj1.walk()                          # Animal.walk (Animal is first in MRO)
Human.walk(obj1)                     # like obj1.Human::walk() in C++
print([c.__name__ for c in Hybrid.__mro__])


# Diamond problem: super() follows the MRO so the shared base runs once
class Base:
    def __init__(self):
        print("Base")


class Left(Base):
    def __init__(self):
        print("Left")
        super().__init__()


class Right(Base):
    def __init__(self):
        print("Right")
        super().__init__()


class Diamond(Left, Right):
    def __init__(self):
        print("Diamond")
        super().__init__()


Diamond()                            # Diamond Left Right Base
