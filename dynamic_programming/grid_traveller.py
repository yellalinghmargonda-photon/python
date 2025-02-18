def gridtraveller(n):
    dp=[[0]*(n+1) for _ in range(n+1)]
    dp[1][1]=1
    for r in range(n+1):
        for c in range(n+1):
            if  c<=n-1:
                dp[r][c+1]=dp[r][c+1]+dp[r][c]
            if r<=n-1:
                dp[r+1][c] =dp[r+1][c]+ dp[r][c]

    return dp[n][n]
print(gridtraveller(3))