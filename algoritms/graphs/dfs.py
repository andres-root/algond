#!/usr/bin/env python3

from graph import Graph, GraphNode


def dfs_search(root, value):
    visited = []
    stack = [root]

    while len(stack) > 0:
        print(visited)
        current_node = stack.pop()
        visited.append(current_node)

        if current_node.value == value:
            return current_node
        
        for child in current_node.children:
            if child not in visited:
                stack.append(child)


if __name__ == '__main__':
    nodeG = GraphNode('G')
    nodeR = GraphNode('R')
    nodeA = GraphNode('A')
    nodeP = GraphNode('P')
    nodeH = GraphNode('H')
    nodeS = GraphNode('S')

    graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA]) 
    graph1.add_edge(nodeG, nodeR)
    graph1.add_edge(nodeA, nodeR)
    graph1.add_edge(nodeA, nodeG)
    graph1.add_edge(nodeR, nodeP)
    graph1.add_edge(nodeH, nodeG)
    graph1.add_edge(nodeH, nodeP)
    graph1.add_edge(nodeS, nodeR)

    assert nodeA == dfs_search(nodeS, 'A')
    assert nodeS == dfs_search(nodeP, 'S')
    assert nodeR == dfs_search(nodeH, 'R')
