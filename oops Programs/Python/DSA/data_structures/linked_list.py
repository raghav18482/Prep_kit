# =====================================================================
#                      LINKED LIST - REVISION NOTES
# =====================================================================
#
# WHAT IS A LINKED LIST?
#   - A linear collection of NODES, where each node holds data and a
#     pointer (reference) to the next node.
#   - Nodes are NOT stored contiguously in memory, so there is no O(1)
#     random access; you must walk from the head.
#
# TYPES
#   1. Singly linked list : node -> next.          head -> 1 -> 2 -> 3 -> None
#   2. Doubly linked list : node has prev and next. None <- 1 <-> 2 <-> 3 -> None
#   3. Circular linked list: last node points back to head (no None).
#
# TERMS
#   - head : first node.  tail : last node.
#   - Dummy / sentinel node: a fake node placed before head so that edge
#     cases (empty list, deleting head) need no special handling.
#
# TIME COMPLEXITY
#   +--------------------------------+---------+---------+
#   | Operation                      | Singly  | Doubly  |
#   +--------------------------------+---------+---------+
#   | Access / search by index/value | O(n)    | O(n)    |
#   | Insert at head                 | O(1)    | O(1)    |
#   | Insert at tail (with tail ptr) | O(1)    | O(1)    |
#   | Delete head                    | O(1)    | O(1)    |
#   | Delete tail                    | O(n)    | O(1)    |
#   | Delete a given node            | O(n)    | O(1)    |
#   | Insert after a given node      | O(1)    | O(1)    |
#   +--------------------------------+---------+---------+
#   Space: O(n), plus extra memory per node for the pointers.
#
# ARRAY vs LINKED LIST
#   - Array: O(1) access, O(n) insert/delete in the middle, cache friendly.
#   - Linked list: O(n) access, O(1) insert/delete once you have the node,
#     no resizing, but poor cache locality and pointer overhead.
#
# COMMON INTERVIEW PATTERNS
#   - Reverse a linked list (iterative: prev, curr, next pointers).
#   - Fast & slow pointers (Floyd's tortoise and hare):
#       * Find the middle node.
#       * Detect a cycle; find where the cycle starts.
#   - Find the nth node from the end: move one pointer n steps ahead first.
#   - Merge two sorted lists (use a dummy node).
#   - Check whether the list is a palindrome (find middle, reverse 2nd half).
#   - Remove duplicates, intersection of two lists, add two numbers.
#   - LRU Cache = hash map + doubly linked list.
#
# QUICK TIPS
#   - Always check for None before accessing node.next.
#   - Draw the pointers on paper before re-linking them.
#   - When re-linking, save node.next BEFORE you overwrite it.
# =====================================================================


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_head(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def insert_at_tail(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        self.size += 1

    def insert_at(self, index, data):
        if not 0 <= index <= self.size:
            raise IndexError("index out of range")
        if index == 0:
            return self.insert_at_head(data)
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        node = Node(data)
        node.next = prev.next
        prev.next = node
        self.size += 1

    def delete(self, data):
        """Delete the first node with the given value. Returns True if deleted."""
        dummy = Node(None)
        dummy.next = self.head
        prev = dummy
        while prev.next:
            if prev.next.data == data:
                prev.next = prev.next.next
                self.head = dummy.next
                self.size -= 1
                return True
            prev = prev.next
        return False

    def search(self, data):
        curr, i = self.head, 0
        while curr:
            if curr.data == data:
                return i
            curr, i = curr.next, i + 1
        return -1

    def reverse(self):
        prev, curr = None, self.head
        while curr:
            nxt = curr.next   # save next
            curr.next = prev  # reverse the pointer
            prev = curr       # move prev forward
            curr = nxt        # move curr forward
        self.head = prev

    def middle(self):
        """Fast & slow pointers: slow ends at the middle."""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def has_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def nth_from_end(self, n):
        fast = slow = self.head
        for _ in range(n):
            if not fast:
                return None
            fast = fast.next
        while fast:
            fast, slow = fast.next, slow.next
        return slow.data if slow else None

    def to_list(self):
        out, curr = [], self.head
        while curr:
            out.append(curr.data)
            curr = curr.next
        return out

    def __len__(self):
        return self.size

    def __repr__(self):
        return " -> ".join(map(str, self.to_list())) + " -> None"


def merge_sorted(l1, l2):
    """Merge two sorted chains of Nodes using a dummy node."""
    dummy = tail = Node(None)
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = DNode(data)
        if not self.tail:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def prepend(self, data):
        node = DNode(data)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def remove_node(self, node):
        """O(1) removal when we already have the node."""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = node.next = None
        self.size -= 1

    def pop(self):
        if not self.tail:
            raise IndexError("pop from empty list")
        data = self.tail.data
        self.remove_node(self.tail)
        return data

    def popleft(self):
        if not self.head:
            raise IndexError("pop from empty list")
        data = self.head.data
        self.remove_node(self.head)
        return data

    def find(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return curr
            curr = curr.next
        return None

    def forward(self):
        out, curr = [], self.head
        while curr:
            out.append(curr.data)
            curr = curr.next
        return out

    def backward(self):
        out, curr = [], self.tail
        while curr:
            out.append(curr.data)
            curr = curr.prev
        return out

    def __len__(self):
        return self.size

    def __repr__(self):
        return "None <- " + " <-> ".join(map(str, self.forward())) + " -> None"


if __name__ == "__main__":
    print("----- Singly Linked List -----")
    sll = SinglyLinkedList()
    for x in [1, 2, 3, 4, 5]:
        sll.insert_at_tail(x)
    sll.insert_at_head(0)
    sll.insert_at(3, 99)
    print(sll)
    print("search(99):", sll.search(99))
    sll.delete(99)
    print("after delete(99):", sll)
    print("middle:", sll.middle(), "| 2nd from end:", sll.nth_from_end(2))
    sll.reverse()
    print("reversed:", sll)
    print("has_cycle:", sll.has_cycle())

    a, b = SinglyLinkedList(), SinglyLinkedList()
    for x in [1, 3, 5]:
        a.insert_at_tail(x)
    for x in [2, 4, 6]:
        b.insert_at_tail(x)
    merged = SinglyLinkedList()
    merged.head = merge_sorted(a.head, b.head)
    print("merged sorted:", merged)

    print("\n----- Doubly Linked List -----")
    dll = DoublyLinkedList()
    for x in [10, 20, 30]:
        dll.append(x)
    dll.prepend(5)
    print(dll)
    dll.remove_node(dll.find(20))
    print("after removing 20:", dll)
    print("backward:", dll.backward())
    print("pop:", dll.pop(), "| popleft:", dll.popleft(), "->", dll)
