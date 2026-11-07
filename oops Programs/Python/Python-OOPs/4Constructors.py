# Python has ONE constructor: __init__ (with __new__ doing allocation).
# Default + parameterised constructors -> default arguments.
# Copy constructor -> a classmethod/explicit copy, or the copy module.
import copy


class Go:
    def __init__(self, x=None):           # default and parameterised in one
        if x is None:
            print("default constructor is called")
            self.x = 0
        else:
            self.x = x
            print("parameterised constructor, id(self) =", id(self))  # self ~ this

    @classmethod
    def copy_of(cls, other):              # "copy constructor"
        return cls(other.x)

    def print(self):
        print("x =", self.x)


a0 = Go()
a1 = Go(20)
a2 = Go.copy_of(a1)
a3 = copy.copy(a1)                        # stdlib shallow copy, does not call __init__
print(a2.x, a3.x)
print("a1 is a2:", a1 is a2)
a1.print()


class Point:
    def __new__(cls, *args):              # allocates the object (rarely overridden)
        print("__new__ creates the instance")
        return super().__new__(cls)

    def __init__(self, x, y):             # initialises it
        print("__init__ initialises it")
        self.x, self.y = x, y


p = Point(1, 2)
print(p.x, p.y)
