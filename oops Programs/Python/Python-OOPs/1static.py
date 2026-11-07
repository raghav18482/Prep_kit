# Class variable = C++ static data member: one copy shared by all objects.
# No separate definition (int Student::count = 0) is needed in Python.


class Student:
    count = 0                      # class (static) variable

    def __init__(self):
        Student.count += 1         # update through the CLASS, not self

    def total(self):
        print("total students:", Student.count)


s1 = Student()
s2 = Student()
s2.total()                         # 2
print(Student.count, s1.count)     # readable via class or instance

# Gotcha: assigning through self creates an INSTANCE variable that shadows the class one
s1.count = 99
print("s1.count =", s1.count, "Student.count =", Student.count)

# Python has no void pointers: every name can refer to any object (dynamic typing)
ptr = "text"
ptr = 42
print("ptr now holds", type(ptr).__name__)
