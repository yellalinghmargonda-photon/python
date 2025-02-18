
def networkDelayTime(times, n: int, k: int) -> int:
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))
    dist = {}  # The starting node has a distance of 0

    # Step 3: Min-heap for Dijkstra's algorithm
    min_heap = [(0, k)]  # (distance, node)
    while min_heap:
        current_time, node = heapq.heappop(min_heap)
        if node in dist:
            continue
        dist[node]=current_time
        for neighbor, time in graph[node]:
            if neighbor not in dist:
                heapq.heappush(min_heap, (current_time + time, neighbor))

    return max(dist.values()) if len(dist)==n else -1