# Abstract class: inherit from ABC and mark methods with @abstractmethod
# (like C++ pure virtual "= 0"). It cannot be instantiated.
from abc import ABC, abstractmethod


class Base(ABC):
    def __init__(self):
        self._x = 0
        print("i am abstract class")

    @abstractmethod
    def fun(self):
        ...

    def get_x(self):                 # concrete method is allowed
        return self._x


class Derived(Base):
    def fun(self):
        print("fun() called")


class Incomplete(Base):
    pass                             # does not implement fun


try:
    Base()
except TypeError as e:
    print("TypeError:", e)

d = Derived()
d.fun()
print(d.get_x())

try:
    Incomplete()
except TypeError as e:
    print("TypeError:", e)
