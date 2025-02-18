# Function to create an adjacency list for a directed graph
def create_directed_graph(edges):
    adj_list = {}
    for u, v in edges:
        if u not in adj_list:
            adj_list[u] = []
        adj_list[u].append(v)
    return adj_list

# DFS function to detect a cycle
def has_cycle(graph, node, visited, rec_stack):
    if node in rec_stack:  # Cycle detected
        return True

    if node in visited:  # Already visited and no cycle found earlier
        return False
    # Mark node as visited and add to recursion stack
    visited.add(node)
    rec_stack.add(node)
    # Recur for all neighbors
    for neighbor in graph.get(node, []):
        if has_cycle(graph, neighbor, visited, rec_stack):
            return True

    # Remove from recursion stack after backtracking
    rec_stack.remove(node)
    return False

# Function to check if the graph has a cycle
def detect_cycle(edges):
    graph = create_directed_graph(edges)
    visited = set()
    rec_stack = set()

    for node in graph:  # Check each node in case of disconnected components
        if node not in visited:
            if has_cycle(graph, node, visited, rec_stack):
                return True
    return False

# Example edges for a directed graph
edges_with_cycle = [
    (0, 1), (1, 2), (2, 3), (3, 1)  # Cycle: 1 → 2 → 3 → 1
]

edges_without_cycle = [
    (0, 1), (1, 2), (2, 3)  # No cycle
]

# Run cycle detection
print("Graph with cycle:", detect_cycle(edges_with_cycle))  # Output: True
print("Graph without cycle:", detect_cycle(edges_without_cycle))  # Output: False
