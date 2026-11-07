# @staticmethod: no self/cls, called on the class — like a C++ static function.
# @classmethod : receives the class (cls), can read/modify class state and act as a factory.


class Student:
    count = 0

    def __init__(self, name="anon"):
        self.name = name
        Student.count += 1

    @staticmethod
    def total():                       # no access to self (like no `this` in C++)
        print("total:", Student.count)

    @classmethod
    def reset(cls):
        cls.count = 0

    @classmethod
    def from_csv(cls, line):           # alternative constructor
        return cls(line.split(",")[0])


Student()
Student()
Student.total()                        # 2, no object needed
s = Student.from_csv("Raghav,21")
print(s.name)
Student.total()                        # 3
Student.reset()
Student.total()                        # 0
