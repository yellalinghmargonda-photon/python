def knapsack(weights, values, W, n):
    if n == 0 or W == 0:
        return 0
        # If weight of the nth item is more than capacity W, we cannot include it
    if weights[n - 1] > W:
            return knapsack(weights, values, W, n - 1)
    else:
        include= values[n-1]+knapsack(weights, values, W-weights[n-1], n - 1)
        exclude = knapsack(weights, values, W, n - 1)
    return  max(include,exclude)
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5  # Maximum weight capacity
n = len(weights)
print(knapsack(weights, values, W, n))  # Output: 7

def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]  # DP table

    for i in range(1, n + 1):  # Iterate through items
        for w in range(1, W + 1):  # Iterate through weight capacities
            if weights[i - 1] <= w:  # Can we include this item?
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:  # Otherwise, exclude it
                dp[i][w] = dp[i-1][w]

    return dp[n][W]

# Example
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
print(knapsack(weights, values, W))  # Output: 7
