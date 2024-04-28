#DFS


class Graph:
    def __init__(self):
        self.graph = dict()
       
    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
   
    def DFS(self, visited, v):
        visited.add(v)
        print(v, end=" ")
       
        for node in self.graph[v]:
            if node not in visited:
                self.DFS(visited, node)
   
if __name__== "__main__":
    visited = set()
    g = Graph()
    edges = int(input("Enter no. of edges: "))
    while edges > 0:
        edge = input("Enter an edge (format: u v): ")
        u, v = map(int, edge.split())  
        g.addEdge(u, v)
        edges -= 1
   
    start_vertex = int(input("Enter the starting vertex for DFS traversal: "))
    print("Path:", end=" ")
    g.DFS(visited, start_vertex)

Output:
Enter no. of edges: 4
Enter an edge (format: u v): 0 2
Enter an edge (format: u v): 2 4
Enter an edge (format: u v): 0 1
Enter an edge (format: u v): 0 3
Enter the starting vertex for DFS traversal: 0
Path: 0 2 4 1 3 
