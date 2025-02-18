from collections import deque


# Function to create adjacency list from edge list
def graph_creation(edges):
    nodes = set()
    for u, v in edges:
        nodes.add(u)
        nodes.add(v)

    ad_list = {node: [] for node in nodes}
    for u, v in edges:
        ad_list[u].append(v)
        ad_list[v].append(u)  # Since it's an undirected graph

    return ad_list


# BFS function to check if graph is bipartite
def bfs(graph, start_node, colored):
    queue = [start_node]
    colored[start_node] = 0  # Start coloring with 0

    while queue:
        node = queue.pop(0)

        for nei in graph[node]:
            if nei not in colored:
                colored[nei] = 1 - colored[node]  # Assign opposite color
                queue.append(nei)
            elif colored[nei] == colored[node]:  # Conflict found
                return False

    return True


# Wrapper function to check all components (handles disconnected graphs)
def is_bipartite(edges):
    graph = graph_creation(edges)
    colored = {}

    for node in graph:  # Check all nodes (to handle disconnected graphs)
        if node not in colored:
            if not bfs(graph, node, colored):
                return False

    return True


# Example Usage

edges1 = [(0, 1), (1, 2), (2, 0)]  # Odd cycle (3 nodes)

edges2 = [(0, 1), (1, 2), (2, 3), (3, 4)]  # Bipartite

print(is_bipartite(edges1))  # Output: False
print(is_bipartite(edges2))  # Output: True
