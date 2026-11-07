# Same program as 19Exception.cpp. Full coverage lives in ../Errors-Exceptions/.
import sys


def divide(a, b):
    print("a/b = ", end="")
    if b == 0:
        raise ZeroDivisionError("value is Undefined")   # throw
    return a / b


print("before try")
a = 10
# input() would block when run non-interactively; use argv or a default
b = int(sys.argv[1]) if len(sys.argv) > 1 else 0
try:                                                    # try
    print(divide(a, b))
except ZeroDivisionError as e:                          # catch
    print(e)
finally:
    print("done")

# try    : block that may raise an exception
# except : handles a specific exception type
# raise  : throws an exception (like C++ throw)
# finally: always runs (no direct C++ equivalent; C++ uses RAII)
