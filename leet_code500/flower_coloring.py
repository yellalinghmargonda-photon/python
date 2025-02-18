from collections import defaultdict

def garden_no_adj(n, paths):
    # Step 1: Build the adjacency list

    graph = defaultdict(list)
    for x, y in paths:
        graph[x].append(y)
        graph[y].append(x)
    print(graph)
    # Step 2: Assign flowers using a greedy algorithm
    flowers = [0] * n  # Initialize flower assignments (0 means unassigned)

    for garden in range(1, n + 1):
        # Step 3: Find the flowers used by neighboring gardens
        used_flowers = {flowers[neighbor - 1] for neighbor in graph[garden]}
        # Step 4: Assign the smallest available flower type (1, 2, 3, 4)
        for flower in range(1, 5):
            if flower not in used_flowers:
                flowers[garden - 1] = flower  # Assign flower to the garden
                break

    return flowers  # Return the flower assignments

# Example Test Case
n = 4
paths = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]  # Gardens with paths
print(garden_no_adj(n, paths))  # Output: [1, 2, 3, 4] (or another valid assignment)
