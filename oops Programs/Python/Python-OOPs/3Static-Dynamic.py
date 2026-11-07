# C++ has stack (static) and heap (new/delete) objects.
# In Python EVERY object lives on the heap; names are just references.
# Memory is freed automatically by reference counting + the garbage collector.
import sys


class Student:
    def __init__(self):
        self.name = ""


s1 = Student()            # "Student s1;" and "new Student" are the same thing in Python
s1.name = "Raghav"
print(s1.name)

s2 = s1                   # copies the reference, not the object
s2.name = "Swami"
print(s1.name, "| same object:", s1 is s2)

print("refcount:", sys.getrefcount(s1) - 1)   # -1 for getrefcount's own argument
del s2                    # removes a NAME, not the object (like dropping one pointer)
print("refcount after del s2:", sys.getrefcount(s1) - 1)

arr = [0] * 10            # like new int[10]; no delete[] needed
print(arr)
del arr                   # object freed once no references remain
