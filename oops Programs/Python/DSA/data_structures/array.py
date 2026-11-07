# =====================================================================
#                    ARRAY / DYNAMIC ARRAY - REVISION NOTES
# =====================================================================
#
# WHAT IS AN ARRAY?
#   - A collection of elements stored in CONTIGUOUS memory locations.
#   - Every element is reached by its INDEX in O(1):
#         address(i) = base_address + i * size_of_element
#   - Static array: fixed size, decided at creation (C arrays).
#   - Dynamic array: grows automatically (Python list, Java ArrayList,
#     C++ vector).
#
# HOW A DYNAMIC ARRAY GROWS
#   - It keeps a hidden fixed-size array with some CAPACITY.
#   - When it is full, it allocates a bigger array (usually 2x), copies
#     every element across, then inserts the new element.
#   - A single resize costs O(n), but it happens rarely, so append is
#     O(1) AMORTIZED (averaged over many appends).
#     Total cost of n appends ~ n + (1 + 2 + 4 + ... + n) ~ 3n -> O(1) each.
#
# TIME COMPLEXITY
#   +-----------------------------+--------------------+
#   | Operation                   | Time               |
#   +-----------------------------+--------------------+
#   | Access arr[i]               | O(1)               |
#   | Update arr[i] = x           | O(1)               |
#   | Append at end               | O(1) amortized     |
#   | Pop from end                | O(1)               |
#   | Insert / delete at index i  | O(n) (shift items) |
#   | Insert / delete at front    | O(n)               |
#   | Search (unsorted)           | O(n)               |
#   | Search (sorted, binary)     | O(log n)           |
#   +-----------------------------+--------------------+
#   Space: O(n)
#
# PROS / CONS
#   + O(1) random access, cache friendly (contiguous memory).
#   - Inserting/deleting in the middle is slow (shifting).
#   - Resizing costs time, and spare capacity wastes some memory.
#
# PYTHON LIST CHEAT SHEET
#   arr.append(x)       O(1)   | arr.pop()        O(1)
#   arr.insert(i, x)    O(n)   | arr.pop(i)       O(n)
#   arr.remove(x)       O(n)   | x in arr         O(n)
#   arr[a:b]            O(b-a) | arr.sort()       O(n log n)  (Timsort, stable)
#   arr.reverse()       O(n)   | len(arr)         O(1)
#   2D list: [[0] * cols for _ in range(rows)]   (NOT [[0]*cols]*rows!)
#
# COMMON INTERVIEW PATTERNS
#   - Two pointers   : pair sum in a sorted array, reverse, remove dups.
#   - Sliding window : max sum subarray of size k, longest substring.
#   - Prefix sum     : range sum queries in O(1) after O(n) prep.
#   - Kadane's algo  : maximum subarray sum in O(n).
#   - Binary search  : on sorted arrays or on the answer space.
#   - Dutch national flag : sort 0s, 1s, 2s in one pass.
#   - Hashing        : two sum, frequency count.
#
# QUICK TIPS
#   - Negative indexing in Python: arr[-1] is the last element.
#   - Mutating a list while iterating over it causes bugs; iterate a copy.
# =====================================================================


class DynamicArray:
    """A simplified version of how Python's list works internally."""

    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._data = [None] * self._capacity

    def __len__(self):
        return self._size

    def __getitem__(self, i):
        if not 0 <= i < self._size:
            raise IndexError("index out of range")
        return self._data[i]

    def __setitem__(self, i, value):
        if not 0 <= i < self._size:
            raise IndexError("index out of range")
        self._data[i] = value

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)  # double when full
        self._data[self._size] = value
        self._size += 1

    def insert(self, index, value):
        if not 0 <= index <= self._size:
            raise IndexError("index out of range")
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        # shift elements right to make room
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def pop(self, index=None):
        if self._size == 0:
            raise IndexError("pop from empty array")
        if index is None:
            index = self._size - 1
        if not 0 <= index < self._size:
            raise IndexError("index out of range")
        value = self._data[index]
        # shift elements left to fill the gap
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        # shrink when only 1/4 full (avoids thrashing)
        if 0 < self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)
        return value

    def index_of(self, value):
        for i in range(self._size):
            if self._data[i] == value:
                return i
        return -1

    def __repr__(self):
        items = [self._data[i] for i in range(self._size)]
        return f"DynamicArray({items}, capacity={self._capacity})"


# ---------------- classic array algorithms ----------------
def binary_search(arr, target):
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


def kadane(arr):
    """Maximum subarray sum in O(n)."""
    best = cur = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


def prefix_sums(arr):
    """prefix[i] = sum of arr[0:i]; range sum (l..r) = prefix[r+1] - prefix[l]."""
    prefix = [0] * (len(arr) + 1)
    for i, x in enumerate(arr):
        prefix[i + 1] = prefix[i] + x
    return prefix


def two_sum_sorted(arr, target):
    """Two pointers on a sorted array."""
    l, r = 0, len(arr) - 1
    while l < r:
        s = arr[l] + arr[r]
        if s == target:
            return l, r
        if s < target:
            l += 1
        else:
            r -= 1
    return None


def max_sum_window(arr, k):
    """Sliding window: max sum of any k consecutive elements."""
    window = sum(arr[:k])
    best = window
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]
        best = max(best, window)
    return best


if __name__ == "__main__":
    print("----- Dynamic Array -----")
    da = DynamicArray()
    for x in [10, 20, 30, 40, 50]:
        da.append(x)
        print(da)
    da.insert(1, 15)
    print("after insert(1, 15):", da)
    print("pop():", da.pop(), "| pop(0):", da.pop(0), "->", da)
    print("index_of(30):", da.index_of(30))

    print("\n----- Algorithms -----")
    print("binary_search:", binary_search([1, 3, 5, 7, 9, 11], 7))
    print("kadane:", kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    p = prefix_sums([1, 2, 3, 4, 5])
    print("prefix sums:", p, "| sum(1..3) =", p[4] - p[1])
    print("two_sum_sorted:", two_sum_sorted([1, 2, 4, 7, 11, 15], 15))
    print("max_sum_window k=3:", max_sum_window([2, 1, 5, 1, 3, 2], 3))
