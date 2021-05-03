from collections import defaultdict
from sys import maxsize


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def bellman_ford(self, start):
        distance = [maxsize] * self.n
        distance[start] = 0

        for i in self.graph:
            for j in self.graph[i]:
                if distance[i] + j[1] < distance[j[0]]:
                    distance[j[0]] = distance[i] + j[1]

        for i in self.graph:
            for j in self.graph[i]:
                if distance[i] + j[1] < distance[j[0]]:
                    distance[j[0]] = -maxsize

        return distance


g = Graph(3)
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 1)
g.add_edge(1, 2, -3)

print(g.bellman_ford(0))
