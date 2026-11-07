# Deep copy: nested objects are copied too, so the copy is fully independent.
import copy


class Go:
    def __init__(self, name):
        self.x = list(name)              # mutable inner object (like char* buffer)

    def __deepcopy__(self, memo):        # optional: custom deep copy (like a copy constructor)
        new = Go("")
        new.x = copy.deepcopy(self.x, memo)
        return new

    def print(self):
        print("".join(self.x))


a1 = Go("Raghav")
a2 = copy.deepcopy(a1)
a1.x[0] = "G"
a1.print()                               # Gaghav
a2.print()                               # Raghav  (independent)
print("inner list shared?", a1.x is a2.x)
