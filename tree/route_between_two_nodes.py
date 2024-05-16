"""
For a given directed graph, design an algorithm to find out whether a route exists between two nodes.
"""
from collections import deque


def check_whether_route_exists(graph, source, destination) -> bool:
    """
    Check whether a route exists between two nodes in a graph.
    Args:
        graph: Graph object
        source: int representing the source node
        destination: int representing the destination node

    Returns:
        bool: True if a route exists between the two nodes, False otherwise
    """
    visited: set = set()
    queue: deque = deque()
    queue.append(source)
    visited.add(source)
    while queue:
        cur = queue.popleft()
        for neighbour in graph[cur]:
            if neighbour not in visited:
                if cur == destination:
                    return True
                queue.append(neighbour)
                visited.add(neighbour)

    return False
