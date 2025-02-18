def solve(value,weights, remaining_weight, current_Val, i):
    if remaining_weight==0 or i==len(value):
        return current_Val
    include=float('-inf')
    if remaining_weight>=weights[i]:
        include =solve(value,weights,remaining_weight-weights[i],current_Val+value[i], i+1)
    exclude = solve(value, weights, remaining_weight, current_Val, i + 1)
    return max(include, exclude)

# Example Usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

# print(solve(values, weights, capacity, 0, 0))

def solve_memo(value,weights, remaining_weight, current_Val, i, dp):
    if remaining_weight==0 or i==len(value):
        return current_Val
    if dp[i][remaining_weight] != -1:
        return dp[i][remaining_weight]  # Return already computed value
    include=float('-inf')
    if remaining_weight>=weights[i]:
        include =solve_memo(value,weights,remaining_weight-weights[i],current_Val+value[i], i+1,dp)
    exclude = solve_memo(value, weights, remaining_weight, current_Val, i + 1,dp)
    dp[i][remaining_weight]=max(include, exclude)
    return dp[i][remaining_weight]

dp = [[-1 ]*(capacity + 1) for _ in range(len(values) + 1)]
print(len(dp),len(dp[0]))

print(solve_memo(values, weights, capacity, 0, 0, dp))  # ✅ Expected Output: 220
