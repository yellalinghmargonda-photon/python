def frog_jump(i, cost):
    if i==0:
        return 0
    left=frog_jump(i-1,cost)+abs(cost[i]-cost[i-1])
    right = frog_jump(i - 2,cost) + abs(cost[i] - cost[i - 2]) if i>1 else float('inf')

    return min(left, right)
array=[10,20,30,10]
print(frog_jump(len(array)-1,array))

def frog_jump_memo(i, cost, memo):
    if i==0:
        return 0
    if i in memo:
        return memo[i]
    left=frog_jump_memo(i-1,cost,memo)+abs(cost[i]-cost[i-1])
    right = frog_jump_memo(i - 2,cost,memo) + abs(cost[i] - cost[i - 2]) if i>1 else float('inf')
    memo[i]=min(left, right)
    return memo[i]
array=[10,20,30,10]
print(frog_jump_memo(len(array)-1,array,{}))
def frog_jump_tabulation(cost):
    n = len(cost)
    dp = [0] * n  # Only `n` elements needed

    for i in range(1, n):
        fs = dp[i - 1] + abs(cost[i] - cost[i - 1])
        sc = dp[i - 2] + abs(cost[i] - cost[i - 2]) if i > 1 else float('inf')
        dp[i] = min(fs, sc)

    return dp[n - 1]  # Correct last index

array = [10, 20, 30, 10]
print(frog_jump_tabulation(array))


