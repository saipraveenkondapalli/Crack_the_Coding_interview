class Graph:
    def __init__(self):
        self.graph = {}
    
    def addEdge(self, s,d):
        try:
            self.graph[s].append(d)
        except KeyError:
            self.graph[s] = [d]

    def printGraph(self):
        for x in self.graph:
            print(f"{x} -> {self.graph[x]}")
    
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
    
    










g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


g.printGraph()
g.DFS(2)

