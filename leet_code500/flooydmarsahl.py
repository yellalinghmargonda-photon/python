def floyd_warshall_negative_cycle(graph, V):
    """
    Floyd-Warshall Algorithm to detect negative cycles.

    Parameters:
    - graph: A 2D list (adjacency matrix) with edge weights. INF if no direct edge.
    - V: Number of vertices.

    Returns:
    - True if a negative cycle is found, else False.
    """
    INF = float('inf')

    # Initialize distance matrix
    dist = [[INF] * V for _ in range(V)]

    # Set initial distances from graph
    for u in range(V):
        dist[u][u] = 0  # Distance to itself is 0
        for v, weight in graph[u]:
            dist[u][v] = weight

    # Floyd-Warshall Algorithm
    for k in range(V):  # Intermediate nodes
        for i in range(V):  # Source
            for j in range(V):  # Destination
                if dist[i][k] < INF and dist[k][j] < INF:  # Prevent overflow issues
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Check for negative cycle (diagonal elements must not be negative)
    for i in range(V):
        if dist[i][i] < 0:
            return True  # Negative cycle found

    return False  # No negative cycle


# Example Graph
V = 4
graph_with_cycle = {
    0: [(1, 1)],
    1: [(2, -1)],
    2: [(3, -1)],
    3: [(0, -1)]  # Forms a negative cycle
}

graph_without_cycle = {
    0: [(1, 4)],
    1: [(2, 3)],
    2: [(3, 2)],
    3: [(0, 1)]
}

print("Graph with negative cycle:", floyd_warshall_negative_cycle(graph_with_cycle, V))  # True
print("Graph without negative cycle:", floyd_warshall_negative_cycle(graph_without_cycle, V))  # False
