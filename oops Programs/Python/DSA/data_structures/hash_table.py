# =====================================================================
#                   HASH TABLE / HASH MAP - REVISION NOTES
# =====================================================================
#
# WHAT IS A HASH TABLE?
#   - Stores KEY -> VALUE pairs with average O(1) insert, lookup, delete.
#   - A HASH FUNCTION turns a key into an integer, and that integer is
#     mapped to a bucket index:   index = hash(key) % capacity
#   - Python's dict and set are hash tables.
#
# GOOD HASH FUNCTION
#   - Deterministic: the same key always gives the same hash.
#   - Spreads keys uniformly across buckets.
#   - Fast to compute.
#   - Keys must be IMMUTABLE / hashable (int, str, tuple; NOT list/dict).
#
# COLLISION: two different keys map to the same index.
#   1. Separate chaining: each bucket holds a list (or linked list) of
#      (key, value) pairs.                       <- implemented below
#   2. Open addressing: store everything in the array itself and probe
#      for the next free slot:
#        * Linear probing   : i, i+1, i+2, ...   (causes clustering)
#        * Quadratic probing: i, i+1^2, i+2^2, ...
#        * Double hashing   : i + k * hash2(key)
#      Deletion needs a "tombstone" marker.   (Python's dict uses this.)
#
# LOAD FACTOR (alpha) = number of items / number of buckets
#   - Higher alpha -> more collisions -> slower operations.
#   - When alpha passes a threshold (e.g. 0.75), REHASH: create a bigger
#     table (usually 2x) and reinsert every item. O(n) once, so insert
#     stays O(1) amortized.
#
# TIME COMPLEXITY
#   +------------+----------+------------------------------------+
#   | Operation  | Average  | Worst (all keys collide)           |
#   +------------+----------+------------------------------------+
#   | Insert     | O(1)     | O(n)                               |
#   | Search     | O(1)     | O(n)                               |
#   | Delete     | O(1)     | O(n)                               |
#   +------------+----------+------------------------------------+
#   Space: O(n). Hash tables do NOT keep keys in sorted order
#   (Python 3.7+ dict keeps INSERTION order).
#
# PYTHON CHEAT SHEET
#   d = {}; d[k] = v; d.get(k, default); k in d; del d[k]; d.pop(k)
#   d.items(), d.keys(), d.values()
#   from collections import defaultdict, Counter, OrderedDict
#   defaultdict(list)    -> missing keys start as []
#   Counter("banana")    -> {'a': 3, 'n': 2, 'b': 1}; .most_common(k)
#   set: add, remove, discard, |, &, -, ^    (union, intersection, ...)
#
# COMMON INTERVIEW PATTERNS
#   - Two sum (store value -> index while scanning).
#   - Frequency counting: anagrams, first unique character, majority element.
#   - Group anagrams (key = sorted word or a tuple of letter counts).
#   - Subarray sum equals k (prefix sum + hash map of counts).
#   - Longest consecutive sequence (set, O(n)).
#   - Longest substring without repeating characters (window + map).
#   - LRU cache (hash map + doubly linked list / OrderedDict).
#   - Detecting duplicates / visited states in BFS/DFS.
#
# QUICK TIPS
#   - "Have I seen this before?" or "how many times?" -> hash map / set.
#   - Trade space for time: an O(n^2) brute force often becomes O(n).
# =====================================================================


