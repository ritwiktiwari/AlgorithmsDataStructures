import heapq
import sys


class Node:
    def __init__(self, name: str):
        self.name = name
        self.predecessor = None
        self.adjacency_list = []
        self.minimum_distance = sys.maxsize

    # def __cmp__(self, other: "Node"):
    #     return self.__cmp__(self.minimum_distance, other.minimum_distance)

    def __lt__(self, other: "Node"):
        return self.minimum_distance < other.minimum_distance


class Edge:
    def __init__(self, weight: int, start_vertex: Node, end_vertex: Node):
        self.weight = weight
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex


class Dijkstra:
    def calculate_shortest_path(self, start_vertex: Node):
        """
        Find predecessors and minimum distance with respect to the starting vertex
        """
        q = []
        start_vertex.minimum_distance = 0
        heapq.heappush(q, start_vertex)

        while len(q) > 0:
            current_vertex = heapq.heappop(q)
            for edge in current_vertex.adjacency_list:
                u = edge.start_vertex
                v = edge.end_vertex
                new_distance = u.minimum_distance + edge.weight

                if new_distance < v.minimum_distance:
                    v.predecessor = u
                    v.minimum_distance = new_distance
                    heapq.heappush(q, v)

    def get_shortest_path(self, target_vertex: Node):
        if target_vertex.predecessor is None:
            print(target_vertex.name)
            return
        else:
            print(target_vertex.name)
            return self.get_shortest_path(target_vertex.predecessor)


nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")


edge1_AB = Edge(5, nodeA, nodeB)
edge2_AH = Edge(8, nodeA, nodeH)
edge3_AE = Edge(9, nodeA, nodeE)
edge4_BD = Edge(15, nodeB, nodeD)
edge5_BC = Edge(12, nodeB, nodeC)
edge6_BH = Edge(4, nodeB, nodeH)
edge7_HC = Edge(7, nodeH, nodeC)
edge8_HF = Edge(6, nodeH, nodeF)
edge9_EH = Edge(5, nodeE, nodeH)
edge10_EF = Edge(4, nodeE, nodeF)
edge11_EG = Edge(20, nodeE, nodeG)
edge12_FC = Edge(1, nodeF, nodeC)
edge13_FG = Edge(13, nodeF, nodeG)
edge14_CD = Edge(3, nodeC, nodeD)
edge15_CG = Edge(11, nodeC, nodeG)
edge16_DG = Edge(9, nodeD, nodeG)


nodeA.adjacency_list.extend([edge1_AB, edge2_AH, edge3_AE])
nodeB.adjacency_list.extend([edge4_BD, edge5_BC, edge6_BH])
nodeC.adjacency_list.extend([edge14_CD, edge15_CG])
nodeD.adjacency_list.append(edge16_DG)
nodeE.adjacency_list.extend([edge9_EH, edge10_EF, edge11_EG])
nodeF.adjacency_list.extend([edge12_FC, edge13_FG])
# nodeG.adjacency_list
nodeH.adjacency_list.extend([edge7_HC, edge8_HF])

algo = Dijkstra()
algo.calculate_shortest_path(start_vertex=nodeA)
algo.get_shortest_path(nodeG)
