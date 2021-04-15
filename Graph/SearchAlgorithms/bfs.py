class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def bfs(start_node):
    queue = [start_node]
    start_node.visited = True
    while queue:
        current_node = queue.pop(0)
        print(current_node.name)
        for neighbour in current_node.adjacency_list:
            if not neighbour.visited:
                neighbour.visited = True
                queue.append(neighbour)


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjacency_list.append(node2)
node1.adjacency_list.append(node4)
node2.adjacency_list.append(node5)
node5.adjacency_list.append(node3)

bfs(node1)
