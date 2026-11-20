"""
Python syntax walkthrough for interviews.
Run:  python3 "oops Programs/Python/syntax.py"

Read top to bottom. Each section is a function that prints its own output;
main() at the bottom runs them in learning order:

    1. Basics (comments, variables, casting, operators)
    2. Control flow (if / loops)
    3. Functions and modules
    4. Strings
    5. Lists
    6. Tuples
    7. Dictionaries
    8. Sets
    9. Arrays (array module + NumPy note)
   10. Comprehensions, iterators, generators
   11. Decorators and context managers
   12. Exceptions        (full coverage: Errors-Exceptions/)
   13. Classes           (full coverage: Python-OOPs/ and lld_python_prep/)
   14. Typing, builtins, standard library one-liners
   15. Interview gotchas
"""
from __future__ import annotations  # so list[int] / X | None annotations parse on 3.9


def header(title: str) -> None:
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# =============================================================================
# 1. BASICS: COMMENTS, DOCSTRINGS, INDENTATION, VARIABLES, CASTING, OPERATORS
# =============================================================================
def section_basics() -> None:
    """Docstring: first string in a module/function/class. Read it with help()."""
    header("1. BASICS")
    # Single-line comment. Indentation (4 spaces) defines blocks; there are no braces.
    print("docstring:", section_basics.__doc__.split(".")[0])

    # --- identifiers & variables ---
    # Letters, digits, underscore; cannot start with a digit; case-sensitive.
    # snake_case for vars/functions, PascalCase for classes, UPPER_CASE for constants.
    PI = 3.14
    name = "Raghav"          # str
    age = 20                 # int
    score = 99.5             # float
    can_vote = True          # bool  (True / False / None are capitalised)
    nothing = None           # absence of a value
    print(PI, name, age, score, can_vote, nothing)
    age = "twenty"           # legal: type is bound at runtime (dynamic typing)
    print("age is now", type(age).__name__)

    a, b = 1, 2              # multiple assignment
    a, b = b, a              # swap without a temp
    x = y = z = 0            # chained assignment
    print("swapped:", a, b, "| chained:", x, y, z)

    # --- type conversion / casting ---
    print(float(-25), int("7"), str(7), bool(0), bool("x"))  # -25.0 7 7 False True
    print(int(3.99), round(3.5), round(2.5))                  # 3 4 2 (banker's rounding)
    print(list("ab"), tuple([1, 2]), set([1, 1, 2]))
    print(int("11", 2), int("ff", 16), bin(5), hex(255))      # 3 255 0b101 0xff
    print(ord("A"), chr(65))                                  # 65 A
    print(bytes("hi", "utf-8"), b"hi".decode())               # b'hi' hi
    print(type(10), isinstance(10, int), isinstance(True, int))  # bool is a subclass of int

    # --- operators ---
    print(7 / 2, 7 // 2, 7 % 2, 2 ** 10)       # 3.5 3 1 1024
    print(-7 // 2, -7 % 2)                     # -4 1  (floor division rounds down)
    print(True and False, True or False, not True)
    print(0 or "default", "" and "never")      # and/or return an operand, not just bool
    print(1 < 2 < 3)                           # chained comparison
    print(5 & 3, 5 | 3, 5 ^ 3, ~5, 1 << 3, 16 >> 2)  # bitwise: 1 7 6 -6 8 4
    print([1, 2] + [3], [0] * 3)               # concat / repeat
    n = 10
    n += 5; n -= 3; n *= 2; n //= 4            # augmented assignment (no ++ / --)
    print("n =", n)                            # 6
    print([] is not None, 1 == 1.0)            # `is` = identity, `==` = value
    if (length := len("hello")) > 3:           # walrus: assign inside an expression (3.8+)
        print("len", length)


# =============================================================================
# 2. CONTROL FLOW: CONDITIONALS AND LOOPS
# =============================================================================
def section_control_flow() -> None:
    header("2. CONTROL FLOW")
    n = 7
    if n > 10:
        grade = "high"
    elif n > 5:
        grade = "mid"
    else:
        grade = "low"
    msg = "even" if n % 2 == 0 else "odd"      # ternary
    print(grade, msg)
    # Falsy values: 0, 0.0, "", [], {}, set(), None, False. Everything else is truthy.
    print([bool(v) for v in (0, "", [], None, "0", [0])])

    status = 404
    if status == 200:
        kind = "ok"
    elif status in (404, 403):
        kind = "client"
    else:
        kind = "other"
    print("status kind:", kind)
    # Python 3.10+ equivalent (this file targets 3.9, so it stays a comment):
    # match status:
    #     case 200: kind = "ok"
    #     case 404 | 403: kind = "client"
    #     case _: kind = "other"

    print(list(range(3)), list(range(1, 10, 3)), list(range(5, 0, -2)))  # [0,1,2] [1,4,7] [5,3,1]
    for i, color in enumerate(["r", "g"], start=1):
        print(i, color, end="  ")
    print()
    for k, v in zip([1, 2], ["a", "b"]):
        print(k, v, end="  ")
    print()

    i = 0
    while i < 5:
        i += 1
        if i == 2:
            continue                           # skip rest of this iteration
        if i == 4:
            break                              # leave loop
        print("while i =", i)
    else:
        print("never printed: else runs only if the loop did NOT break")

    for x in [1, 3, 5]:
        if x % 2 == 0:
            print("found even")
            break
    else:
        print("for-else: no even number found")

    for leaked in range(2):
        pass                                   # `pass` = empty block placeholder
    print("loop variable leaks to enclosing scope: leaked =", leaked)


# =============================================================================
# 3. FUNCTIONS AND MODULES
# =============================================================================
counter = 0                                    # module-level (global) variable


def add(x: int, y: int = 0) -> int:            # type hints are optional and not enforced
    """Return x + y."""
    return x + y


def append_to(item, bucket: list | None = None) -> list:
    if bucket is None:                         # never use [] / {} as a default: shared across calls
        bucket = []
    bucket.append(item)
    return bucket


def f(pos_only, /, either, *, kw_only=1):      # before / : positional only; after * : keyword only
    return pos_only, either, kw_only


def variadic(*args, **kwargs):                 # extras: args is a tuple, kwargs is a dict
    return args, kwargs


def min_max(nums):
    return min(nums), max(nums)                # "multiple return values" = one tuple


def factorial(n: int) -> int:                  # recursion (default limit about 1000 frames)
    return 1 if n <= 1 else n * factorial(n - 1)


def make_counter():
    n = 0

    def inc():                                 # closure: remembers n
        nonlocal n                             # rebind the enclosing function's variable
        n += 1
        return n

    return inc


def bump_global():
    global counter                             # rebind a module-level variable
    counter += 1


def section_functions_and_modules() -> None:
    header("3. FUNCTIONS AND MODULES")
    print(add(2), add(2, 3), add(y=1, x=4))    # positional, default, keyword args
    print(add.__doc__, add.__annotations__)
    print(append_to(1), append_to(2))          # [1] [2]  (fresh list each call)
    print(f(1, 2, kw_only=3), f(1, either=2))
    print(variadic(1, 2, a=3))                 # ((1, 2), {'a': 3})
    print(add(*[1, 2]), add(**{"x": 1, "y": 2}))  # unpack into arguments
    lo, hi = min_max([4, 1, 9])
    print("min/max:", lo, hi, "| 5! =", factorial(5))

    c = make_counter()
    c(); c()
    print("closure counter:", c())             # 3
    bump_global(); bump_global()
    print("global counter:", counter)          # 2

    # Scope lookup order: LEGB = Local -> Enclosing -> Global -> Built-in

    square = lambda x: x * x                   # lambda: anonymous single-expression function
    print(square(4))
    print(sorted([("b", 2), ("a", 1)], key=lambda p: p[1]))
    print(list(map(lambda x: x * 2, [1, 2, 3])))
    print(list(filter(lambda x: x > 1, [1, 2, 3])))
    print("functions are objects:", [fn.__name__ for fn in (add, factorial)])

    # --- modules ---
    # A module is a .py file; a package is a folder of modules (often with __init__.py).
    import math                                # import the whole module
    from math import sqrt as root              # import one name, with an alias
    from package import cal                    # package/cal.py next to this file
    print(math.pi, root(16), math.factorial(5), math.gcd(12, 18), math.ceil(2.1))
    print(cal.add(1, 2), cal.sub(1, 2), cal.mul(1, 2), cal.div(1, 2))
    import random
    random.seed(0)                             # reproducible output
    print(random.randint(1, 6), random.choice("abc"))
    print("this file's __name__ is", repr(__name__))   # "__main__" when run directly
    print("names in cal:", [n for n in dir(cal) if not n.startswith("_")])
    # import sys; sys.path lists where Python searches for modules.
    # `if __name__ == "__main__":` keeps demo code from running on import.


# =============================================================================
# 4. STRINGS — immutable sequences of Unicode characters
# =============================================================================
def section_strings() -> None:
    header("4. STRINGS")
    s1, s2 = 'single', "double"
    print(s1, s2)
    print('He said, "I want to eat an apple".')
    print("He said, \"I want to eat an apple\".")
    print("tab\tnewline->\nbackslash\\")            # escape sequences
    recipe = """1. Heat the pan
2. Crack the egg"""                                  # multiline string
    print(recipe)
    print(r"raw\npath")                              # raw: backslashes kept

    pie = "ApplePie"
    print(pie[0], pie[-1])                           # A e
    print(pie[:5], pie[5:], pie[2:6])                # Apple Pie pleP
    print(pie[::2], pie[::-1])                       # Apei eiPelppA
    print(len(pie), "Pie" in pie)                    # 8 True
    try:
        pie[0] = "a"                                 # immutable
    except TypeError as e:
        print("TypeError:", e)
    print("a" + pie[1:])                             # build a new string instead

    # Methods always return a NEW string
    print("Silver Spoon".replace("Sp", "M"))         # Silver Moon
    print("Silver Spoon".split(" "), "a,b,,c".split(","))
    print("  hi  ".strip() + "|", "xxhixx".strip("x"), "  hi".lstrip(), "hi  ".rstrip() + "|")
    print("-".join(["a", "b", "c"]))                 # a-b-c
    print("hello".capitalize(), "he's dan".title())  # Hello He'S Dan
    print("abc".upper(), "ABC".lower(), "Ab".swapcase())
    print("hello".find("ll"), "hello".find("z"))     # 2 -1
    print("hello".index("ll"))                       # 2 (ValueError if missing)
    print("aaaba".count("a"))                        # 4
    print("123".isdigit(), "ab".isalpha(), "a1".isalnum(), " ".isspace(), "Ab".islower())
    print("hello".startswith("he"), "hello".endswith("lo"))
    print("7".zfill(3), "hi".center(6, "*"), "hi".ljust(4, ".") + "|", "hi".rjust(4))
    print("key=value=x".partition("="), "a\nb".splitlines())

    who, n = "Raghav", 3
    print(f"{who} solved {n} problems")              # f-string (prefer this)
    print("{} solved {} problems".format(who, n))
    print("%s solved %d problems" % (who, n))        # old style
    print(f"{3.14159:.2f} {42:05d} {1234567:,} {0.25:.0%} {'x':>4}|")
    print(f"{n=}")                                   # n=3 (3.8+ debug format)

    print("apple" < "banana", "Z" < "a")             # lexicographic, by code point
    for ch in "abc":
        print(ch, end=" ")
    print()
    import string
    print(string.ascii_lowercase[:5], string.digits)
    words = "python is fun"
    print(" ".join(reversed(words.split())))         # fun is python
    word = "Level"
    print("palindrome:", word.lower() == word.lower()[::-1])
    print("héllo".encode("utf-8"), len("héllo"))


# =============================================================================
# 5. LISTS — ordered, mutable, allow duplicates and mixed types
# =============================================================================
def section_lists() -> None:
    header("5. LISTS")
    #            0        1       2        3        4
    colors = ["Red", "Green", "Blue", "Yellow", "Green"]
    #           -5       -4      -3       -2       -1
    print(colors[-1], colors[-3])                    # Green Blue
    mixed = [8, 2.3, [-4, 5], ["apple", "banana"]]
    print(mixed[2][1], len(mixed))                   # 5 4

    animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
    print(animals[3:7])                              # ['mouse', 'pig', 'horse', 'donkey']
    print(animals[-7:-2])                            # ['bat', 'mouse', 'pig', 'horse', 'donkey']
    print(animals[::2])                              # every 2nd from start
    print(animals[-8:-1:2])                          # every 2nd in a negative window

    colors.insert(1, "green")                        # O(n) — dynamic array (Python list), shifts elements
    colors.append("orange")                          # amortized O(1) — dynamic array (Python list)
    colors.extend(["pink", "black"])                 # O(k) — dynamic array (Python list), k items added
    print(colors)
    colors[1:4] = ["juan", "Anastasia"]              # slice assignment can change length
    print(colors)
    last = colors.pop()                              # remove + return last
    colors.pop(1)                                    # by index
    if "Yellow" in colors:
        colors.remove("Yellow")                      # first matching value (ValueError if missing)
    del colors[0]                                    # delete by index or slice
    print("popped", last, "->", colors)
    colors.clear()
    print("cleared:", colors)

    nums = [3, 1, 2]
    print(sorted(nums), sorted("cab"), nums)         # sorted() returns a NEW list
    nums.sort(reverse=True)                          # in place, returns None
    print(nums)
    nums.reverse()
    print(nums, nums.count(1), nums.index(3))
    print(sorted(["bb", "a", "ccc"], key=len))       # sort by a key function
    print(min(nums), max(nums), sum(nums), len(nums))

    stack = []                                       # list as a stack (LIFO)
    stack.append(1); stack.append(2)
    print("stack pop:", stack.pop())
    # For a queue use collections.deque (list.pop(0) is O(n)).

    # Shallow copy: creates a new outer collection, but keeps references to the same nested objects.
    # Deep copy: recursively copies nested objects, so the copy is independent of the original.
    copy1 = nums[:]                                  # shallow copies
    copy2 = nums.copy()
    print(copy1 == nums, copy1 is nums, copy2)
    nested = [[1], [2]]
    shallow = nested[:]
    shallow[0][0] = 99                               # inner lists are shared
    from copy import deepcopy
    deep = deepcopy(nested)
    deep[1][0] = -1
    print("nested:", nested, "deep:", deep)          # [[99], [2]] [[99], [-1]]

    bad_grid = [[0] * 3] * 2                         # 2 references to ONE row
    bad_grid[0][0] = 1
    good_grid = [[0] * 3 for _ in range(2)]          # independent rows
    good_grid[0][0] = 1
    print("bad:", bad_grid, "good:", good_grid)

    first, *middle, end = [1, 2, 3, 4]
    print(first, middle, end)                        # 1 [2, 3] 4


# =============================================================================
# 6. TUPLES — ordered, immutable, hashable if their items are
# =============================================================================
def section_tuples() -> None:
    header("6. TUPLES")
    t = (("parrot", "sparrow"), ("Lion", "Tiger"))
    print(t[1][0], len(t))                           # Lion 2
    one = (1,)                                       # trailing comma makes a 1-tuple
    not_tuple = (1)
    print(type(one).__name__, type(not_tuple).__name__)  # tuple int
    packed = 1, 2, 3                                 # parentheses optional (packing)
    print(packed, packed.count(2), packed.index(3))
    try:
        packed[0] = 9
    except TypeError as e:
        print("TypeError:", e)

    # "Modify": convert to list, change, convert back
    countries = ("Spain", "Italy", "India", "England", "Germany")
    temp = list(countries)
    temp.append("Russia")
    temp.pop(3)
    temp[2] = "Finland"
    countries = tuple(temp)
    print(countries)                                 # ('Spain', 'Italy', 'Finland', 'Germany', 'Russia')
    print(countries + ("Japan",), ("ha",) * 3)

    fauna = ("cat", "dog", "horse", "pig", "parrot", "salmon")
    (*mammals, bird, fish) = fauna                   # *name collects the rest into a list
    print(mammals, bird, fish)

    print((1, 2) < (1, 3), (2,) > (1, 99))           # compared element by element
    distances = {("Delhi", "Agra"): 233}             # tuples can be dict keys; lists cannot
    print(distances[("Delhi", "Agra")])

    from collections import namedtuple
    Point = namedtuple("Point", "x y")
    p = Point(1, 2)
    print(p, p.x, p[1], p._replace(x=5))


# =============================================================================
# 7. DICTIONARIES — key:value pairs, insertion-ordered (3.7+), unique hashable keys
# =============================================================================
def section_dictionaries() -> None:
    header("7. DICTIONARIES")
    info = {"name": "Karan", "age": 19, "eligible": True}
    print(info["name"])                              # KeyError if missing
    print(info.get("missing"), info.get("age", 0))   # None 19
    print(list(info.keys()), list(info.values()), list(info.items()))
    print("age" in info, len(info))                  # membership checks KEYS

    info["city"] = "Delhi"                           # insert / overwrite
    info.update({"age": 20, "role": "SDE"})
    info.setdefault("name", "x")                     # keeps the existing value
    info.setdefault("team", "infra")                 # inserts when missing
    removed = info.pop("role")                       # remove key, return value
    last = info.popitem()                            # remove last inserted pair
    del info["eligible"]
    print(info, "| popped:", removed, last)
    print({**info, "extra": 1})                      # merge into a new dict (right wins)
    print(info | {"age": 21})                        # 3.9+ merge operator

    for k, v in info.items():
        print(f"  {k} -> {v}")
    for k in list(info):                             # iterate over a copy to delete safely
        if k == "city":
            del info[k]
    print(info)

    squares = {x: x * x for x in range(4)}           # dict comprehension
    print(squares)
    print(dict(zip(["a", "b"], [1, 2])), dict.fromkeys("ab", 0), dict(a=1))
    scores = {"amit": 72, "bina": 91, "chetan": 85}
    print(sorted(scores, key=scores.get, reverse=True))   # keys by value
    print(max(scores, key=scores.get))                    # bina
    print({v: k for k, v in scores.items()})              # invert

    nested = {"user": {"name": "R", "langs": ["py", "c++"]}}
    print(nested["user"]["langs"][1])

    from collections import Counter, defaultdict
    print(Counter("banana").most_common(2))          # [('a', 3), ('n', 2)]
    groups = defaultdict(list)                       # missing keys get a default
    for word in ["apple", "avocado", "banana"]:
        groups[word[0]].append(word)
    print(dict(groups))
    try:
        {[1]: "x"}
    except TypeError as e:
        print("TypeError:", e)                       # unhashable key


# =============================================================================
# 8. SETS — unordered, unique items, mutable (frozenset is immutable)
# =============================================================================
def section_sets() -> None:
    header("8. SETS")
    set1 = {4, -5, 8, 3, 2.9, 4}
    print(len(set1), 4 in set1)                      # 5 True (duplicate removed)
    empty_set = set()                                # {} is an empty DICT
    print(type(empty_set).__name__, type({}).__name__)
    a = {1, 2, 3, 4}
    b = {3, 4, 5}
    a.add(10)
    a.update({11, 12})
    a.discard(99)                                    # no error if missing
    a.remove(12)                                     # KeyError if missing
    print(sorted(a))
    print(a | b, a & b, a - b, a ^ b)                # union, intersection, difference, symmetric
    print({1, 2} <= a, a.isdisjoint({100}))          # subset, disjoint
    print(sorted(set("mississippi")))                # dedupe
    print(frozenset([1, 2]))                         # hashable, can be a dict key / set item


# =============================================================================
# 9. ARRAYS — the `array` module (typed, compact) and a NumPy note
# =============================================================================
def section_arrays() -> None:
    header("9. ARRAYS")
    from array import array
    # Python has no built-in fixed-type array; list is the default sequence.
    # array.array stores ONE C type compactly. Common type codes:
    #   'b' signed char  'i' int  'l' long  'f' float  'd' double  'u' unicode char
    arr = array("i", [10, 20, 30])
    print(arr, arr[0], arr[-1], len(arr))
    arr.append(40)
    arr.extend([50, 60])
    arr.insert(1, 15)
    print(arr.tolist())                              # [10, 15, 20, 30, 40, 50, 60]
    print(arr.pop(), arr.pop(0))                     # 60 10
    arr.remove(30)                                   # first occurrence
    print(arr.index(40), arr.count(20), arr.tolist())
    arr.reverse()
    print(arr[1:3], arr[::-1].tolist())              # slicing returns an array
    arr[0] = 99
    for x in arr:
        print(x, end=" ")
    print()
    print("typecode:", arr.typecode, "| itemsize:", arr.itemsize, "bytes")
    try:
        arr.append(1.5)                              # type is enforced
    except TypeError as e:
        print("TypeError:", e)
    doubles = array("d", [1.5, 2.5])
    raw = doubles.tobytes()
    print(len(raw), array("d", raw))                 # 16 array('d', [1.5, 2.5])

    import sys
    nums_list = list(range(1000))
    nums_arr = array("i", nums_list)
    print("list bytes ~", sys.getsizeof(nums_list) + sum(sys.getsizeof(n) for n in nums_list),
    "| array bytes ~", sys.getsizeof(nums_arr))

    # NumPy (third-party: pip install numpy) is what people usually mean by
    # "arrays" in data/ML work: n-dimensional, vectorised maths, broadcasting.
    try:
        import numpy as np
    except ImportError:
        print("NumPy not installed; example:  np.array([1, 2, 3]) * 2 -> [2 4 6]")
    else:
        v = np.array([1, 2, 3])
        m = np.arange(6).reshape(2, 3)
        print(v * 2, v.sum(), v.dtype, m.shape, m.T.tolist(), m[:, 1])


# =============================================================================
# 10. COMPREHENSIONS, ITERATORS, GENERATORS
# =============================================================================
def countdown(n):
    while n:
        yield n                                      # generator: lazy, one value at a time
        n -= 1


def section_iteration() -> None:
    header("10. COMPREHENSIONS, ITERATORS, GENERATORS")
    print([x * x for x in range(5) if x % 2 == 0])   # list
    print({x % 3 for x in range(10)})                # set
    print({x: x * x for x in range(3)})              # dict
    print(tuple(x for x in range(3)))                # generator -> tuple
    print([[i * j for j in range(3)] for i in range(2)])
    print(["even" if x % 2 == 0 else "odd" for x in range(3)])
    print([y for row in [[1, 2], [3]] for y in row]) # flatten

    it = iter([10, 20])
    print(next(it), next(it), next(it, "done"))      # default instead of StopIteration
    print(list(countdown(3)))                        # [3, 2, 1]
    gen = (x * x for x in range(4))
    print(sum(gen), sum(gen))                        # 14 0  (generators are single-use)


# =============================================================================
# 11. DECORATORS AND CONTEXT MANAGERS
# =============================================================================
def logged(fn):
    import functools

    @functools.wraps(fn)                             # keep fn's name/docstring
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f"{fn.__name__}{args} -> {result}")
        return result

    return wrapper


@logged
def double(n):
    return n * 2


def section_decorators_and_context() -> None:
    header("11. DECORATORS AND CONTEXT MANAGERS")
    double(21)
    print("name preserved:", double.__name__)

    from contextlib import contextmanager

    @contextmanager
    def tag(name):
        print(f"<{name}>")
        yield
        print(f"</{name}>")

    with tag("ok"):
        print("inside")

    import os
    import tempfile
    path = os.path.join(tempfile.gettempdir(), "syntax_demo.txt")
    with open(path, "w", encoding="utf-8") as fh:    # file closed automatically
        fh.write("line1\nline2\n")
    with open(path, encoding="utf-8") as fh:
        print(fh.read().splitlines())                # also .readline() / .readlines() / for line in fh
    os.remove(path)


# =============================================================================
# 12. EXCEPTIONS — summary; see Errors-Exceptions/ for the full set
# =============================================================================
class AppError(Exception):
    pass


def section_exceptions() -> None:
    header("12. EXCEPTIONS")
    try:
        1 / 0
    except ZeroDivisionError as e:
        print("caught", type(e).__name__, "-", e)
    except (TypeError, ValueError):
        print("not reached")
    else:
        print("only if try succeeded")
    finally:
        print("always")
    try:
        try:
            int("x")
        except ValueError as e:
            raise AppError("bad input") from e       # exception chaining
    except AppError as e:
        print(repr(e), "caused by", repr(e.__cause__))


# =============================================================================
# 13. CLASSES — syntax only; see Python-OOPs/ and lld_python_prep/principles/
# =============================================================================
class Animal:
    species = "unknown"                              # class attribute (shared)

    def __init__(self, name: str) -> None:
        self.name = name                             # instance attribute

    def speak(self) -> str:                          # instance method: first arg is self
        return "..."

    @classmethod
    def from_upper(cls, name: str) -> Animal:
        return cls(name.title())

    @staticmethod
    def ping() -> str:
        return "pong"

    def __repr__(self) -> str:                       # unambiguous, for debugging
        return f"Animal({self.name!r})"

    def __str__(self) -> str:                        # readable, for users
        return self.name

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Animal) and self.name == other.name

    def __hash__(self) -> int:                       # define with __eq__ to use in sets/dicts
        return hash(self.name)


