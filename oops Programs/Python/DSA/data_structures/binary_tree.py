# =====================================================================
#                       BINARY TREE - REVISION NOTES
# =====================================================================
#
# WHAT IS A TREE?
#   - A hierarchical, non-linear data structure of NODES connected by
#     EDGES, with no cycles. A tree with n nodes has n - 1 edges.
#   - BINARY TREE: every node has at most 2 children (left and right).
#
# TERMS
#   - Root: top node. Leaf: node with no children.
#   - Parent / child / sibling / ancestor / descendant.
#   - Depth of a node : number of edges from the root to the node.
#   - Height of a node: number of edges on the longest path down to a leaf.
#   - Height of tree = height of root. (Some books count nodes instead.)
#   - Level: all nodes at the same depth.
#
# TYPES OF BINARY TREES
#   - Full / strict : every node has 0 or 2 children.
#   - Complete      : all levels full except possibly the last, which is
#                     filled from the left (heaps are complete trees).
#   - Perfect       : all internal nodes have 2 children, all leaves at the
#                     same level. Nodes = 2^(h+1) - 1.
#   - Balanced      : height of left and right subtrees differ by at most 1
#                     for every node -> height is O(log n).
#   - Degenerate / skewed: every node has one child -> behaves like a
#                     linked list, height is O(n).
#
# USEFUL FACTS
#   - Max nodes at level L = 2^L.
#   - Max nodes in a tree of height h = 2^(h+1) - 1.
#   - Min height with n nodes = floor(log2 n).
#
# TRAVERSALS (all O(n) time)
#   DFS (depth first), uses recursion or a stack:
#     - Preorder  : Root, Left, Right  -> copy/serialize a tree.
#     - Inorder   : Left, Root, Right  -> gives SORTED order for a BST.
#     - Postorder : Left, Right, Root  -> delete a tree, evaluate expressions.
#   BFS (breadth first), uses a queue:
#     - Level order: level by level, left to right.
#
#   Example:          1
#                   /   \
#                  2     3
#                 / \     \
#                4   5     6
#     Preorder : 1 2 4 5 3 6
#     Inorder  : 4 2 5 1 3 6
#     Postorder: 4 5 2 6 3 1
#     Level    : [1] [2, 3] [4, 5, 6]
#
# SPACE
#   - Recursive DFS uses O(h) stack space (O(log n) balanced, O(n) skewed).
#   - BFS uses O(w) where w = maximum width of the tree.
#
# COMMON INTERVIEW PATTERNS
#   - Height / max depth, diameter, check if balanced.
#   - Same tree, symmetric tree, mirror / invert a tree.
#   - Lowest common ancestor (LCA).
#   - Path sum, root-to-leaf paths, max path sum.
#   - Left / right / top / bottom view, zigzag level order.
#   - Build a tree from preorder + inorder traversals.
#   - Serialize / deserialize a tree.
#
# QUICK TIPS
#   - Most tree problems are recursion: solve for left, solve for right,
#     combine at the root. Always handle the `None` base case first.
#   - "Level" or "minimum depth" questions -> BFS.
# =====================================================================

from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Build a tree from a level-order list; None marks a missing node."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


# ---------------- recursive DFS traversals ----------------
def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []


def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []


# ---------------- iterative DFS traversals ----------------
def preorder_iterative(root):
    if not root:
        return []
    out, stack = [], [root]
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.right:            # push right first so left is processed first
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return out


def inorder_iterative(root):
    out, stack, curr = [], [], root
    while curr or stack:
        while curr:               # go as far left as possible
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        out.append(curr.val)
        curr = curr.right
    return out


def postorder_iterative(root):
    """Reverse of (Root, Right, Left)."""
    if not root:
        return []
    out, stack = [], [root]
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return out[::-1]


# ---------------- BFS ----------------
def level_order(root):
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(level)
    return out


# ---------------- common problems ----------------
def height(root):
    """Number of nodes on the longest root-to-leaf path (0 for empty)."""
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


def count_nodes(root):
    return 0 if not root else 1 + count_nodes(root.left) + count_nodes(root.right)


def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)


def diameter(root):
    """Longest path (in edges) between any two nodes."""
    best = 0

    def depth(node):
        nonlocal best
        if not node:
            return 0
        l, r = depth(node.left), depth(node.right)
        best = max(best, l + r)
        return 1 + max(l, r)

    depth(root)
    return best


def is_balanced(root):
    def check(node):  # returns height, or -1 if unbalanced
        if not node:
            return 0
        l, r = check(node.left), check(node.right)
        if l == -1 or r == -1 or abs(l - r) > 1:
            return -1
        return 1 + max(l, r)

    return check(root) != -1


def invert(root):
    if root:
        root.left, root.right = invert(root.right), invert(root.left)
    return root


def is_symmetric(root):
    def mirror(a, b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return mirror(a.left, b.right) and mirror(a.right, b.left)

    return mirror(root.left, root.right) if root else True


def lowest_common_ancestor(root, p, q):
    """LCA of values p and q in a general binary tree."""
    if not root or root.val in (p, q):
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right


def left_view(root):
    return [level[0] for level in level_order(root)]


def right_view(root):
    return [level[-1] for level in level_order(root)]


def build_from_pre_in(pre, ino):
    """Rebuild a tree from preorder + inorder lists (unique values)."""
    index = {v: i for i, v in enumerate(ino)}
    it = iter(pre)

    def helper(lo, hi):
        if lo > hi:
            return None
        val = next(it)
        node = TreeNode(val)
        mid = index[val]
        node.left = helper(lo, mid - 1)
        node.right = helper(mid + 1, hi)
        return node

    return helper(0, len(ino) - 1)


if __name__ == "__main__":
    #           1
    #         /   \
    #        2     3
    #       / \     \
    #      4   5     6
    root = build_tree([1, 2, 3, 4, 5, None, 6])

    print("----- Traversals -----")
    print("preorder :", preorder(root), "| iterative:", preorder_iterative(root))
    print("inorder  :", inorder(root), "| iterative:", inorder_iterative(root))
    print("postorder:", postorder(root), "| iterative:", postorder_iterative(root))
    print("level    :", level_order(root))

    print("\n----- Properties -----")
    print("height:", height(root), "| nodes:", count_nodes(root), "| leaves:", count_leaves(root))
    print("diameter:", diameter(root), "| balanced:", is_balanced(root))
    print("LCA(4, 5):", lowest_common_ancestor(root, 4, 5).val,
          "| LCA(4, 6):", lowest_common_ancestor(root, 4, 6).val)
    print("left view:", left_view(root), "| right view:", right_view(root))
    print("symmetric:", is_symmetric(root), "| symmetric([1,2,2,3,4,4,3]):",
          is_symmetric(build_tree([1, 2, 2, 3, 4, 4, 3])))

    rebuilt = build_from_pre_in(preorder(root), inorder(root))
    print("rebuilt from pre+in, level order:", level_order(rebuilt))
    print("inverted level order:", level_order(invert(root)))
