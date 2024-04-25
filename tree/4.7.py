"""
Build Order:
You are given a list of projects and a list of dependencies (which is a list of pairs of projects,
where the second project is dependent on the first project).
All of a project's dependencies must be built before the project is.
Find a build order that will allow the projects to be built.
If there is no valid build order, return an error.

example:
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c
"""

"""
Refer topological sort in graph.py
"""

from graph import Graph


def build_graph(projects, dependencies):
    graph = Graph()
    for project in projects:
        graph.add_vertex(project)
    for dependency in dependencies:
        graph.add_edge(dependency[0], dependency[1])
    return graph


def build_order(projects: list, dependencies:list) -> list:
    graph = build_graph(projects, dependencies)
    return graph.topological_sort()


if __name__ == "__main__":
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
    print(build_order(projects, dependencies))