class Dog(Animal):
    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name)
        self.breed = breed

    def speak(self) -> str:                          # override
        return f"{self.name}: woof"


def section_classes() -> None:
    header("13. CLASSES")
    from dataclasses import dataclass, field

    @dataclass
    class User:                                      # __init__/__repr__/__eq__ generated
        name: str
        tags: list[str] = field(default_factory=list)

    a = Animal.from_upper("bruno")
    print(repr(a), str(a), Animal.ping(), Animal.species)
    print(Dog("bruno", "lab").speak(), Dog("x", "y") == Animal("x"))
    print(User("Raghav"), User("a") == User("a"))


# =============================================================================
# 14. TYPING, BUILTINS, STANDARD LIBRARY ONE-LINERS
# =============================================================================
def section_builtins() -> None:
    header("14. TYPING, BUILTINS, STDLIB")
    from typing import Iterable, Optional, TypeVar

    T = TypeVar("T")

    def first(xs: Iterable[T]) -> Optional[T]:      # 3.10+: T | None
        for x in xs:
            return x
        return None

    print(first([9, 8]), first([]))
    print(all([True, 1]), any([0, ""]))
    print(min([3, 1, 2]), max("abc"), sum([1, 2, 3], start=10))
    print(abs(-2), round(2.675, 2), pow(2, 5, 10))   # 2.67: floats are binary approximations
    print(divmod(7, 2), sorted({3, 1, 2}, reverse=True), list(reversed([1, 2, 3])))

    from collections import deque
    q = deque([1, 2])
    q.appendleft(0)
    q.append(3)
    print(q.popleft(), q.pop(), q)                   # 0 3 deque([1, 2])

    from functools import lru_cache, partial, reduce
    print(reduce(lambda acc, x: acc + x, [1, 2, 3], 0))

    @lru_cache(maxsize=None)                         # memoisation
    def fib(n: int) -> int:
        return n if n < 2 else fib(n - 1) + fib(n - 2)

    plus1 = partial(add, y=1)
    print(fib(30), plus1(4))

    from itertools import chain, combinations, groupby, islice, permutations, product
    print(list(islice(range(10), 2, 6)))             # [2, 3, 4, 5]
    print(list(combinations([1, 2, 3], 2)))
    print(len(list(permutations("abc"))), list(product("ab", repeat=2)))
    print(list(chain([1], [2, 3])))
    print([(k, len(list(g))) for k, g in groupby("aaabcc")])

    import heapq
    h = [5, 1, 4]
    heapq.heapify(h)                                 # min-heap
    heapq.heappush(h, 0)
    print(heapq.heappop(h), heapq.nsmallest(2, h))   # 0 [1, 4]
    import bisect
    sorted_nums = [1, 3, 5]
    bisect.insort(sorted_nums, 4)
    print(sorted_nums, bisect.bisect_left(sorted_nums, 4))


