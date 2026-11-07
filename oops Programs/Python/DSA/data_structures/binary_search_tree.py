# =====================================================================
#                   BINARY SEARCH TREE (BST) - REVISION NOTES
# =====================================================================
#
# WHAT IS A BST?
#   - A binary tree where, for EVERY node:
#       all values in the LEFT subtree  <  node.val
#       all values in the RIGHT subtree >  node.val
#   - Both subtrees are also BSTs.
#   - INORDER traversal of a BST gives the values in SORTED order.
#
#   Example:          8
#                   /   \
#                  3     10
#                 / \      \
#                1   6      14
#                   / \    /
#                  4   7  13
#   Inorder -> 1 3 4 6 7 8 10 13 14
#
# OPERATIONS
#   - Search : compare with node; go left if smaller, right if bigger.
#   - Insert : search for the value, then attach a new leaf where you
#              fall off the tree.
#   - Delete : 3 cases
#       1. Leaf node        -> just remove it.
#       2. One child        -> replace the node with its child.
#       3. Two children     -> replace the value with its INORDER SUCCESSOR
#                              (smallest in right subtree) or PREDECESSOR
#                              (largest in left subtree), then delete that
#                              successor/predecessor node.
#   - Min = leftmost node. Max = rightmost node.
#
# TIME COMPLEXITY (h = height of tree)
#   +-------------------+----------+------------------+----------+
#   | Operation         | Average  | Worst (skewed)   | Balanced |
#   +-------------------+----------+------------------+----------+
#   | Search            | O(log n) | O(n)             | O(log n) |
#   | Insert            | O(log n) | O(n)             | O(log n) |
#   | Delete            | O(log n) | O(n)             | O(log n) |
#   | Min / Max         | O(log n) | O(n)             | O(log n) |
#   | Inorder traversal | O(n)     | O(n)             | O(n)     |
#   +-------------------+----------+------------------+----------+
#   All operations are really O(h).
#   Inserting already sorted data (1, 2, 3, 4...) creates a SKEWED tree.
#
# SELF-BALANCING BSTs (keep h = O(log n) always)
#   - AVL tree      : |height(left) - height(right)| <= 1 for every node;
#                     fixed using rotations (LL, RR, LR, RL). Strictly
#                     balanced -> faster lookups.
#   - Red-Black tree: looser balance using node colors; fewer rotations
#                     -> faster inserts/deletes. Used by C++ std::map,
#                     Java TreeMap.
#   - B-tree / B+ tree: many keys per node; used in databases and file
#                     systems.
#
# BST vs HASH TABLE
#   - Hash table: O(1) average lookups, but NO ordering.
#   - BST: O(log n) (balanced), but supports ordered operations: sorted
#     iteration, min/max, floor/ceil, range queries, kth smallest.
#
# COMMON INTERVIEW PATTERNS
#   - Validate a BST (pass down a (low, high) range; don't just compare
#     with the immediate children!).
#   - Kth smallest element (inorder traversal, stop at k).
#   - LCA in a BST (use the ordering: both smaller -> go left, etc.).
#   - Floor / ceil of a value, inorder successor / predecessor.
#   - Convert a sorted array to a balanced BST (pick the middle as root).
#   - Range sum of BST, two sum in BST, trim a BST.
# =====================================================================


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    # ---------- insert ----------
    def insert(self, key):
        def _insert(node, key):
            if node is None:
                self.size += 1
                return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            # equal keys are ignored (no duplicates)
            return node

        self.root = _insert(self.root, key)

    # ---------- search (iterative) ----------
    def search(self, key):
        curr = self.root
        while curr:
            if key == curr.key:
                return True
            curr = curr.left if key < curr.key else curr.right
        return False

    # ---------- delete ----------
    def delete(self, key):
        def _min_node(node):
            while node.left:
                node = node.left
            return node

        def _delete(node, key):
            if node is None:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                # case 1 & 2: zero or one child
                if node.left is None:
                    self.size -= 1
                    return node.right
                if node.right is None:
                    self.size -= 1
                    return node.left
                # case 3: two children -> copy inorder successor
                succ = _min_node(node.right)
                node.key = succ.key
                node.right = _delete(node.right, succ.key)
            return node

        self.root = _delete(self.root, key)

    # ---------- min / max ----------
    def min(self):
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.key if curr else None

    def max(self):
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.key if curr else None

    # ---------- floor / ceil ----------
    def floor(self, key):
        """Largest value <= key."""
        curr, result = self.root, None
        while curr:
            if curr.key == key:
                return key
            if curr.key < key:
                result = curr.key
                curr = curr.right
            else:
                curr = curr.left
        return result

    def ceil(self, key):
        """Smallest value >= key."""
        curr, result = self.root, None
        while curr:
            if curr.key == key:
                return key
            if curr.key > key:
                result = curr.key
                curr = curr.left
            else:
                curr = curr.right
        return result

    # ---------- traversal & queries ----------
    def inorder(self):
        out = []

        def _walk(node):
            if node:
                _walk(node.left)
                out.append(node.key)
                _walk(node.right)

        _walk(self.root)
        return out

    def kth_smallest(self, k):
        stack, curr = [], self.root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.key
            curr = curr.right
        return None

    def lca(self, a, b):
        curr = self.root
        while curr:
            if a < curr.key and b < curr.key:
                curr = curr.left
            elif a > curr.key and b > curr.key:
                curr = curr.right
            else:
                return curr.key
        return None

    def range_query(self, lo, hi):
        """All keys in [lo, hi], in sorted order; skips useless subtrees."""
        out = []

        def _walk(node):
            if not node:
                return
            if lo < node.key:
                _walk(node.left)
            if lo <= node.key <= hi:
                out.append(node.key)
            if node.key < hi:
                _walk(node.right)

        _walk(self.root)
        return out

    def height(self):
        def _h(node):
            return 0 if not node else 1 + max(_h(node.left), _h(node.right))

        return _h(self.root)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        return self.search(key)


