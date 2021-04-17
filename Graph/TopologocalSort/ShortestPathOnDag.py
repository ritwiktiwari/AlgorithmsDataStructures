from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = 0

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.vertices += 1

    def printer(self):
        print(f"U\tV\tW")
        print(f"-" * 10)
        for i in range(self.vertices):
            for j in self.graph[i]:
                print(f"{i}\t{j[0]}\t{j[1]}")
        print(f"-" * 10)

    def dfs(self, start_node, visited, ordering):
        visited[start_node] = True
        neighbours = self.graph[start_node]
        for i in neighbours:
            if not visited[i[0]]:
                self.dfs(i[0], visited, ordering)
        ordering.insert(0, start_node)

    def topological_sort(self):
        visited = [False] * self.vertices
        ordering = []

        for current_node in range(self.vertices):
            if not visited[current_node]:
                self.dfs(current_node, visited, ordering)
        return ordering

    def dag_shortest_path(self, start):
        from sys import maxsize

        top_sort = self.topological_sort()
        distance = [maxsize] * self.vertices

        distance[start] = 0

        for i in range(self.vertices):
            current_node = top_sort[i]
            adjacent_edges = self.graph[current_node]
            for edge in adjacent_edges:
                new_distance = distance[current_node] + edge[1]
                distance[edge[0]] = min(new_distance, distance[edge[0]])

        return distance


g = Graph()
g.add_edge(0, 1, 3)
g.add_edge(1, 2, 2)
g.add_edge(0, 3, 1)
g.add_edge(3, 2, 11)

g.printer()
print(g.dag_shortest_path(0))
