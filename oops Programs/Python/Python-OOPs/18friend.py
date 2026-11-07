# Python has no friend functions/classes: there is no enforced access control.
# A module-level function can read any attribute; underscores are just conventions.
# The closest idea: functions in the same module that are allowed to touch _private state.


class Student:
    def __init__(self):
        self.__usn = 0                # name-mangled "private"


def write(s, usn):                    # "friend" helper: uses the mangled name
    s._Student__usn = usn
    print("write usn", usn)


def iknow(s):
    return s._Student__usn


s = Student()
write(s, 101)                         # C++ used cin; fixed value keeps this runnable
print(iknow(s))
print(vars(s))                        # everything is inspectable