def is_valid_bst(node, low=float("-inf"), high=float("inf")):
    if node is None:
        return True
    if not low < node.key < high:
        return False
    return is_valid_bst(node.left, low, node.key) and is_valid_bst(node.right, node.key, high)


def sorted_array_to_bst(arr):
    """Pick the middle as the root -> balanced BST of height O(log n)."""
    if not arr:
        return None
    mid = len(arr) // 2
    node = Node(arr[mid])
    node.left = sorted_array_to_bst(arr[:mid])
    node.right = sorted_array_to_bst(arr[mid + 1:])
    return node


if __name__ == "__main__":
    bst = BST()
    for x in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        bst.insert(x)

    print("----- BST -----")
    print("inorder (sorted):", bst.inorder(), "| size:", len(bst), "| height:", bst.height())
    print("search(6):", bst.search(6), "| 5 in bst:", 5 in bst)
    print("min:", bst.min(), "| max:", bst.max())
    print("floor(5):", bst.floor(5), "| ceil(5):", bst.ceil(5), "| ceil(15):", bst.ceil(15))
    print("3rd smallest:", bst.kth_smallest(3))
    print("LCA(4, 7):", bst.lca(4, 7), "| LCA(4, 13):", bst.lca(4, 13))
    print("range [4, 10]:", bst.range_query(4, 10))
    print("valid BST:", is_valid_bst(bst.root))

    print("\n----- Delete -----")
    bst.delete(1)    # leaf
    print("delete 1 (leaf)        :", bst.inorder())
    bst.delete(14)   # one child
    print("delete 14 (one child)  :", bst.inorder())
    bst.delete(3)    # two children
    print("delete 3 (two children):", bst.inorder(), "| root:", bst.root.key)

    print("\n----- Skewed vs balanced -----")
    skewed = BST()
    for x in range(1, 8):
        skewed.insert(x)
    print("sorted inserts 1..7 -> height:", skewed.height(), "(skewed, like a linked list)")
    balanced = BST()
    balanced.root = sorted_array_to_bst(list(range(1, 8)))
    print("sorted_array_to_bst 1..7 -> height:", balanced.height(), "(balanced)")
