# Operator overloading via "dunder" (double underscore) methods.


class Complex:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def __add__(self, other):          # c1 + c2
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):          # c1 - c2
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):          # (a+bi)(c+di)
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __eq__(self, other):           # c1 == c2
        return isinstance(other, Complex) and (self.real, self.imag) == (other.real, other.imag)

    def __str__(self):                 # print(c)
        return f"{self.real} + i{self.imag}"

    def __repr__(self):
        return f"Complex({self.real}, {self.imag})"


c1, c2 = Complex(10, 5), Complex(2, 4)
c3 = c1 + c2
print(c3)                              # 12 + i9
print(c1 - c2, "|", c1 * c2)
print(c1 == Complex(10, 5))
print(repr(c3))


class Vector:                          # other common dunders
    def __init__(self, *items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, i):
        return self.items[i]

    def __lt__(self, other):
        return len(self) < len(other)


v = Vector(1, 2, 3)
print(len(v), v[0], Vector(1) < v)