# =============================================================================
# 15. INTERVIEW GOTCHAS
# =============================================================================
def section_gotchas() -> None:
    header("15. GOTCHAS")
    funcs = [lambda: i for i in range(3)]
    print([fn() for fn in funcs])                    # [2, 2, 2]  late-binding closures
    funcs = [lambda i=i: i for i in range(3)]
    print([fn() for fn in funcs])                    # [0, 1, 2]
    import math
    nan = float("nan")
    print(nan == nan, math.isnan(nan))               # False True
    print(0.1 + 0.2 == 0.3, math.isclose(0.1 + 0.2, 0.3))   # False True
    print([3, 1].sort())                             # None: sort() is in place
    # 1. Mutable default args are shared across calls -> default to None (see append_to).
    # 2. `is` vs `==`: use `is` only for None / True / False / same-object checks.
    # 3. Shallow copy vs deepcopy for nested lists/dicts (see section 5).
    # 4. dict keeps insertion order; set order is arbitrary.
    # 5. Small ints/strings may be cached so `is` looks equal; never rely on it.
    # 6. `except Exception:` swallows bugs; catch specific types.
    # 7. str/tuple/frozenset are hashable; list/dict/set are not.
    # 8. Loop variables leak out of for loops (section 2).
    # 9. [[0] * n] * m shares one row (section 5).


def main() -> None:
    section_basics()
    section_control_flow()
    section_functions_and_modules()
    section_strings()
    section_lists()
    section_tuples()
    section_dictionaries()
    section_sets()
    section_arrays()
    section_iteration()
    section_decorators_and_context()
    section_exceptions()
    section_classes()
    section_builtins()
    section_gotchas()


if __name__ == "__main__":
    main()
