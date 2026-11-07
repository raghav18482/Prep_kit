# Common built-in exceptions: what triggers each one.
# Syntax errors (SyntaxError, IndentationError) happen at compile time, so they are
# shown with compile(); everything else is a runtime exception.
#
# Hierarchy (simplified):
# BaseException
#  ├── SystemExit, KeyboardInterrupt, GeneratorExit   <- do not catch these casually
#  └── Exception
#       ├── ArithmeticError -> ZeroDivisionError, OverflowError
#       ├── LookupError     -> IndexError, KeyError
#       ├── ValueError, TypeError, NameError, AttributeError
#       ├── OSError         -> FileNotFoundError, PermissionError
#       ├── ImportError     -> ModuleNotFoundError
#       ├── RuntimeError    -> RecursionError, NotImplementedError
#       └── StopIteration, AssertionError, ...

examples = [
    ("ZeroDivisionError", lambda: 1 / 0),
    ("ValueError", lambda: int("abc")),
    ("TypeError", lambda: "1" + 1),
    ("IndexError", lambda: [1, 2][5]),
    ("KeyError", lambda: {"a": 1}["b"]),
    ("NameError", lambda: undefined_name),          # noqa: F821
    ("AttributeError", lambda: None.upper()),
    ("FileNotFoundError", lambda: open("does_not_exist.txt")),
    ("ModuleNotFoundError", lambda: __import__("no_such_module")),
    ("StopIteration", lambda: next(iter([]))),
    ("OverflowError", lambda: 10.0 ** 1000),
    ("RecursionError", lambda: (f := lambda: f())()),
    ("UnicodeDecodeError", lambda: b"\xff".decode("utf-8")),
]

for expected, fn in examples:
    try:
        fn()
    except Exception as e:
        status = "ok" if type(e).__name__ == expected else "UNEXPECTED"
        print(f"{type(e).__name__:<20} {status:<4} {e}")

for code in ("x = (1, 2", "if True:\nprint('x')"):
    try:
        compile(code, "<demo>", "exec")
    except SyntaxError as e:                        # IndentationError is a subclass
        print(f"{type(e).__name__:<20} line {e.lineno}: {e.msg}")

# Catching a parent class catches all of its children
try:
    [][0]
except LookupError as e:
    print("LookupError caught", type(e).__name__)
print(issubclass(KeyError, LookupError), issubclass(ZeroDivisionError, ArithmeticError))
print([c.__name__ for c in FileNotFoundError.__mro__])
