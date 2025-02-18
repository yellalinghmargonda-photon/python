from collections import deque

# Function to create an adjacency list and calculate in-degrees
def create_directed_graph(edges, num_nodes):
    adj_list = {i: [] for i in range(num_nodes)}
    in_degree = {i: 0 for i in range(num_nodes)}

    for u, v in edges:
        adj_list[u].append(v)  # Directed edge from u -> v
        in_degree[v] += 1       # Increase in-degree of v

    return adj_list, in_degree

# Backtracking function to generate all topological orders
def all_topo_sorts(graph, in_degree, topo_order, visited, result):
    num_nodes = len(graph)

    # Try to find all nodes with in-degree 0
    found = False
    for node in range(num_nodes):
        if in_degree[node] == 0 and not visited[node]:  # Only process unvisited nodes
            found = True
            visited[node] = True  # Mark as visited
            topo_order.append(node)  # Add to the order

            # Reduce in-degree of its neighbors
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1

            # Recur to generate further topological orders
            all_topo_sorts(graph, in_degree, topo_order, visited, result)

            # Backtrack: Undo changes
            visited[node] = False
            topo_order.pop()
            for neighbor in graph[node]:
                in_degree[neighbor] += 1

    # If no node was added, we have found a valid topological order
    if not found:
        result.append(topo_order[:])

# Function to generate all topological orderings
def get_all_topological_sorts(edges, num_nodes):
    graph, in_degree = create_directed_graph(edges, num_nodes)
    visited = {i: False for i in range(num_nodes)}
    result = []
    all_topo_sorts(graph, in_degree, [], visited, result)
    return result

# Example test case
edges_acyclic = [
    (5, 0), (5, 2), (4, 0), (4, 1), (2, 3), (3, 1)
]
num_nodes = 6

# Get all topological orders
all_orders = get_all_topological_sorts(edges_acyclic, num_nodes)

# Print all possible topological orderings
print("All Possible Topological Orders:")
for order in all_orders:
    print(order)
