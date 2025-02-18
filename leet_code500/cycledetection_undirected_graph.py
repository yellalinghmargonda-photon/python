def dfs(graph, seen, parent, node):
    """
    Depth-First Search to detect cycles in an undirected graph.

    Parameters:
    - graph: Dictionary representing an adjacency list of the graph.
    - seen: Set to keep track of visited nodes.
    - parent: The parent node in the DFS traversal (to avoid false cycles).
    - node: The current node being visited.

    Returns:
    - True if a cycle is detected, False otherwise.
    """

    seen.add(node)  # Mark the node as visited

    for nei in graph[node]:  # Iterate over all neighbors
        if nei not in seen:  # Visit unvisited neighbors
            if dfs(graph, seen, node, nei):  # If a cycle is found in recursion, return True
                return True
        elif nei != parent:  # If the neighbor is visited and is NOT the parent, a cycle exists
            return True

    return False  # No cycle found


# Wrapper function to check for cycles in the graph
def detect_cycle(graph):
    seen = set()  # Set to track visited nodes

    for node in graph:  # Handle disconnected components
        if node not in seen:
            if dfs(graph, seen, -1, node):  # Start DFS with no parent (-1)
                return True  # Cycle detected

    return False  # No cycle found


# Example Graph with a Cycle
graph_with_cycle = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]  # Cycle exists: 1 → 3 → 2 → 1
}

# Example Graph without a Cycle
graph_without_cycle = {
    0: [1, 2],
    1: [0],
    2: [0, 3],
    3: [2]
}

# Test Cases
print("Graph with cycle:", detect_cycle(graph_with_cycle))  # Output: True
print("Graph without cycle:", detect_cycle(graph_without_cycle))  # Output: False
