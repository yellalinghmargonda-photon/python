import heapq

def minCostConnectPoints(points):
    n = len(points)
    # Adjacency list is not needed since we compute distances on the fly
    pq = [(0, 0)]  # (weight, node)
    visited = set()
    mst_weight = 0

    while len(visited) < n:
        weight, u = heapq.heappop(pq)
        if u in visited:
            continue  # Skip already visited nodes

        visited.add(u)
        mst_weight += weight  # Add edge weight to total MST cost

        # Add all unvisited neighbors to the priority queue
        for v in range(n):
            if v not in visited:
                distance = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                heapq.heappush(pq, (distance, v))

    return mst_weight

# Example Usage
points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
print(minCostConnectPoints(points))  # Output: Minimum MST Cost
