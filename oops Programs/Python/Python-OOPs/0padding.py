# Python has no struct padding you control; every object is a heap object with a header.
# sys.getsizeof shows the object's own size (not what it references).
# __slots__ removes the per-instance __dict__ and is Python's closest "memory layout" knob.
import sys


class Student:
    def __init__(self):
        self.rollno = 1
        self.name = "R"
        self.school = 9.5


class SlotStudent:
    __slots__ = ("rollno", "name", "school")  # fixed attributes, no __dict__

    def __init__(self):
        self.rollno = 1
        self.name = "R"
        self.school = 9.5


s1 = Student()
s2 = SlotStudent()
normal_total = sys.getsizeof(s1) + sys.getsizeof(s1.__dict__)
print("normal object:", sys.getsizeof(s1), "+ __dict__", sys.getsizeof(s1.__dict__), "=", normal_total)
print("slots object :", sys.getsizeof(s2), "(no __dict__)")
print("slots saves  :", normal_total - sys.getsizeof(s2), "bytes per object")
print("has __dict__?", hasattr(s1, "__dict__"), hasattr(s2, "__dict__"))
try:
    s2.extra = 1  # cannot add attributes not listed in __slots__
except AttributeError as e:
    print("AttributeError:", e)

# Sizes vary by Python version/platform; the point is slots objects use less memory in total.
