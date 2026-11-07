# =====================================================================
#                          GRAPH - REVISION NOTES
# =====================================================================
#
# WHAT IS A GRAPH?
#   - A set of VERTICES (nodes) V connected by EDGES E.  G = (V, E)
#   - Trees and linked lists are special kinds of graphs.
#
# TYPES
#   - Directed (edges have a direction, u -> v) vs Undirected (u - v).
#   - Weighted (edges have costs) vs Unweighted.
#   - Cyclic vs Acyclic. DAG = Directed Acyclic Graph.
#   - Connected: a path exists between every pair of vertices.
#   - Dense (E close to V^2) vs Sparse (E close to V).
#
# TERMS
#   - Degree: number of edges at a vertex. Directed graphs have
#     in-degree and out-degree.
#   - Path, cycle, connected component, self-loop, bipartite graph.
#   - Max edges: undirected V(V-1)/2, directed V(V-1).
#
# REPRESENTATIONS
#   +----------------------+-----------+----------------+-------------+
#   |                      | Space     | Check edge u-v | Neighbours  |
#   +----------------------+-----------+----------------+-------------+
#   | Adjacency matrix     | O(V^2)    | O(1)           | O(V)        |
#   | Adjacency list       | O(V + E)  | O(deg(u))      | O(deg(u))   |
#   | Edge list            | O(E)      | O(E)           | O(E)        |
#   +----------------------+-----------+----------------+-------------+
#   - Adjacency LIST is the default choice (most graphs are sparse).
#   - Matrix is good for dense graphs or quick edge checks.
#
# TRAVERSALS: O(V + E) with an adjacency list
#   - BFS (queue): explores level by level. Gives the SHORTEST PATH in an
#     UNWEIGHTED graph.
#   - DFS (recursion / stack): goes deep first. Used for cycle detection,
#     topological sort, connected components, path finding.
#   - Always keep a `visited` set, or cycles cause infinite loops.
#
# KEY ALGORITHMS
#   +---------------------------+----------------------------+---------------------+
#   | Problem                   | Algorithm                  | Time                |
#   +---------------------------+----------------------------+---------------------+
#   | Shortest path, unweighted | BFS                        | O(V + E)            |
#   | Shortest path, weights>=0 | Dijkstra (min-heap)        | O((V + E) log V)    |
#   | Shortest path, neg weights| Bellman-Ford               | O(V * E)            |
#   | All-pairs shortest path   | Floyd-Warshall             | O(V^3)              |
#   | Minimum spanning tree     | Prim (heap) / Kruskal (DSU)| O(E log V)          |
#   | Ordering of a DAG         | Topological sort (Kahn/DFS)| O(V + E)            |
#   | Cycle detection           | DFS colors / DSU / Kahn    | O(V + E)            |
#   | Connected components      | BFS / DFS / DSU            | O(V + E)            |
#   | Bipartite check           | BFS/DFS 2-coloring         | O(V + E)            |
#   +---------------------------+----------------------------+---------------------+
#   - Bellman-Ford can also DETECT negative cycles.
#   - Spanning tree of V vertices has exactly V - 1 edges.
#
# CYCLE DETECTION
#   - Undirected: during DFS, a visited neighbour that is not the parent
#     means a cycle. (Or Union-Find: both ends already in the same set.)
#   - Directed: DFS with 3 colors (white = unvisited, gray = on the
#     current path, black = done). Reaching a GRAY node -> cycle.
#     (Or Kahn's algorithm: if not all nodes are processed -> cycle.)
#
# COMMON INTERVIEW PATTERNS
#   - Number of islands / flood fill (grid = implicit graph).
#   - Course schedule (topological sort / cycle in a directed graph).
#   - Clone a graph, word ladder (BFS), rotting oranges (multi-source BFS).
#   - Network delay time / cheapest flights (Dijkstra / Bellman-Ford).
#   - Redundant connection, accounts merge (Union-Find).
#
# QUICK TIPS
#   - A grid problem is a graph: each cell is a node, 4 neighbours.
#   - "Minimum steps" -> BFS. "Dependencies / order" -> topological sort.
#   - "Weighted shortest path" -> Dijkstra. "Connect all, min cost" -> MST.
# =====================================================================

