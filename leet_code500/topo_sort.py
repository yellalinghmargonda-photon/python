edges = [
    (0, 1),
    (1, 2),
    (2, 0),  # Cycle
    (3, 4)
]

# Step 1: Initialize nodes, adjacency list, and in-degree dictionary
nodes = set()
for u, v in edges:
    nodes.add(u)
    nodes.add(v)

ad = {node: [] for node in nodes}
in_degree = {node: 0 for node in nodes}

# Step 2: Build adjacency list and in-degree map
for u, v in edges:
    ad[u].append(v)  # Append instead of assigning
    in_degree[v] += 1  # Increment in-degree

print("In-degree:", in_degree)

# Step 3: Initialize queue with nodes having in-degree 0
queue = [node for node, in_d in in_degree.items() if in_d == 0]
visited = set()

# Step 4: Process nodes in topological order
processed_nodes = 0
while queue:
    node = queue.pop(0)
    visited.add(node)
    processed_nodes += 1  # Count processed nodes
    for nei in ad[node]:
        in_degree[nei] -= 1
        if in_degree[nei] == 0:
            queue.append(nei)

# Step 5: Cycle detection check
if processed_nodes == len(nodes):
    print("No cycle detected")
else:
    print("Cycle detected")
