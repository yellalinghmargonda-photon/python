def coin_change_optimized(coins, S):
    dp = [0] * (S + 1)
    dp[0] = 1  # One way to make amount 0

    for coin in coins:
        for j in range(coin, S + 1):
            dp[j] += dp[j - coin]
    print(dp)
    return dp[S]

# Example usage:
coins = [1, 2, 3]
S = 4
print(coin_change_optimized(coins, S))  # Output: 4

def coinchange(coins, s,n):
    if s==0:
        return 1
    if n==0 or s<0:
        return 0
    return coinchange(coins, s,n-1)+coinchange(coins, s- coins[n - 1],n)
coins = [1, 2, 3]
S = 4

print(coinchange(coins, S, len(coins)))  # Output: 4
