edges = [
    # Notice that node 0 is unconnected
    (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
    (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
]

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

def dfs(graph, seen, node, result):
    if node not in seen:
        seen.add(node)  # Mark the node as visited
        result.append(node)
        for n in graph[node]:
            dfs(graph, seen, n, result)
    return result
edges = [
        # Notice that node 0 is unconnected
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]
grp=graph_cration(edges)
print(dfs(grp,set(),1,[]))

