def path_sum(m, n,grid):
    if m==0 and n==0:
        return grid[0][0]
    if n<0 or m<0:
        return float('inf')  # Return a large value instead of None
    right=path_sum(m-1,n, grid)
    down=path_sum(m,n-1,grid)
    return min(right, down)+grid[m][n]
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(path_sum(len(grid)-1,len(grid[0])-1,grid))

def path_sum_memo(m, n, memo, grid):
    if (m, n) in memo:
        return memo[(m,n)]
    if m==0 and n==0:
        return grid[0][0]
    if n<0 or m<0:
        return float('inf')  # Return a large value instead of None
    right=path_sum_memo(m-1,n, memo,grid)
    down=path_sum_memo(m,n-1,memo,grid)
    memo[(m,n)]=min(right, down)+grid[m][n]
    return memo[(m,n)]
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(path_sum_memo(len(grid)-1,len(grid[0])-1,{},grid))

m=len(grid)
n=len(grid[0])
dp=[[-1]*n for _ in range(m)]
def path_sum2d_memo(m,n, dp, grid):

      if m==0 and n==0:
          return grid[0][0]

      if dp[m][n]!=-1:
          return dp[m][n]
      if m<0 or n<0:
          return float('inf')
      right=path_sum2d_memo(m-1,n, dp,grid)
      down=path_sum2d_memo(m,n-1,dp,grid)
      dp[m][n]=min(right, down)+grid[m][n]
      return dp[m][n]


grid = [[1,3,1],[1,5,1],[4,2,1]]                              
print(path_sum2d_memo(len(grid)-1,len(grid[0])-1,dp,grid))

def path_sum_dp(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0]=grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

        # Fill first row (can only come from left)
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    for i in range(1,m):
        for j in range(1, n):
            dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
    return dp[m-1][n-1]
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(path_sum_dp(grid))

