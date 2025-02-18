def matsum(i, j, grid,dp):
    if i<0 or j<0 or j>=len(grid[0]):
        return float('-inf')
    if dp[i][j]!=-1:
        return dp[i][j]
    if i==0:
        dp[i][j]=grid[i][j]
        return grid[i][j]
    l=grid[i][j]+matsum(i-1, j-1, grid,dp)
    u=grid[i][j]+matsum(i-1, j, grid, dp)
    r = grid[i][j] + matsum(i - 1, j + 1, grid,dp)
    dp[i][j]=max(l,r, u)
    return dp[i][j]


def find_maximum_path_sum(grid):
    rows = len(grid)
    cols = len(grid[0])

    max_sum = -float('inf')
    dp=[[-1]*cols for _ in range(rows)]
    # Try starting from every column in the last row
    for j in range(cols):
        max_sum = max(max_sum, matsum(rows - 1, j, grid,dp))

    return max_sum


# Example input
grid = [
    [1, 2, 3],
    [9, 8, 7],
    [4, 5, 6]
]

print(find_maximum_path_sum(grid))  # Output: 17

