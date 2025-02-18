# Backtracking function to generate all topological orders

def create_directed_graph(edges, num_nodes):
    adj_list = {i: [] for i in range(num_nodes)}
    in_degree = {i: 0 for i in range(num_nodes)}

    for u, v in edges:
        adj_list[u].append(v)  # Directed edge from u -> v
        in_degree[v] += 1       # Increase in-degree of v

    return adj_list, in_degree
def all_topo_sorts(graph, in_degree, topo_order, visited, result):
    """
    Generates all possible topological orderings of a DAG using backtracking.

    Parameters:
    - graph: Adjacency list representation of the DAG.
    - in_degree: Dictionary storing in-degree of each node.
    - topo_order: List storing the current topological order being built.
    - visited: Dictionary marking visited nodes.
    - result: List to store all valid topological orderings.
    """

    ### BASE CASE: If topo_order contains all nodes, add the result and return
    if len(topo_order) == len(graph):
        result.append(topo_order[:])  # Store a copy of the valid order
        return

    ### RECURSION: Try to find all nodes with in-degree 0
    for node in range(len(graph)):
        if in_degree[node] == 0 and not visited[node]:  # Unvisited nodes with no dependencies
            # Mark the node as visited and include it in the topological order
            visited[node] = True
            topo_order.append(node)

            # Reduce in-degree for all neighbors (simulate node removal)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1

            # Recursive call to continue finding topological orders
            all_topo_sorts(graph, in_degree, topo_order, visited, result)

            # BACKTRACK: Undo changes to explore other possibilities
            visited[node] = False
            topo_order.pop()
            for neighbor in graph[node]:
                in_degree[neighbor] += 1

# Function to generate all topological orderings
def get_all_topological_sorts(edges, num_nodes):
    graph, in_degree = create_directed_graph(edges, num_nodes)
    visited = {i: False for i in range(num_nodes)}
    result = []
    all_topo_sorts(graph, in_degree, [], visited, result)
    return result
