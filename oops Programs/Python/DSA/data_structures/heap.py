# =====================================================================
#                         HEAP - REVISION NOTES
# =====================================================================
#
# WHAT IS A HEAP?
#   - A heap is a COMPLETE BINARY TREE that satisfies the HEAP PROPERTY.
#   - Complete binary tree: every level is fully filled except possibly
#     the last, and the last level is filled from LEFT to RIGHT.
#   - Because it is complete, it is stored in a plain ARRAY (no pointers).
#
# TYPES
#   - Min-Heap: parent <= children  -> smallest element is at the root.
#   - Max-Heap: parent >= children  -> largest element is at the root.
#   - NOTE: a heap is NOT sorted. Only the root is guaranteed to be the
#     min/max. Siblings have no ordering between them.
#
# ARRAY INDEXING (0-based)
#   For a node at index i:
#       parent      -> (i - 1) // 2
#       left child  -> 2 * i + 1
#       right child -> 2 * i + 2
#   Leaf nodes are at indices n//2 ... n-1
#   Last non-leaf node is at index n//2 - 1
#   (For 1-based indexing: parent = i//2, left = 2i, right = 2i+1)
#
#   Example Min-Heap:          Array: [1, 3, 2, 5, 9, 8]
#               1
#             /   \
#            3     2
#           / \   /
#          5   9 8
#
#   Height of heap with n nodes = floor(log2 n)  -> that is why ops are O(log n)
#
# CORE OPERATIONS
#   1. Insert (push):
#        - Add element at the end of the array.
#        - "Sift up" / "bubble up" / "heapify up": swap with parent while
#          it violates the heap property.                     -> O(log n)
#
#   2. Delete root (pop / extract-min / extract-max):
#        - Swap root with the last element, remove the last element.
#        - "Sift down" / "heapify down": swap with the smaller (min-heap)
#          or larger (max-heap) child until the property holds. -> O(log n)
#
#   3. Peek (get min/max):  return arr[0]                     -> O(1)
#
#   4. Build heap (heapify an array):
#        - Call sift down on every non-leaf node, from index n//2 - 1
#          down to 0.
#        - Looks like O(n log n) but is actually O(n), because most
#          nodes are near the bottom and sift down only a little.
#
#   5. Search for an arbitrary element:                        -> O(n)
#   6. Delete an arbitrary element (if index known):           -> O(log n)
#        - Replace with last element, then sift up OR sift down.
#
# TIME COMPLEXITY SUMMARY
#   +----------------+-----------+
#   | Operation      | Time      |
#   +----------------+-----------+
#   | peek           | O(1)      |
#   | push           | O(log n)  |
#   | pop            | O(log n)  |
#   | build heap     | O(n)      |
#   | search         | O(n)      |
#   | heap sort      | O(n log n)|
#   +----------------+-----------+
#   Space: O(n) for the heap; heap sort itself is O(1) extra (in-place).
#
# HEAP SORT
#   1. Build a MAX-heap from the array.                       -> O(n)
#   2. Repeat n-1 times: swap root (max) with the last element of the
#      heap, shrink heap size by 1, sift down the new root.   -> O(n log n)
#   - In-place, O(1) extra space.
#   - NOT stable (equal elements may change relative order).
#   - Always O(n log n): best, average and worst case.
#
# PYTHON'S BUILT-IN: heapq module (MIN-heap only)
#   import heapq
#   heapq.heapify(arr)            # build heap in place, O(n)
#   heapq.heappush(arr, x)        # push
#   heapq.heappop(arr)            # pop smallest
#   arr[0]                        # peek smallest
#   heapq.heappushpop(arr, x)     # push then pop (efficient)
#   heapq.heapreplace(arr, x)     # pop then push (efficient)
#   heapq.nlargest(k, arr)        # k largest elements
#   heapq.nsmallest(k, arr)       # k smallest elements
#   - MAX-heap trick: push negative values ->  heappush(h, -x), -heappop(h)
#   - Tuples are compared element by element: heappush(h, (priority, item))
#
# COMMON APPLICATIONS / INTERVIEW PATTERNS
#   - Priority Queue (heap is the standard implementation).
#   - Kth largest element  -> MIN-heap of size k (root = kth largest).
#   - Kth smallest element -> MAX-heap of size k (root = kth smallest).
#   - Top K frequent elements  (count with dict, then heap of size k).
#   - Merge K sorted lists/arrays (push first item of each list).
#   - Median of a data stream (two heaps: max-heap for the lower half,
#     min-heap for the upper half, keep their sizes balanced).
#   - Dijkstra's shortest path, Prim's MST (min-heap of distances/edges).
#   - Task scheduling, K closest points to origin, sliding window max.
#
# QUICK TIPS TO REMEMBER
#   - "K largest" -> use MIN-heap;  "K smallest" -> use MAX-heap.
#     (you keep k items and throw away the root when size exceeds k)
#   - Heap vs sorting: a heap gives the top-k in O(n log k), better than
#     O(n log n) when k is much smaller than n.
#   - Heap vs BST: a heap has O(1) min/max and O(n) search; a balanced
#     BST has O(log n) min/max and O(log n) search.
# =====================================================================


