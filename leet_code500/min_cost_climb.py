def minCostClimbingStairs(cost):
    n = len(cost)
    if n == 2:
        return min(cost[0], cost[1])
    #dp[i] = cost[i] + min(dp[i−1], dp[i−2])
    dp = [0] * n
    dp[0], dp[1] = cost[0], cost[1]
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    return min(dp[n - 1], dp[n - 2])
# Example Usage:
cost = [10, 15, 20]
print(minCostClimbingStairs(cost))  # Output: 15

def minCostClimbingStairs(cost):
    memo = {}

    def dp(i):
        if i < 0:
            return 0
        if i == 0 or i == 1:
            return cost[i]
        if i in memo:
            return memo[i]

        memo[i] = cost[i] + min(dp(i - 1), dp(i - 2))
        return memo[i]

    n = len(cost)
    return min(dp(n - 1), dp(n - 2))

# Example Usage:
cost = [10, 15, 20]
print(minCostClimbingStairs(cost))  # Output: 15
