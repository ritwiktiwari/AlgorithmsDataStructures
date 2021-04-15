from sys import maxsize


class Vertex:
    def __init__(self, data) -> None:
        self.data = data
        self._adjacent = {}
        self._distance = maxsize
        self._visited = False
        self._previous = None

    @property
    def adjacent(self):
        return self._adjacent

    @adjacent.setter
    def adjacent(self, neighbour: "Vertex"):
        self._adjacent[neighbour] = 0

    def adjacent_with_weight(self, neighbour: "Vertex", weight):
        self._adjacent[neighbour] = weight

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, value: bool):
        self._visited = value

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, vertex: "Vertex"):
        self._previous = vertex

    def __str__(self):
        return f"{self.data}: {[(_.data, self.adjacent[_]) for _ in self.adjacent]}"


class Graph:
    """
    Things are incomplete here
    """
    def __init__(self):
        self._vertices = 0
        self._vertex_dictionary = {}

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, value: int):
        self._vertices = value

    @property
    def vertex_dictionary(self):
        return self._vertex_dictionary

    # @vertex_dictionary.setter
    # def vertex_dictionary(self, value: Vertex):
    #     self._vertex_dictionary.append(value)

    def add_vertex(self, data):
        self.vertices += 1
        new_vertex = Vertex(data)
        return new_vertex

    def add_edge(self, from_vertex, to_vertex, weight: int = 0):
        if self.add_vertex(from_vertex) not in self.vertex_dictionary:
            self.vertex_dictionary[self.add_vertex(from_vertex)] = [self.add_vertex(to_vertex)]

        from_vertex.adjacent_with_weight(to_vertex, weight)

    def __str__(self):
        g = ""
        print(self.vertex_dictionary)
        for i in self.vertex_dictionary:
            g = g + str(i) + "\n"
        return g


vertexA = Vertex("A")
vertexB = Vertex("B")
vertexC = Vertex("C")
vertexD = Vertex("D")

graph = Graph()
graph.add_edge(vertexA, vertexB, 1)
graph.add_edge(vertexA, vertexC, 4)
graph.add_edge(vertexC, vertexD, 3)
graph.add_edge(vertexD, vertexB, 12)
# graph.add_edge("A", "B", 1)
# graph.add_edge("A", "C", 4)
# graph.add_edge("C", "D", 3)
# graph.add_edge("D", "B", 12)
print(graph)

