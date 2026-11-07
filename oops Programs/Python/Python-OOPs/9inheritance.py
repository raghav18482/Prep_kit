# Single inheritance. super().__init__() runs the parent constructor
# (Python does NOT call it automatically, unlike C++).
# Python has no public/protected/private inheritance; everything is inherited.


class Human:
    def __init__(self):
        self.height = 170       # instance variables
        self.weight = 60
        self.age = 0
        print("i am base class")

    def get_age(self):
        return self.age

    def set_weight(self, w):    # w is a local variable
        self.weight = w


class Male(Human):
    def __init__(self, age):
        super().__init__()      # call base constructor explicitly
        self.age = age
        self.color = "brown"
        print("i am child class")

    def sleep(self):
        print("Male Sleeping")

    def get_height(self):
        return self.height


m = Male(18)
print(m.age, m.weight, m.get_height())
m.set_weight(84)
print(m.weight)
m.sleep()
print(isinstance(m, Human), issubclass(Male, Human))
