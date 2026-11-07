# Hierarchical inheritance: several children share one parent.


class A:
    def __init__(self):
        print("I am base class")

    def func1(self):
        print("Inside Function 1")


class B(A):
    def __init__(self):
        super().__init__()
        print("I am B")

    def func2(self):
        print("Inside Function 2")


class C(A):
    def __init__(self):
        super().__init__()
        print("I am C")

    def func3(self):
        print("Inside Function 3")


object1 = A()
object1.func1()

object2 = B()
object2.func1()
object2.func2()

object3 = C()
object3.func1()
object3.func3()
print(A.__subclasses__())
