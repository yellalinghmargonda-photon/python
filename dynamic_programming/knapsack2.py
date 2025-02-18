def knapsack( values,weights,capacity):
    n=len(values)
    dp=[[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(capacity+1):
            if weights[i-1]>w:
                dp[i][w]=dp[i-1][w]
            else:
                dp[i][w]=max(values[i-1]+dp[i-1][w-weights[i - 1]],dp[i-1][w])

    select=[]
    w=capacity
    for i in range(n,0,-1):
        if dp[i][w] != dp[i - 1][w]:
            select.append(i-1)
            w-=weights[i-1]
    return dp[n][capacity],select
# Example usage
values = [6, 10, 12]
weights = [1, 2, 3]
capacity = 5
max_value, items = knapsack(values, weights, capacity)
print(f"Maximum value: {max_value}")
print(f"Selected items: {items}")
