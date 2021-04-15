from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, source):
        visited = [False] * (max(self.graph) + 1)
        queue = [source]
        visited[source] = True

        while len(queue) > 0:
            current_vertex = queue.pop(0)
            print(current_vertex, end=" ")
            for i in self.graph[current_vertex]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.bfs(2)
