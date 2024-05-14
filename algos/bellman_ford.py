class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printArr(self, dist, pred):
        print("Vertex\tDistance from Source\tPath")
        for i in range(self.V):
            if i != src:  # Assuming src is globally known for simplicity
                print("%d \t\t %d \t\t\t" % (i, dist[i]), end='')
                self.printPath(pred, i)
                print()

    def printPath(self, pred, j):
        """Function to print path from source to j using predecessor array"""
        if pred[j] is None:
            print(src, end='')
            return
        # Recursive call to print the path
        self.printPath(pred, pred[j])
        print(f' -> {j}', end='')

    def bellman_ford(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        pred = [None] * self.V  # Predecessor array

        # run relaxation V-1 times to find shortest path
        for _ in range(self.V - 1):
            # for each edge u-v with weight w in self.graph relax the edge
            for u, v, w in self.graph:
                # If the distance to the destination is shorter by going through u, update the distance
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    pred[v] = u

        # Check for negative weight cycles
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return None

        self.printArr(dist, pred)
        return dist, pred

# Overall time complexity: O(V*E)

g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
src = 0  # Define source vertex
g.bellman_ford(src)



# g = Graph(4)
# g.addEdge(0, 2, 10)
# g.addEdge(0, 1, 6)
# g.addEdge(1, 2, 7)
# g.addEdge(2, 3, 8)
# src = 0  # Define source vertex
# g.bellman_ford(src)
