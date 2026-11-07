# =====================================================================
#                          QUEUE - REVISION NOTES
# =====================================================================
# (File is named queue_ds.py so it does not shadow Python's built-in
#  `queue` module.)
#
# WHAT IS A QUEUE?
#   - A linear data structure that follows FIFO: First In, First Out.
#   - Like a line at a ticket counter: join at the REAR, leave from the FRONT.
#
# OPERATIONS
#   enqueue(x) : add x at the rear                -> O(1)
#   dequeue()  : remove and return the front item -> O(1)
#   front()    : look at the front item           -> O(1)
#   is_empty() / size()                           -> O(1)
#   Space: O(n)
#
# TYPES
#   1. Simple queue   : FIFO.
#   2. Circular queue : fixed-size array where rear wraps around to the
#                       start, so space freed by dequeue is reused.
#                       next index = (i + 1) % capacity
#   3. Deque (double-ended queue): insert/delete at BOTH ends in O(1).
#   4. Priority queue : the element with the highest priority leaves
#                       first (not FIFO). Implemented with a HEAP
#                       (see heap.py).
#
# IMPLEMENTATIONS IN PYTHON
#   - collections.deque : append() / popleft() -> O(1). USE THIS.
#   - list.pop(0) is O(n) because every element shifts -> avoid it.
#   - queue.Queue       : thread-safe queue (for multithreading).
#   - heapq             : priority queue.
#
# deque CHEAT SHEET
#   from collections import deque
#   dq = deque()
#   dq.append(x)      dq.appendleft(x)     # add right / left
#   dq.pop()          dq.popleft()         # remove right / left
#   dq[0], dq[-1]                          # peek front / back
#   deque(maxlen=k)                        # auto-drops oldest items
#
# REAL-WORLD USES
#   - CPU / task scheduling, printer queues, request handling.
#   - BFS (breadth-first search) on trees and graphs.
#   - Buffers (keyboard buffer, IO buffers, streaming).
#
# COMMON INTERVIEW PATTERNS
#   - BFS / level order traversal of a tree.
#   - Shortest path in an unweighted graph or grid (BFS).
#   - Sliding window maximum -> MONOTONIC DEQUE, O(n).
#   - Implement a stack using queues / a queue using two stacks.
#   - First non-repeating character in a stream.
#   - Rotting oranges, number of islands (multi-source BFS).
#
# QUICK TIPS
#   - "Shortest path / minimum steps" in an unweighted graph -> BFS + queue.
#   - Circular queue full check : (rear + 1) % cap == front, or keep a
#     size counter (simpler, used below).
# =====================================================================

from collections import deque


class Queue:
    """Queue using collections.deque."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._items[0]

    def is_empty(self):
        return not self._items

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Queue(front -> rear: {list(self._items)})"


class _Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    """Queue using a linked list: enqueue at tail, dequeue at head."""

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, item):
        node = _Node(item)
        if self._tail:
            self._tail.next = node
        else:
            self._head = node
        self._tail = node
        self._size += 1

    def dequeue(self):
        if not self._head:
            raise IndexError("dequeue from empty queue")
        item = self._head.data
        self._head = self._head.next
        if not self._head:
            self._tail = None
        self._size -= 1
        return item

    def __len__(self):
        return self._size


class CircularQueue:
    """Fixed-capacity queue using an array with wrap-around indices."""

    def __init__(self, capacity):
        self._data = [None] * capacity
        self._cap = capacity
        self._front = 0
        self._size = 0

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("queue is full")
        rear = (self._front + self._size) % self._cap
        self._data[rear] = item
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._cap
        self._size -= 1
        return item

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._cap

    def __repr__(self):
        return f"CircularQueue(raw={self._data}, front={self._front}, size={self._size})"


class QueueUsingTwoStacks:
    """Amortized O(1) per operation: each element moves at most once."""

    def __init__(self):
        self._in = []
        self._out = []

    def enqueue(self, item):
        self._in.append(item)

    def dequeue(self):
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
        if not self._out:
            raise IndexError("dequeue from empty queue")
        return self._out.pop()


def sliding_window_max(nums, k):
    """Monotonic deque holding indices; values decrease from front to back."""
    dq, result = deque(), []
    for i, x in enumerate(nums):
        if dq and dq[0] <= i - k:       # front index left the window
            dq.popleft()
        while dq and nums[dq[-1]] < x:  # drop smaller elements
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


def shortest_path_grid(grid, start, end):
    """BFS on a grid of 0 (open) / 1 (wall). Returns min steps or -1."""
    rows, cols = len(grid), len(grid[0])
    q = deque([(start, 0)])
    seen = {start}
    while q:
        (r, c), dist = q.popleft()
        if (r, c) == end:
            return dist
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in seen:
                seen.add((nr, nc))
                q.append(((nr, nc), dist + 1))
    return -1


if __name__ == "__main__":
    print("----- Queue (deque) -----")
    q = Queue()
    for x in [1, 2, 3]:
        q.enqueue(x)
    print(q, "| front:", q.front())
    print("dequeue:", q.dequeue(), "->", q)

    print("\n----- Linked Queue -----")
    lq = LinkedQueue()
    for x in "abc":
        lq.enqueue(x)
    print("dequeue order:", [lq.dequeue() for _ in range(len(lq))])

    print("\n----- Circular Queue (capacity 3) -----")
    cq = CircularQueue(3)
    for x in [10, 20, 30]:
        cq.enqueue(x)
    print(cq, "| full:", cq.is_full())
    print("dequeue:", cq.dequeue())
    cq.enqueue(40)  # wraps around to index 0
    print(cq)

    print("\n----- Queue using two stacks -----")
    qs = QueueUsingTwoStacks()
    for x in [1, 2, 3]:
        qs.enqueue(x)
    print("dequeue:", qs.dequeue(), qs.dequeue())

    print("\n----- Deque -----")
    dq = deque([2, 3])
    dq.appendleft(1)
    dq.append(4)
    print(dq)
    print("pop:", dq.pop(), "| popleft:", dq.popleft(), "->", dq)

    print("\n----- Problems -----")
    print("sliding_window_max:", sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
    grid = [[0, 0, 0],
            [1, 1, 0],
            [0, 0, 0]]
    print("shortest_path_grid:", shortest_path_grid(grid, (0, 0), (2, 0)))
