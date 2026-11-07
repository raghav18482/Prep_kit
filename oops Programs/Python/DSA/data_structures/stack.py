# =====================================================================
#                         STACK - REVISION NOTES
# =====================================================================
#
# WHAT IS A STACK?
#   - A linear data structure that follows LIFO: Last In, First Out.
#   - Think of a stack of plates: you add and remove only from the TOP.
#
# OPERATIONS
#   push(x)   : add x on top                          -> O(1)
#   pop()     : remove and return the top element     -> O(1)
#   peek()    : look at the top element (no removal)  -> O(1)
#   is_empty(): check whether the stack is empty      -> O(1)
#   size()    : number of elements                    -> O(1)
#   Space: O(n)
#
# IMPLEMENTATIONS
#   1. Array / Python list : append() = push, pop() = pop.  (most common)
#   2. Linked list         : push and pop at the HEAD, both O(1).
#   3. collections.deque   : append() / pop(), also O(1).
#   - Do NOT use list.insert(0, x) / list.pop(0); those are O(n).
#
# ERRORS
#   - Stack Overflow : pushing onto a full (fixed-size) stack.
#                      Also deep recursion -> "maximum recursion depth".
#   - Stack Underflow: popping from an empty stack.
#
# REAL-WORLD USES
#   - Function call stack (recursion uses it internally).
#   - Undo / redo in editors, browser back button.
#   - Expression evaluation and syntax parsing (compilers).
#   - DFS (depth-first search) on graphs/trees, done iteratively.
#
# COMMON INTERVIEW PATTERNS
#   - Valid parentheses / balanced brackets.
#   - Infix -> postfix conversion; evaluate postfix (Reverse Polish).
#   - MONOTONIC STACK (keeps elements in increasing/decreasing order):
#       * Next greater element / next smaller element.
#       * Daily temperatures, stock span.
#       * Largest rectangle in histogram, trapping rain water.
#   - Min stack: get the minimum in O(1) (keep a second stack of mins).
#   - Implement a queue using two stacks.
#   - Reverse a string / decode string ("3[a2[c]]").
#
# QUICK TIPS
#   - Always check is_empty() before pop/peek.
#   - "Next greater/smaller" or "previous greater/smaller" in a problem
#     -> think MONOTONIC STACK, O(n).
# =====================================================================


class Stack:
    """Stack using a Python list (top = end of the list)."""

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack (underflow)")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return not self._items

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Stack(bottom -> top: {self._items})"


class _Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedStack:
    """Stack using a linked list (top = head)."""

    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, item):
        self._top = _Node(item, self._top)
        self._size += 1

    def pop(self):
        if self._top is None:
            raise IndexError("pop from empty stack (underflow)")
        item = self._top.data
        self._top = self._top.next
        self._size -= 1
        return item

    def peek(self):
        if self._top is None:
            raise IndexError("peek from empty stack")
        return self._top.data

    def is_empty(self):
        return self._top is None

    def __len__(self):
        return self._size


class MinStack:
    """Stack that returns the minimum element in O(1)."""

    def __init__(self):
        self._items = []
        self._mins = []

    def push(self, item):
        self._items.append(item)
        if not self._mins or item <= self._mins[-1]:
            self._mins.append(item)

    def pop(self):
        item = self._items.pop()
        if item == self._mins[-1]:
            self._mins.pop()
        return item

    def get_min(self):
        return self._mins[-1]


# ---------------- classic stack problems ----------------
def is_balanced(expr):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in expr:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


def infix_to_postfix(expr):
    """Shunting-yard algorithm for single-character operands."""
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    out, stack = [], []
    for ch in expr.replace(" ", ""):
        if ch.isalnum():
            out.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack[-1] != "(":
                out.append(stack.pop())
            stack.pop()  # remove "("
        else:
            # ^ is right-associative, the others are left-associative
            while (stack and stack[-1] != "(" and
                   (precedence[stack[-1]] > precedence[ch] or
                    (precedence[stack[-1]] == precedence[ch] and ch != "^"))):
                out.append(stack.pop())
            stack.append(ch)
    while stack:
        out.append(stack.pop())
    return "".join(out)


def evaluate_postfix(tokens):
    stack = []
    for tok in tokens:
        if tok in "+-*/":
            b, a = stack.pop(), stack.pop()  # order matters!
            if tok == "+":
                stack.append(a + b)
            elif tok == "-":
                stack.append(a - b)
            elif tok == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))  # truncate toward zero
        else:
            stack.append(int(tok))
    return stack.pop()


def next_greater_element(arr):
    """Monotonic decreasing stack of indices. -1 if no greater element."""
    result = [-1] * len(arr)
    stack = []
    for i, x in enumerate(arr):
        while stack and arr[stack[-1]] < x:
            result[stack.pop()] = x
        stack.append(i)
    return result


if __name__ == "__main__":
    print("----- Stack (list) -----")
    s = Stack()
    for x in [1, 2, 3]:
        s.push(x)
    print(s, "| peek:", s.peek())
    print("pop:", s.pop(), "->", s)

    print("\n----- Stack (linked list) -----")
    ls = LinkedStack()
    for x in "abc":
        ls.push(x)
    print("pop order:", [ls.pop() for _ in range(len(ls))])

    print("\n----- Min Stack -----")
    ms = MinStack()
    for x in [5, 3, 7, 2, 8]:
        ms.push(x)
    print("min:", ms.get_min())
    ms.pop()
    ms.pop()
    print("after 2 pops, min:", ms.get_min())

    print("\n----- Problems -----")
    for e in ["{[()]}", "([)]", "(("]:
        print(f"is_balanced({e!r}):", is_balanced(e))
    print("infix_to_postfix('a+b*(c^d-e)'):", infix_to_postfix("a+b*(c^d-e)"))
    print("evaluate_postfix(['2','1','+','3','*']):", evaluate_postfix(["2", "1", "+", "3", "*"]))
    print("next_greater_element([4,5,2,25]):", next_greater_element([4, 5, 2, 25]))
