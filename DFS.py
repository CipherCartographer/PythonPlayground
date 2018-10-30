from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def dfs_util(self, v, visited):
        visited[v] = True
        print v,

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_util(i, visited)

    def dfs(self, v):
        visited = [False] * (len(self.graph))
        self.dfs_util(v, visited)


def main():
    print "DFS in Python"
    g = Graph()
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3)

    print "Graph starting vertex 2 :"

    g.dfs(2)

if __name__ == "__main__":
    main()
