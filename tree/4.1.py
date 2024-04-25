from graph import Graph

"""
For a given directed graph, design an algorithm to find out whether a route exists between two nodes.
"""


def check_whether_route_exists(graph, source, destination):
    visited = set()
    queue = [source]
    visited.add(source)
    ans = []  # acts as queue for BFS
    while queue:
        s = queue.pop(0)
        ans.append(s)
        for i in graph[s]:
            if i not in visited:
                if i == destination:
                    return True
                queue.append(i)
                visited.add(i)
    return False


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(4, 2)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
