def explor_path(m, n):
    if m==0 or n==0:
        return 1
    if m<0 or n<0:
        return 0
    up=explor_path(m-1,n)
    left=explor_path(m, n-1)
    return up+left
def explor_path_memo(m,n, dp):
    if dp[m][n]!=0:
        return dp[m][n]
    if m==0 or n==0:
        return 1
    up = explor_path_memo(m - 1, n,dp)
    left = explor_path_memo(m, n - 1,dp)
    dp[m][n]=up+left
    return dp[m][n]
dp=[[0]*n for _ in range(m)]

def explor_path_tabulation(m,n, dp):
    # Initialize the base cases: first row and first column
    for i in range(m):
        dp[i][0] = 1  # There's only one way to reach any cell in the first column (moving down)

    for j in range(n):
        dp[0][j] = 1  # There's only one way to reach any cell in the first row (moving right)

    for row in range(1, m):
        for col in range(1, n):
            up = dp[row - 1][col] if row>0 else 0
            left = dp[row][col-1] if col>0 else 0
            dp[m][n] = up + left
    return dp[m][n]
