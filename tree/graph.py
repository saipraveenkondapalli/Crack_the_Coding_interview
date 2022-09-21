class Graph:
    def __init__(self):
        self.graph = {}
    
    def addEdge(self, s,d):
        try:  # if s is already in graph
            self.graph[s].append(d)
        except KeyError: # if s is not in graph
            self.graph[s] = [d] # add s to graph and add d to s's list
            self.graph[d] = [] # add destination vertex to the graph

    def addVertex(self, v):
        self.graph[v] = []

    def printGraph(self):
        for x in self.graph:
            print(f"{x} -> {self.graph[x]}")

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


    def BFS(self,s):
        visted = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visted[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end = " ")

            for i in self.graph[s]:
                if visted[i] == False:
                    queue.append(i)
                    visted[i] = True

    def _DFSUtil(self, v, visited):
 
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')
 
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self._DFSUtil(neighbour, visited)
 
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
 
        # Create a set to store visited vertices
        visited = set()
 
        # Call the recursive helper function
        # to print DFS traversal
        self._DFSUtil(v, visited)
    
    






