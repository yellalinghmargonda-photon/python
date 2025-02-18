def houseRobber(cost):
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[0]

    dp = [0] * (n + 1)
    dp[0] = 0  # No house to rob
    dp[1] = cost[0]  # First house (index 0)

    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], cost[i - 1] + dp[i - 2])  # Fix indexing

    return dp[n]


# Example Usage:
cost = [2, 7, 9, 3, 1]
print(houseRobber(cost))  # Output: 12 (Rob house 1 and 3)
