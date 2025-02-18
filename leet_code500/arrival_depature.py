edges = [(0, 1), (0, 2), (2, 3), (2, 4), (3, 1), (3, 5), (4, 5), (6, 7)]
def graph_cration(edges):
    nodes=set()
    for u,v in edges:
        nodes.add(u)
        nodes.add(v)
    ad_list={node:[] for node in nodes }
    for u, v in edges:
        ad_list[u].append(v)
        ad_list[v].append(u)
    return ad_list
def dfs(graph, seen, arrival, depathure, time, node):
    if node not in seen:
        arrival[node]=time
        seen.add(node)
        for n in graph[node]:
            time=dfs(graph, seen, arrival, depathure, time+1, n)
        depathure[node]=time+1
        return  time+1
    return time
# Example graph (tree)
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [],
    3: [],
    4: []
}

# Initialize structures
seen = set()
arrival = {}
departure = {}
time = 0
#{0: 0, 1: 1, 3: 2, 4: 3, 2: 4} {3: 2, 4: 3, 1: 3, 2: 4, 0: 4}
# Run DFS
dfs(graph, seen, arrival, departure, time, 0)
print(arrival, departure)
