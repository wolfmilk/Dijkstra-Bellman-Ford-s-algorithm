from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = [] 
    def addEdge(self,u,v,w):
        self.graph.append([u, v, w])
    def printArr(self, dist):
        for i in range(self.V):
            if i==8:
               print("The Sortest Distance Between A and I by Using this Method is: %d" %  dist[i])
    def BellmanFord(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0
        for i in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
        for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        print ("Graph contains negative weight cycle")
                        return
        self.printArr(dist)
g = Graph(9)
g.addEdge(0,1, 22)
g.addEdge(0,2, 9)
g.addEdge(0,3, 12)
g.addEdge(1,2, 35)
g.addEdge(1,5, 36)
g.addEdge(1,7, 34)
g.addEdge(2,5, 42)
g.addEdge(2,4, 65)
g.addEdge(2,3, 4)
g.addEdge(3,4, 33)
g.addEdge(3,8, 30)
g.addEdge(4,5, 18)
g.addEdge(4,6, 23)
g.addEdge(5,7, 24)
g.addEdge(5,6, 39)
g.addEdge(6,7, 25)
g.addEdge(6,8, 21)
g.addEdge(7,8, 19)
g.BellmanFord(0)
print("The Path is A-D-I")
import timeit
print("The timeit for this program is: ",timeit.timeit("g.BellmanFord", globals=globals(), number=5))
