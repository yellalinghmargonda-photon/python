# Solving "1971. Find if Path Exists in Graph"

When solving the problem "1971. Find if Path Exists in Graph," the thought process should involve breaking down the problem systematically. Here’s an intuition-driven guide to approaching it:

## 1. **Understand the Problem**
- You are given a graph (nodes and edges) and two nodes (`source` and `destination`).
- Your goal is to determine if there is a path from `source` to `destination`.

Ask yourself:
- Is the graph directed or undirected?
- Are there any constraints on the graph (e.g., maximum nodes/edges, connectivity)?

## 2. **Graph Representation**
- Think about how to represent the graph efficiently. For example:
  - **Adjacency List:** Ideal for sparse graphs as it saves memory.
  - **Adjacency Matrix:** Useful for dense graphs but can consume more memory.
- An adjacency list is often preferred for problems involving traversal because it efficiently stores edges and allows easy iteration over neighbors.

## 3. **Pathfinding and Traversal**
- You need to determine if you can "reach" the destination from the source. This hints at a graph traversal algorithm.
  - **Breadth-First Search (BFS):** Best for finding the shortest path in an unweighted graph. Use when you want to explore level-by-level.
  - **Depth-First Search (DFS):** Explores as far as possible along one branch before backtracking. Use when you want to dive deep into one path.
- Consider whether to use iterative (stack/queue) or recursive approaches for DFS/BFS based on your preference or constraints.

## 4. **Key Questions to Ask**
- **Graph connectivity:** Are all nodes connected, or could there be disconnected components?
- **Cycles:** Are cycles a concern, or can you ignore them?
- **Visited nodes:** How will you track visited nodes to avoid redundant checks and infinite loops?

## 5. **Base Cases and Edge Cases**
- What if the graph has no edges? (`n = 1` or empty graph)
- What if `source` and `destination` are the same node? (Check this as a base case.)
- What if `source` or `destination` is not present in the graph? (Invalid input?)

## 6. **Algorithm Choice**
- Start from the `source` node.
- Traverse the graph using BFS/DFS.
- Stop when:
  - You reach the `destination` (path exists).
  - You exhaust all possibilities (path doesn’t exist).

## 7. **Optimize for Large Inputs**
- The number of nodes and edges can be large. Optimize:
  - Avoid redundant visits using a `visited` set.
  - Choose data structures (e.g., dictionaries/lists for adjacency list) wisely to reduce overhead.

## 8. **Iterative vs Recursive**
- If using recursion for DFS, be mindful of stack overflow for deep recursion in large graphs.
- Prefer an iterative approach (using an explicit stack or queue) for robustness in such cases.

By systematically thinking through these steps, you can devise a clear plan to solve the problem and implement it effectively.


# Example Input

```python
edges = [[0, 1], [1, 2], [2, 0], [3, 4]]
n = 5  # Number of nodes (0 to n-1)

# Step 1: Initialize the adjacency list
adj_list = {i: [] for i in range(n)}

# Step 2: Populate the adjacency list
for u, v in edges:
    adj_list[u].append(v)  # Add v as a neighbor of u
    adj_list[v].append(u)  # Add u as a neighbor of v (for undirected graph) remove this line for directed graph

# Resulting adjacency list
print(adj_list)

```python
{
  0: [1, 2],
  1: [0, 2],
  2: [1, 0],
  3: [4],
  4: [3]
}

# Depth-First Search (DFS) Approach

A common DFS (Depth-First Search) approach to traverse from a source node to a target node involves recursively or iteratively exploring the graph. Here's how you can implement it:

## Recursive DFS Implementation

```python
def dfs_recursive(node, target, adj_list, visited):
    if node == target:
        return True
    
    visited.add(node)
    
    for neighbor in adj_list[node]:
        if neighbor not in visited:
            if dfs_recursive(neighbor, target, adj_list, visited):
                return True
    
    return False
