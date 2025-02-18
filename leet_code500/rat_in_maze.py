import sys

def is_safe(mat, visited, x, y):
    """Check if the cell (x, y) is within bounds, not blocked, and not visited."""
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == 1 and not visited[x][y]

def find_shortest_path(mat, visited, i, j, dest, min_dist=sys.maxsize, dist=0):
    """Recursively find the shortest path from (i, j) to `dest`."""
    if (i, j) == dest:
        return min(dist, min_dist)

    # Mark cell as visited
    visited[i][j] = True

    # Possible moves: Down, Right, Up, Left
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in directions:
        new_x, new_y = i + dx, j + dy
        if is_safe(mat, visited, new_x, new_y):
            min_dist = find_shortest_path(mat, visited, new_x, new_y, dest, min_dist, dist + 1)

    # Backtrack: Unmark cell as visited
    visited[i][j] = False

    return min_dist

def find_shortest_path_length(mat, src, dest):
    """Wrapper function to find the shortest path length."""
    i, j = src
    x, y = dest

    if not mat or mat[i][j] == 0 or mat[x][y] == 0:
        return -1

    M, N = len(mat), len(mat[0])
    visited = [[False] * N for _ in range(M)]

    min_dist = find_shortest_path(mat, visited, i, j, dest)

    return min_dist if min_dist != sys.maxsize else -1