import heapq
from collections import defaultdict, deque


class Graph:
    """Adjacency-list graph. Works for directed/undirected, weighted/unweighted."""

    def __init__(self, directed=False):
        self.directed = directed
        self.adj = defaultdict(list)  # u -> [(v, weight), ...]

    def add_vertex(self, u):
        self.adj[u]  # touching the defaultdict creates the entry

    def add_edge(self, u, v, weight=1):
        self.adj[u].append((v, weight))
        if self.directed:
            self.adj[v]  # make sure v exists as a vertex
        else:
            self.adj[v].append((u, weight))

    def remove_edge(self, u, v):
        self.adj[u] = [(x, w) for x, w in self.adj[u] if x != v]
        if not self.directed:
            self.adj[v] = [(x, w) for x, w in self.adj[v] if x != u]

    def vertices(self):
        return list(self.adj.keys())

    def neighbours(self, u):
        return [v for v, _ in self.adj[u]]

    def __repr__(self):
        lines = [f"  {u} -> {self.neighbours(u)}" for u in self.adj]
        return "Graph(\n" + "\n".join(lines) + "\n)"

    # ---------------- traversals ----------------
    def bfs(self, start):
        visited, order = {start}, []
        q = deque([start])
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.neighbours(u):
                if v not in visited:
                    visited.add(v)  # mark when ENQUEUED, not when dequeued
                    q.append(v)
        return order

    def dfs(self, start):
        visited, order = set(), []

        def _dfs(u):
            visited.add(u)
            order.append(u)
            for v in self.neighbours(u):
                if v not in visited:
                    _dfs(v)

        _dfs(start)
        return order

    def dfs_iterative(self, start):
        visited, order, stack = set(), [], [start]
        while stack:
            u = stack.pop()
            if u in visited:
                continue
            visited.add(u)
            order.append(u)
            for v in reversed(self.neighbours(u)):  # keep same order as recursion
                if v not in visited:
                    stack.append(v)
        return order

    # ---------------- shortest paths ----------------
    def shortest_path_unweighted(self, start, end):
        parent = {start: None}
        q = deque([start])
        while q:
            u = q.popleft()
            if u == end:
                path = []
                while u is not None:
                    path.append(u)
                    u = parent[u]
                return path[::-1]
            for v in self.neighbours(u):
                if v not in parent:
                    parent[v] = u
                    q.append(v)
        return None

    def dijkstra(self, start):
        dist = {u: float("inf") for u in self.adj}
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:  # stale entry, already found something better
                continue
            for v, w in self.adj[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
        return dist

    def bellman_ford(self, start):
        """Returns distances, or None if a negative cycle is reachable."""
        dist = {u: float("inf") for u in self.adj}
        dist[start] = 0
        edges = [(u, v, w) for u in self.adj for v, w in self.adj[u]]
        for _ in range(len(self.adj) - 1):  # relax all edges V-1 times
            for u, v, w in edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in edges:  # one more pass -> still improving = neg cycle
            if dist[u] + w < dist[v]:
                return None
        return dist

    # ---------------- structure ----------------
    def connected_components(self):
        """For undirected graphs."""
        visited, components = set(), []
        for u in self.adj:
            if u not in visited:
                comp, q = [], deque([u])
                visited.add(u)
                while q:
                    x = q.popleft()
                    comp.append(x)
                    for v in self.neighbours(x):
                        if v not in visited:
                            visited.add(v)
                            q.append(v)
                components.append(comp)
        return components

    def has_cycle(self):
        if self.directed:
            WHITE, GRAY, BLACK = 0, 1, 2
            color = {u: WHITE for u in self.adj}

            def _dfs(u):
                color[u] = GRAY
                for v in self.neighbours(u):
                    if color[v] == GRAY:
                        return True
                    if color[v] == WHITE and _dfs(v):
                        return True
                color[u] = BLACK
                return False

            return any(color[u] == WHITE and _dfs(u) for u in list(self.adj))

        visited = set()

        def _dfs_undirected(u, parent):
            visited.add(u)
            for v in self.neighbours(u):
                if v not in visited:
                    if _dfs_undirected(v, u):
                        return True
                elif v != parent:
                    return True
            return False

        return any(u not in visited and _dfs_undirected(u, None) for u in list(self.adj))

    def topological_sort(self):
        """Kahn's algorithm (BFS on in-degrees). Returns None if there is a cycle."""
        indegree = {u: 0 for u in self.adj}
        for u in self.adj:
            for v in self.neighbours(u):
                indegree[v] += 1
        q = deque(u for u in self.adj if indegree[u] == 0)
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.neighbours(u):
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return order if len(order) == len(self.adj) else None

    def is_bipartite(self):
        color = {}
        for s in self.adj:
            if s in color:
                continue
            color[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for v in self.neighbours(u):
                    if v not in color:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return False
        return True

    def prim_mst(self):
        """Minimum spanning tree for a connected undirected weighted graph."""
        start = next(iter(self.adj))
        visited, mst, total = {start}, [], 0
        pq = [(w, start, v) for v, w in self.adj[start]]
        heapq.heapify(pq)
        while pq and len(visited) < len(self.adj):
            w, u, v = heapq.heappop(pq)
            if v in visited:
                continue
            visited.add(v)
            mst.append((u, v, w))
            total += w
            for nxt, nw in self.adj[v]:
                if nxt not in visited:
                    heapq.heappush(pq, (nw, v, nxt))
        return mst, total


def adjacency_matrix(n, edges, directed=False):
    """Matrix representation for vertices 0..n-1."""
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        matrix[u][v] = 1
        if not directed:
            matrix[v][u] = 1
    return matrix


def count_islands(grid):
    """Grid as an implicit graph: count groups of connected '1's."""
    rows, cols = len(grid), len(grid[0])
    seen, islands = set(), 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in seen:
                islands += 1
                stack = [(r, c)]
                seen.add((r, c))
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if (0 <= nx < rows and 0 <= ny < cols and
                                grid[nx][ny] == "1" and (nx, ny) not in seen):
                            seen.add((nx, ny))
                            stack.append((nx, ny))
    return islands


if __name__ == "__main__":
    print("----- Undirected graph -----")
    #   0 --- 1 --- 3
    #   |     |
    #   2 ----+     4 --- 5
    g = Graph()
    for u, v in [(0, 1), (0, 2), (1, 2), (1, 3), (4, 5)]:
        g.add_edge(u, v)
    print(g)
    print("BFS from 0:", g.bfs(0))
    print("DFS from 0:", g.dfs(0), "| iterative:", g.dfs_iterative(0))
    print("shortest path 0 -> 3:", g.shortest_path_unweighted(0, 3))
    print("components:", g.connected_components())
    print("has cycle:", g.has_cycle(), "| bipartite:", g.is_bipartite())
    print("adjacency matrix (0-3):", adjacency_matrix(4, [(0, 1), (0, 2), (1, 2), (1, 3)]))

    print("\n----- Directed acyclic graph (course schedule) -----")
    dag = Graph(directed=True)
    for u, v in [("math", "physics"), ("math", "cs"), ("physics", "robotics"), ("cs", "robotics")]:
        dag.add_edge(u, v)
    print("topological order:", dag.topological_sort())
    print("has cycle:", dag.has_cycle())
    dag.add_edge("robotics", "math")
    print("after adding robotics -> math, has cycle:", dag.has_cycle(),
          "| topo sort:", dag.topological_sort())

    print("\n----- Weighted graph -----")
    wg = Graph()
    for u, v, w in [("A", "B", 4), ("A", "C", 1), ("C", "B", 2), ("B", "D", 1), ("C", "D", 5)]:
        wg.add_edge(u, v, w)
    print("dijkstra from A:", wg.dijkstra("A"))
    print("bellman_ford from A:", wg.bellman_ford("A"))
    print("prim MST:", wg.prim_mst())

    neg = Graph(directed=True)
    for u, v, w in [(0, 1, 1), (1, 2, -3), (2, 0, 1)]:
        neg.add_edge(u, v, w)
    print("bellman_ford with negative cycle:", neg.bellman_ford(0))

    print("\n----- Grid as a graph -----")
    grid = [["1", "1", "0", "0"],
            ["1", "0", "0", "1"],
            ["0", "0", "1", "1"]]
    print("number of islands:", count_islands(grid))
