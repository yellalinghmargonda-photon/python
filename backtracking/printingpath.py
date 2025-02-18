def paths(p, maze, r, c, step, pathmat):
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        pathmat[r][c] = step
        return [p]  # Return a list containing the valid path

    pathmat[r][c] = step

    if not maze[r][c]:  # If the cell is blocked, return an empty list
        return []

    maze[r][c] = False  # Mark the cell as visited
    paths_list = []  # Store all valid paths

    if r < len(maze) - 1:
        paths_list.extend(paths(p + 'D', maze, r + 1, c, step + 1, pathmat))  # Down

    if c < len(maze[0]) - 1:
        paths_list.extend(paths(p + 'R', maze, r, c + 1, step + 1, pathmat))  # Right

    if r > 0:
        paths_list.extend(paths(p + 'U', maze, r - 1, c, step + 1, pathmat))  # Up

    if c > 0:
        paths_list.extend(paths(p + 'L', maze, r, c - 1, step + 1, pathmat))  # Left

    maze[r][c] = True  # Unmark the cell (backtracking)
    pathmat[r][c] = 0  # Reset step for this cell

    return paths_list  # Return collected paths

# Example maze
board = [
    [True, True, True],
    [True, False, True],
    [True, True, True]
]

# Initialize path matrix
pathmat = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Call the function and print all possible paths
print(paths(p='', maze=board, r=0, c=0, step=1, pathmat=pathmat))
