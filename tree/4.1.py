from graph import Graph


def check_whether_route_exists(graph, source, destination):
    visted = [False] * (len(graph)+1)
    queue = []
    queue.append(source)
    visted[source] = True
    ans = []
    while queue:
        s = queue.pop(0)
        ans.append(s)
        for i in graph[s]:
            if visted[i] == False:
                if i == destination:
                    return True
                queue.append(i)
                visted[i] = True
    return False






if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2,3)
    g.addEdge(4, 2)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    print(check_whether_route_exists(g.graph, 6, 0))
