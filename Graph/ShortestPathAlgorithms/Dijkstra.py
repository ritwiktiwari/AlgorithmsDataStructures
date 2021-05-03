import heapq
from collections import defaultdict
from sys import maxsize


class Graph:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.n = n

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def printer(self):
        print(f"U\tV\tW")
        print(f"-" * 10)
        n = max(self.graph) + 1
        for i in range(n):
            for j in self.graph[i]:
                print(f"{i}\t{j[0]}\t{j[1]}")
        print(f"-" * 10)

    def dijkstra(self, start, end):
        visited = [False] * self.n
        previous = [None] * self.n
        distance = [maxsize] * self.n

        distance[start] = 0
        q = []
        heapq.heappush(q, (start, 0))

        while len(q) != 0:
            index, min_value = heapq.heappop(q)
            visited[index] = True
            if distance[index] < min_value:
                continue
            for edge in self.graph[index]:
                if visited[edge[0]]:
                    continue
                new_distance = distance[index] + edge[1]
                if new_distance < distance[edge[0]]:
                    distance[edge[0]] = new_distance
                    previous[edge[0]] = index
                    try:
                        heapq.heapreplace(q, (edge[0], new_distance))
                    except IndexError:
                        heapq.heappush(q, (edge[0], new_distance))
            if index == end:
                return distance, previous
        return distance, previous

    def find_shortest_path(self, start, end):
        distance, previous = self.dijkstra(start, end)
        path = []
        if distance[end] == maxsize:
            return path
        at = end
        while at is not None:
            path.append(at)
            at = previous[at]

        return list(reversed(path))


g = Graph(3)
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 2)
g.add_edge(1, 2, 3)

g.printer()
print(g.find_shortest_path(0, 2))
