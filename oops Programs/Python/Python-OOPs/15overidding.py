# Method overriding = runtime polymorphism. The child redefines a parent method;
# super() lets the child also call the parent's version.


class A:
    def __init__(self):
        print("constructor of parent")

    def print(self):
        print("i am base class")


class B(A):
    def __init__(self):
        super().__init__()
        print("constructor of child")

    def print(self):                 # overrides A.print
        print("i am derived class")

    def print_both(self):
        super().print()
        self.print()


a = A()
b = B()
a.print()
b.print()
b.print_both()

for obj in (A(), B()):               # same call, different behaviour
    obj.print()
