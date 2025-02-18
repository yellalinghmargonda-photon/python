
def issafe(row, col, grid, visited):
    return 0<=row<len(grid) and 0<=col<len(grid[0]) and grid[row][col]==1 and not visited[row][col]

def rat_maze_path(path, row, col, grid, visited):
    if row==len(grid)-1 and col==len(grid[0])-1:
        return [path]
    visited[row][col]=True
    temp_path=[]

    directions = [(0, -1, 'L'),(0, 1, 'R'), (-1, 0, 'U'), (1, 0, 'D')]
    for r, c, d in directions:
        dr, dc=row+r, col+c
        if issafe(dr,dc,grid, visited):
            temp_path.extend(rat_maze_path(path+d, dr,dc, grid,visited))
    visited[row][col] = False
    return temp_path
# Example usage
grid = [
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
]
visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
print(rat_maze_path("", 0, 0, grid, visited))