class MinHeap:
    def __init__(self, items=None):
        self.heap = []
        if items:
            self.heap = list(items)
            self._heapify()

    # ---------- helper methods ----------
    @staticmethod
    def _parent(i):
        return (i - 1) // 2

    @staticmethod
    def _left(i):
        return 2 * i + 1

    @staticmethod
    def _right(i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _compare(self, a, b):
        """Return True if a should be above b in the heap."""
        return a < b

    def _sift_up(self, i):
        """Move element at index i up until heap property is restored."""
        while i > 0:
            p = self._parent(i)
            if self._compare(self.heap[i], self.heap[p]):
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i):
        """Move element at index i down until heap property is restored."""
        n = len(self.heap)
        while True:
            best = i
            l, r = self._left(i), self._right(i)
            if l < n and self._compare(self.heap[l], self.heap[best]):
                best = l
            if r < n and self._compare(self.heap[r], self.heap[best]):
                best = r
            if best == i:
                break
            self._swap(i, best)
            i = best

    def _heapify(self):
        """Build heap from an unordered list in O(n)."""
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._sift_down(i)

    # ---------- public methods ----------
    def push(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        """Remove and return the root element."""
        if not self.heap:
            raise IndexError("pop from empty heap")
        self._swap(0, len(self.heap) - 1)
        root = self.heap.pop()
        if self.heap:
            self._sift_down(0)
        return root

    def peek(self):
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def pushpop(self, value):
        """Push value, then pop and return the root (faster than push + pop)."""
        if self.heap and self._compare(self.heap[0], value):
            value, self.heap[0] = self.heap[0], value
            self._sift_down(0)
        return value

    def replace(self, value):
        """Pop the root, then push value."""
        if not self.heap:
            raise IndexError("replace on empty heap")
        root = self.heap[0]
        self.heap[0] = value
        self._sift_down(0)
        return root

    def is_empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.heap})"


class MaxHeap(MinHeap):
    def _compare(self, a, b):
        return a > b


def heap_sort(arr):
    """In-place heap sort (ascending) using a max-heap."""
    n = len(arr)

    def sift_down(i, size):
        while True:
            largest = i
            l, r = 2 * i + 1, 2 * i + 2
            if l < size and arr[l] > arr[largest]:
                largest = l
            if r < size and arr[r] > arr[largest]:
                largest = r
            if largest == i:
                return
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest

    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, n)

    # Move current max to the end, shrink heap, repeat
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(0, end)

    return arr


if __name__ == "__main__":
    print("----- Min Heap -----")
    min_heap = MinHeap()
    for x in [5, 3, 8, 1, 9, 2]:
        min_heap.push(x)
    print(min_heap)
    print("peek:", min_heap.peek())
    print("popped in order:", [min_heap.pop() for _ in range(len(min_heap))])

    print("\n----- Max Heap (built with heapify) -----")
    max_heap = MaxHeap([5, 3, 8, 1, 9, 2])
    print(max_heap)
    print("peek:", max_heap.peek())
    print("popped in order:", [max_heap.pop() for _ in range(len(max_heap))])

    print("\n----- Heap Sort -----")
    print(heap_sort([12, 11, 13, 5, 6, 7]))

    print("\n----- K largest elements using a min heap of size k -----")
    nums, k = [3, 2, 1, 5, 6, 4], 2
    h = MinHeap()
    for n in nums:
        h.push(n)
        if len(h) > k:
            h.pop()
    print(f"{k} largest:", sorted(h.heap, reverse=True), "| kth largest:", h.peek())
