from graph import Graph

"""
Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.
example:
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c
"""

"""
    def topological_sort(self):
        visited = set()
        stack = []
        for vertex in self.graph:
            if vertex not in visited:
                self._topological_sort(vertex, visited, stack)
        return stack
    def _topological_sort(self, vertex, visited, stack):
        visited.add(vertex)
        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self._topological_sort(neighbour, visited, stack)
        stack.insert(0, vertex)
"""

# Runtime: O(V + E) V is the number of vertices and E is the number of edges
def build_order(projects, dependencies):
    graph = Graph()
    for project in projects:
        graph.addVertex(project)
    for dependency in dependencies:
        graph.addEdge(dependency[0], dependency[1])
    return graph.topological_sort()


if __name__ == "__main__":
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    print(build_order(projects, dependencies))
