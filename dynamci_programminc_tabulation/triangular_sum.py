def triangular(i, j, grid):
    if i==len(grid)-1:
        return grid[i][j]
    d=grid[i][j]+triangular(i+1,j, grid)
    dg=grid[i][j] + triangular(i + 1, j+1,grid)
    return  min(d, dg)
TRIANGLE = [[1], [2,3], [3,6,7], [8,9,6,1]]

print(triangular(0,0,TRIANGLE))

def triangular_memo(i, j, grid, memo):
    if i==len(grid)-1 :
        return grid[i][j]
    d=grid[i][j]+triangular_memo(i+1,j, grid, memo)
    dg=grid[i][j] + triangular_memo(i + 1, j+1,grid, memo)
    memo[i][j]=min(d, dg)
    return  memo[i][j]
grid = [[1], [2,3], [3,6,7], [8,9,6,1]]
m=len(grid)
n=len(grid[0])
dp = [[-1] * len(row) for row in grid]

print(triangular_memo(0,0,grid,dp))

def trigular_2d(grid):
    dp = [[-1] * len(row) for row in grid]
    n=len(grid)
    for j in range(len(grid[-1])):
        dp[n-1][j]=grid[n-1][j]
    for i in range(n-2, -1, -1):
        for j in range(i, -1, -1):
            d=dp[i+1][j]+grid[i][j]
            dg=dp[i + 1][j+1] + grid[i][j]
            dp[i][j]=min(d,dg)
    return dp[0][0]
print(trigular_2d(grid))
