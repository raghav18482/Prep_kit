# In Python every method is "virtual": lookup happens at runtime on the actual
# object's class (late binding). There is no early binding as in C++ non-virtual methods.
# Duck typing: any object with the right method works, no common base needed.


class Base:
    def show(self):
        print("I am base")

    def print(self):
        print("I am base print")


class Derived(Base):
    def show(self):
        print("I am derived with late binding")

    def print(self):
        print("I am derived print (still late binding)")


p: Base = Derived()        # type hint says Base; object is Derived
p.print()                  # Derived version (C++ would call Base without virtual)
p.show()


class Duck:
    def show(self):
        print("I am a duck, not a Base")


for obj in (Base(), Derived(), Duck()):
    obj.show()
