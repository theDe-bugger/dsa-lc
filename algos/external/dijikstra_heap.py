import heapq

def dijkstra_heap(graph, start):
    # Initialize distances and a priority queue
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # heap of (distance, node)

    while priority_queue:
        # Extract the node with the smallest distance
        current_distance, min_node = heapq.heappop(priority_queue)

        # If a node's distance is updated in the heap, it might be popped later again with a larger distance, skip it
        if current_distance > distances[min_node]:
            continue

        # Update distances of adjacent nodes
        for neighbor, weight in graph[min_node].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances

# Overall time complexity: O((V+E)logV)



# Example usage
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 6},
    'D': {'B': 3, 'C': 6}
}

start_node = 'A'
distances = dijkstra_heap(graph, start_node)

print("Shortest distances from node", start_node)
for node, distance in distances.items():
    print(node, ":", distance)
