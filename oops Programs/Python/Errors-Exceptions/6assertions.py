# assert condition, "message"  -> raises AssertionError if condition is False.
# Use asserts for internal invariants and tests, NOT for validating user input:
# `python3 -O file.py` strips all assert statements.


def average(nums):
    assert len(nums) > 0, "nums must not be empty"
    return sum(nums) / len(nums)


print(average([2, 4, 6]))
try:
    average([])
except AssertionError as e:
    print("AssertionError:", e)
except ZeroDivisionError:                # what actually happens under -O: assert was removed
    print("ZeroDivisionError: the assert was stripped by -O")


def binary_search(arr, target):
    assert arr == sorted(arr), "input must be sorted"   # precondition
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


print(binary_search([1, 3, 5, 7], 5))
try:
    print("unsorted search ->", binary_search([3, 1, 2], 1))   # wrong answer under -O
except AssertionError as e:
    print("AssertionError:", e)

# Simple test-style checks
assert binary_search([1, 2, 3], 3) == 2
assert binary_search([], 1) == -1
print("all asserts passed" if __debug__ else "asserts skipped (-O)")

# Gotcha: a tuple is always truthy, so this assert can never fail
#   assert (1 == 2, "message")     # SyntaxWarning in recent Pythons
print("asserts enabled:", __debug__)   # False when run with -O

# Input validation should raise a real exception instead
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age


try:
    set_age(-1)
except ValueError as e:
    print("ValueError:", e)
