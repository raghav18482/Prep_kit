# Encapsulation. Python has no private keyword:
#   _name   -> "protected" by convention
#   __name  -> name-mangled to _Class__name ("private")
# Pythonic getters/setters use @property.


class Student:
    count = 0

    def __init__(self):
        self.__rollno = 0            # private
        self._name = ""              # protected by convention
        Student.count += 1

    # Java/C++ style
    def get_rollno(self):
        return self.__rollno

    def set_rollno(self, x):
        if x <= 0:
            raise ValueError("rollno must be positive")
        self.__rollno = x

    # Pythonic style: attribute syntax, method behaviour
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("name cannot be empty")
        self._name = value.title()


s1 = Student()
s1.set_rollno(12)
print(s1.get_rollno())
s1.name = "raghav"                   # calls the setter
print(s1.name)
try:
    s1.name = ""
except ValueError as e:
    print("ValueError:", e)
try:
    print(s1.__rollno)
except AttributeError as e:
    print("AttributeError:", e)
print("mangled access still possible:", s1._Student__rollno)
print("count:", Student.count)
