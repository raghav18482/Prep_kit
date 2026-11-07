# Python is neither pure call-by-value nor call-by-reference: it is "call by object reference"
# (call by sharing). The function gets a reference to the same object.
#  - Rebinding the parameter (a = ...) never affects the caller.
#  - Mutating a mutable object (list.append) IS visible to the caller.


def swap(a, b):           # like C++ call by value: only local names are swapped
    a, b = b, a
    print("inside swap a =", a, "b =", b)


def swap_list(pair):      # like C++ call by reference: mutate the shared object
    pair[0], pair[1] = pair[1], pair[0]


def rebind(lst):
    lst = [100]           # new local object; caller's list untouched


a, b = 2, 3
swap(a, b)
print("After swap (value-like) a =", a, "b =", b)        # 2 3

pair = [2, 3]
swap_list(pair)
print("After swap_list (reference-like) pair =", pair)  # [3, 2]

nums = [1, 2]
rebind(nums)
print("After rebind nums =", nums)                      # [1, 2]

# Idiomatic Python: return new values instead of mutating
a, b = b, a
print("Pythonic swap a =", a, "b =", b)                 # 3 2
print("id shows same object passed:", id(nums) == id((lambda x: x)(nums)))
