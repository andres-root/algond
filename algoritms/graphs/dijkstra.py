#!/usr/bin/env python3


class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)


def dijkstra(start_node, end_node):
    visited = []
    queue = [root]
    
    while len(queue) > 0:
        current_node = queue.pop(0)
        visited.append(current_node)

        if current_node.value == value:
            return current_node

        for child in current_node.children:
            if child not in visited:
                queue.append(child)


if __name__ == '__main__':
    node_u = GraphNode('U')
    node_d = GraphNode('D')
    node_a = GraphNode('A')
    node_c = GraphNode('C')
    node_i = GraphNode('I')
    node_t = GraphNode('T')
    node_y = GraphNode('Y')

    graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])
    graph.add_edge(node_u, node_a, 4)
    graph.add_edge(node_u, node_c, 6)
    graph.add_edge(node_u, node_d, 3)
    graph.add_edge(node_d, node_u, 3)
    graph.add_edge(node_d, node_c, 4)
    graph.add_edge(node_a, node_u, 4)
    graph.add_edge(node_a, node_i, 7)
    graph.add_edge(node_c, node_d, 4)
    graph.add_edge(node_c, node_u, 6)
    graph.add_edge(node_c, node_i, 4)
    graph.add_edge(node_c, node_t, 5)
    graph.add_edge(node_i, node_a, 7)
    graph.add_edge(node_i, node_c, 4)
    graph.add_edge(node_i, node_y, 4)
    graph.add_edge(node_t, node_c, 5)
    graph.add_edge(node_t, node_y, 5)
    graph.add_edge(node_y, node_i, 4)
    graph.add_edge(node_y, node_t, 5)


    print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra(node_u, node_y)))
