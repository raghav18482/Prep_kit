# Shallow copy: a new outer object, but inner (mutable) objects are SHARED.
import copy


class Go:
    def __init__(self, name):
        self.x = list(name)              # mutable attribute -> source of shallow-copy bugs

    def print(self):
        print("".join(self.x))


a1 = Go("Raghav")
a2 = copy.copy(a1)
a1.x[0] = "G"
a1.print()                               # Gaghav
a2.print()                               # Gaghav  (same inner list)
print("a1 is a2:", a1 is a2, "| inner list shared:", a1.x is a2.x)

# Same with built-ins
nested = [[1, 2], [3]]
shallow = nested[:]                      # or list(nested) / nested.copy()
shallow[0].append(99)
print(nested)                            # [[1, 2, 99], [3]]
