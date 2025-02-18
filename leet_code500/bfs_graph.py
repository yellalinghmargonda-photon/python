from collections import deque

# Graph edges (includes disconnected nodes)
edges = [
    # Notice that node 0, 13, and 14 are unconnected
    (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
    (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
]

# Function to create adjacency list
def graph_creation(edges):
    nodes = set()
    for u, v in edges:
        nodes.add(u)
        nodes.add(v)

    # Include all nodes (even if not in edges)
    all_nodes = nodes | {0, 13, 14}  # Add unconnected nodes

    adj_list = {node: [] for node in all_nodes}
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)  # Since it's undirected

    return adj_list

# BFS function
def bfs(graph, start_node, visited):
    queue = deque([start_node])
    bfs_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            bfs_order.append(node)

            # Add all unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return bfs_order

# Perform BFS for all disconnected components
def bfs_all_components(graph):
    visited = set()
    all_bfs_orders = []

    for node in graph:  # Ensure all nodes are visited
        if node not in visited:
            all_bfs_orders.append(bfs(graph, node, visited))

    print(all_bfs_orders)
    return all_bfs_orders

# Create the graph and perform BFS
graph = graph_creation(edges)
bfs_result = bfs_all_components(graph)

# Print BFS traversal for each component
for i, comp in enumerate(bfs_result, 1):
    print(f"BFS Component {i}: {comp}")
