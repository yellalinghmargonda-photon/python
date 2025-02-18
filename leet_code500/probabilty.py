import heapq


def maxProbability(n: int, edges, succProb, start_node: int, end_node: int) -> float:
    # Step 1: Build adjacency list correctly
    ad = {node: [] for node in range(n)}
    for i in range(len(edges)):
        u, v = edges[i]
        ad[u].append((v, succProb[i]))
        ad[v].append((u, succProb[i]))  # Since the graph is undirected

    # Step 2: Max-heap and probability tracker
    max_heap = [(-1.0, start_node)]  # Start with probability 1 (max heap uses negative values)
    max_prod = {node: 0.0 for node in range(n)}  # Initialize max probabilities to 0
    max_prod[start_node] = 1.0  # Start node has 100% probability

    # Step 3: Dijkstra's algorithm with max heap
    while max_heap:
        prob, node = heapq.heappop(max_heap)
        prob = -prob  # Convert back to positive probability

        # If we reach the end node, return the max probability
        if node == end_node:
            return prob

        # Explore neighbors
        for nei, edge_prob in ad[node]:
            new_prob = prob * edge_prob  # Multiply probabilities along the path
            if new_prob > max_prod[nei]:  # Update if a better probability is found
                max_prod[nei] = new_prob
                heapq.heappush(max_heap, (-new_prob, nei))  # Push into max heap

    # If no path to the end node exists
    return 0.0
