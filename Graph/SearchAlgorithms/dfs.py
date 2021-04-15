from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.visited.append(False)

    def dfs(self, source):
        if self.visited[source]:
            return
        self.visited[source] = True
        print(source, end=" ")
        neighbours = self.graph[source]
        for next_vertex in neighbours:
            self.dfs(next_vertex)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.dfs(2)
