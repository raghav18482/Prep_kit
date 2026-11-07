# __del__ is called when the object's reference count reaches zero (CPython).
# Timing is not guaranteed in general (cycles, other interpreters), so for cleanup
# of files/locks/connections prefer a context manager (with) instead.


class Test:
    def __init__(self, name):
        self.name = name
        print("Constructor executed", name)

    def __del__(self):
        print("Destructor executed", self.name)


def scope():
    t = Test("local")      # destroyed when the function returns (like a stack object)
    print("leaving scope")


scope()
t1 = Test("manual")
del t1                     # last reference gone -> destructor runs now
print("after del")


class Resource:            # deterministic cleanup
    def __enter__(self):
        print("acquire")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("release")


with Resource():
    print("using resource")
