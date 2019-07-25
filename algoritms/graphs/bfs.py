#!/usr/bin/env python3

from graph import Graph, GraphNode


def bfs_search(root, value):
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
    nodeG = GraphNode('G')
    nodeR = GraphNode('R')
    nodeA = GraphNode('A')
    nodeP = GraphNode('P')
    nodeH = GraphNode('H')
    nodeS = GraphNode('S')

    graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] ) 
    graph1.add_edge(nodeG,nodeR)
    graph1.add_edge(nodeA,nodeR)
    graph1.add_edge(nodeA,nodeG)
    graph1.add_edge(nodeR,nodeP)
    graph1.add_edge(nodeH,nodeG)
    graph1.add_edge(nodeH,nodeP)
    graph1.add_edge(nodeS,nodeR)

    assert nodeA == bfs_search(nodeS, 'A')
    assert nodeS == bfs_search(nodeP, 'S')
    assert nodeR == bfs_search(nodeH, 'R')
