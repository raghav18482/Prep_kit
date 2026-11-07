# =====================================================================
#              DISJOINT SET UNION (UNION-FIND) - REVISION NOTES
# =====================================================================
#
# WHAT IS IT?
#   - Keeps track of elements split into NON-OVERLAPPING groups (sets).
#   - Each set is a tree; the ROOT of the tree is the set's
#     representative ("leader").
#   - Stored in a `parent` array: parent[x] = x means x is a root.
#
# OPERATIONS
#   - find(x)     : return the root of x's set.
#   - union(x, y) : merge the sets containing x and y.
#   - connected(x, y) : find(x) == find(y).
#
# OPTIMIZATIONS (use BOTH)
#   1. Path compression (in find): make every node on the path point
#      directly to the root, so later finds are almost instant.
#   2. Union by rank / size: attach the SMALLER (shorter) tree under the
#      root of the bigger one, so trees stay flat.
#
# TIME COMPLEXITY
#   +------------------------------------+---------------------+
#   | Version                            | find / union        |
#   +------------------------------------+---------------------+
#   | Naive                              | O(n) worst          |
#   | Only union by rank or compression  | O(log n)            |
#   | Both optimizations                 | O(alpha(n)) ~ O(1)  |
#   +------------------------------------+---------------------+
#   alpha(n) = inverse Ackermann function, < 5 for any practical n.
#   Space: O(n)
#
# APPLICATIONS / INTERVIEW PATTERNS
#   - Kruskal's minimum spanning tree (sort edges, union if not connected).
#   - Detect a cycle in an UNDIRECTED graph (edge between two nodes
#     already in the same set -> cycle).
#   - Number of connected components / provinces / islands II.
#   - Redundant connection, accounts merge, satisfiability of equations.
#   - Dynamic connectivity (networks, social groups, image segmentation).
#
# QUICK TIPS
#   - Union-Find only MERGES; it cannot split sets apart efficiently.
#   - Track the number of components: start at n, decrement on every
#     successful union.
# =====================================================================


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  # each element is its own root
        self.rank = [0] * n           # upper bound on tree height
        self.size = [1] * n           # number of elements in each root's set
        self.components = n

    def find(self, x):
        """Find root with path compression (iterative, two passes)."""
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:   # point every node on the path at root
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, x, y):
        """Union by rank. Returns False if x and y were already connected."""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx               # make rx the taller tree
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.components -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def set_size(self, x):
        return self.size[self.find(x)]

    def groups(self):
        out = {}
        for x in range(len(self.parent)):
            out.setdefault(self.find(x), []).append(x)
        return list(out.values())


def kruskal_mst(n, edges):
    """edges = [(weight, u, v), ...]. Returns (mst_edges, total_weight)."""
    dsu = DisjointSet(n)
    mst, total = [], 0
    for w, u, v in sorted(edges):
        if dsu.union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == n - 1:
                break
    return mst, total


def has_cycle_undirected(n, edges):
    dsu = DisjointSet(n)
    for u, v in edges:
        if not dsu.union(u, v):  # already connected -> this edge closes a cycle
            return True
    return False


if __name__ == "__main__":
    print("----- Disjoint Set -----")
    ds = DisjointSet(7)
    for a, b in [(0, 1), (1, 2), (3, 4), (5, 6), (4, 6)]:
        ds.union(a, b)
    print("groups:", ds.groups(), "| components:", ds.components)
    print("connected(0, 2):", ds.connected(0, 2), "| connected(0, 3):", ds.connected(0, 3))
    print("size of set containing 3:", ds.set_size(3))

    print("\n----- Kruskal MST -----")
    edges = [(1, 0, 1), (3, 0, 2), (2, 1, 2), (4, 1, 3), (5, 2, 3)]
    print(kruskal_mst(4, edges))

    print("\n----- Cycle detection -----")
    print("edges (0-1, 1-2, 2-0):", has_cycle_undirected(3, [(0, 1), (1, 2), (2, 0)]))
    print("edges (0-1, 1-2):     ", has_cycle_undirected(3, [(0, 1), (1, 2)]))
