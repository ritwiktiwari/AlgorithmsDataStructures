class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def dfs(start_node: Node):
    start_node.visited = True
    print(start_node.name)
    for neighbour in start_node.adjacency_list:
        if not neighbour.visited:
            dfs(neighbour)


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjacency_list.append(node2)
node1.adjacency_list.append(node4)
node2.adjacency_list.append(node5)
node5.adjacency_list.append(node3)

dfs(node1)
