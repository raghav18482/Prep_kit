# Python has NO compile-time method overloading: a second def with the same name
# replaces the first. Achieve the same with default args, *args, or singledispatch.
from functools import singledispatchmethod


class Area:
    def area(self, a, b=None):             # default argument "overload"
        return a * a if b is None else a * b


class AreaVar:
    def area(self, *sides):                # variable arguments
        if len(sides) == 1:
            return sides[0] ** 2
        if len(sides) == 2:
            return sides[0] * sides[1]
        raise TypeError("area() takes 1 or 2 sides")


class Printer:
    @singledispatchmethod                  # overload by type of first argument
    def show(self, arg):
        print("generic:", arg)

    @show.register
    def _(self, arg: int):
        print("int:", arg)

    @show.register
    def _(self, arg: list):
        print("list of", len(arg))


print(Area().area(4), Area().area(2, 3))     # 16 6
print(AreaVar().area(4), AreaVar().area(2, 3))
p = Printer()
p.show(5)
p.show([1, 2])
p.show("hi")


class Shadow:
    def f(self):
        return "first"

    def f(self, x):                        # replaces the first f
        return f"second {x}"


try:
    Shadow().f()
except TypeError as e:
    print("TypeError:", e)
