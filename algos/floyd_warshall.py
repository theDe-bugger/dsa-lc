def floyd_warshall(graph):
    # Number of vertices in the graph
    vertices = list(graph.keys())
    num_vertices = len(vertices)

    # Map vertices to integers for indexing the distance matrix
    vertex_index = {vertex: i for i, vertex in enumerate(vertices)}

    # Initialize distance matrix from the graph
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    for vertex, edges in graph.items():
        for neighbor, weight in edges.items():
            i, j = vertex_index[vertex], vertex_index[neighbor]
            dist[i][j] = weight
    for i in range(num_vertices):
        dist[i][i] = 0  # Distance to self is zero

    # Floyd-Warshall algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Construct result: Convert distances back to dictionary format
    result = {v: {} for v in vertices}
    for i in range(num_vertices):
        for j in range(num_vertices):
            if dist[i][j] != float('inf'):
                result[vertices[i]][vertices[j]] = dist[i][j]

    return result

# Overall time complexity: O(V^3)

# Example usage
graph = {
    'A': {'B': 3, 'C': 8, 'E': -4},
    'B': {'D': 1, 'E': 7},
    'C': {'B': 4},
    'D': {'A': 2, 'C': -5},
    'E': {'D': 6}
}

shortest_paths = floyd_warshall(graph)

print("Shortest path distances:")
for start, distances in shortest_paths.items():
    print(f"From {start}:")
    for end, distance in distances.items():
        print(f"  to {end} = {distance}")
