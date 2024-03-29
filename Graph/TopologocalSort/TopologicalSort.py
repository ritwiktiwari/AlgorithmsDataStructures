from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def printer(self):
        print(self.graph)

    def dfs(self, start_node, visited, ordering):
        visited[start_node] = True
        for neighbour in self.graph[start_node]:
            if not visited[neighbour]:
                self.dfs(neighbour, visited, ordering)
        ordering.insert(0, start_node)

    def topological_sort(self):
        n = max(self.graph) + 1
        visited = [False] * n
        ordering = []
        for current_node in range(n):
            if not visited[current_node]:
                self.dfs(current_node, visited, ordering)
        return ordering

    def dfs_2(self, start_node, visited, ordering, i):
        visited[start_node] = True
        for neighbour in self.graph[start_node]:
            if not visited[neighbour]:
                i = self.dfs_2(neighbour, visited, ordering, i)
        ordering[i] = start_node
        return i - 1

    def topological_sort_2(self):
        n = max(self.graph) + 1
        visited = [False] * n
        ordering = [0] * n
        i = n - 1
        for current_node in range(n):
            if not visited[current_node]:
                i = self.dfs_2(current_node, visited, ordering, i)
        return ordering


g = Graph()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.printer()
print(g.topological_sort())
print(g.topological_sort_2())