class HashTable:
    """Hash map using separate chaining with automatic resizing."""

    def __init__(self, capacity=8, max_load=0.75):
        self._capacity = capacity
        self._size = 0
        self._max_load = max_load
        self._buckets = [[] for _ in range(capacity)]

    def _index(self, key):
        return hash(key) % self._capacity

    def put(self, key, value):
        bucket = self._buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:              # key exists -> update
                bucket[i] = (key, value)
                return
        bucket.append((key, value))   # new key
        self._size += 1
        if self._size / self._capacity > self._max_load:
            self._rehash()

    def get(self, key, default=None):
        for k, v in self._buckets[self._index(key)]:
            if k == key:
                return v
        return default

    def remove(self, key):
        bucket = self._buckets[self._index(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return v
        raise KeyError(key)

    def _rehash(self):
        old_items = self.items()
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        for k, v in old_items:
            self.put(k, v)

    def items(self):
        return [pair for bucket in self._buckets for pair in bucket]

    def load_factor(self):
        return self._size / self._capacity

    def __contains__(self, key):
        return any(k == key for k, _ in self._buckets[self._index(key)])

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        for k, v in self._buckets[self._index(key)]:
            if k == key:
                return v
        raise KeyError(key)

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"HashTable({dict(self.items())}, capacity={self._capacity})"


class LinearProbingHashTable:
    """Open addressing with linear probing and tombstones for deletion."""

    _DELETED = object()  # tombstone marker

    def __init__(self, capacity=8):
        self._capacity = capacity
        self._keys = [None] * capacity
        self._values = [None] * capacity
        self._size = 0

    def _probe(self, key):
        """Yield slot indices in probe order, starting at hash(key)."""
        start = hash(key) % self._capacity
        for step in range(self._capacity):
            yield (start + step) % self._capacity

    def put(self, key, value):
        if (self._size + 1) / self._capacity > 0.5:
            self._resize()
        first_free = None
        for i in self._probe(key):
            k = self._keys[i]
            if k is None:
                if first_free is None:
                    first_free = i
                break
            if k is self._DELETED:
                if first_free is None:
                    first_free = i
            elif k == key:
                self._values[i] = value
                return
        self._keys[first_free] = key
        self._values[first_free] = value
        self._size += 1

    def get(self, key, default=None):
        for i in self._probe(key):
            k = self._keys[i]
            if k is None:
                return default
            if k is not self._DELETED and k == key:
                return self._values[i]
        return default

    def remove(self, key):
        for i in self._probe(key):
            k = self._keys[i]
            if k is None:
                break
            if k is not self._DELETED and k == key:
                self._keys[i] = self._DELETED
                self._size -= 1
                return self._values[i]
        raise KeyError(key)

    def _resize(self):
        old = [(k, v) for k, v in zip(self._keys, self._values)
               if k is not None and k is not self._DELETED]
        self._capacity *= 2
        self._keys = [None] * self._capacity
        self._values = [None] * self._capacity
        self._size = 0
        for k, v in old:
            self.put(k, v)

    def __len__(self):
        return self._size


# ---------------- classic hashing problems ----------------
def two_sum(nums, target):
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        if target - x in seen:
            return seen[target - x], i
        seen[x] = i
    return None


def group_anagrams(words):
    groups = {}
    for w in words:
        groups.setdefault("".join(sorted(w)), []).append(w)
    return list(groups.values())


def subarray_sum_equals_k(nums, k):
    count, prefix = 0, 0
    seen = {0: 1}  # prefix sum -> how many times it occurred
    for x in nums:
        prefix += x
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count


def longest_consecutive(nums):
    s, best = set(nums), 0
    for x in s:
        if x - 1 not in s:  # x starts a sequence
            length = 1
            while x + length in s:
                length += 1
            best = max(best, length)
    return best


if __name__ == "__main__":
    print("----- Hash Table (separate chaining) -----")
    ht = HashTable(capacity=4)
    for i, name in enumerate(["apple", "banana", "cherry", "date", "elder"]):
        ht[name] = i
        print(f"put {name!r}: load factor = {ht.load_factor():.2f}, capacity = {ht._capacity}")
    print(ht)
    print("get('cherry'):", ht.get("cherry"), "| 'fig' in ht:", "fig" in ht)
    print("remove('banana'):", ht.remove("banana"), "| size:", len(ht))

    print("\n----- Hash Table (linear probing) -----")
    lp = LinearProbingHashTable()
    for k, v in [("a", 1), ("b", 2), ("c", 3)]:
        lp.put(k, v)
    lp.remove("b")
    print("get('a'):", lp.get("a"), "| get('b'):", lp.get("b"), "| get('c'):", lp.get("c"))

    print("\n----- Problems -----")
    print("two_sum([2,7,11,15], 9):", two_sum([2, 7, 11, 15], 9))
    print("group_anagrams:", group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print("subarray_sum_equals_k([1,1,1], 2):", subarray_sum_equals_k([1, 1, 1], 2))
    print("longest_consecutive([100,4,200,1,3,2]):", longest_consecutive([100, 4, 200, 1, 3, 2]))
