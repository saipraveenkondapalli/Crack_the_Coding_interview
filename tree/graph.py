class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, s, d):
        try:  # if s is already in graph
            self.graph[s].append(d)
        except KeyError:  # if s is not in graph
            self.graph[s] = [d]  # add s to graph and add d to s's list
            self.graph[d] = []  # add destination vertex to the graph

    def add_vertex(self, v):
        self.graph[v] = []

    def print_graph(self):
        for x in self.graph:
            print(f"{x} -> {self.graph[x]}")

    def topological_sort(self):
        visited = set()
        stack = []
        for vertex in self.graph:
            if vertex not in visited:
                self._topological_sort(vertex, visited, stack)
        return stack[::-1]  # reverse the stack

    def _topological_sort(self, vertex, visited, stack):
        visited.add(vertex)
        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self._topological_sort(neighbour, visited, stack)
        stack.append(vertex)

    def bfs(self, s):
        visited = [False] * (len(self.graph))
        queue = [s]
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def _dfs_util(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self._dfs_util(neighbour, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def dfs(self, v):

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self._dfs_util(v, visited)

    # graph in a readable format
    def __str__(self):
        result = []
        for node, edges in self.graph.items():
            result.append(f"{node}: {', '.join(map(str, edges))}")
        return "\n".join(result)


if __name__ == "__main__":
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
    graph = Graph()
    for project in projects:
        graph.add_vertex(project)
    for dependency in dependencies:
        graph.add_edge(dependency[0], dependency[1])

    build_order = graph.topological_sort()
    print(build_order)
