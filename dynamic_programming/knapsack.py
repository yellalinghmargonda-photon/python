def knapsack(values, weights, capacity):
    """
    Solves the 0/1 Knapsack Problem using Dynamic Programming.

    :param values: List of values of items.
    :param weights: List of weights of items.
    :param capacity: Maximum capacity of the knapsack.
    :return: Maximum value that can be achieved and the selected items.
    """
    n = len(values)
    # Create a DP table with dimensions (n+1) x (capacity+1)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]  # Exclude the item
            else:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    # Trace back to find the selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # Item indices are 0-based
            w -= weights[i - 1]

    return dp[n][capacity], selected_items


# Example usage
values = [6, 10, 12]
weights = [1, 2, 3]
capacity = 5
max_value, items = knapsack(values, weights, capacity)
print(f"Maximum value: {max_value}")
print(f"Selected items: {items}")
