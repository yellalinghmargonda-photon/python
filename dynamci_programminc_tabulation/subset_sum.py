def subset_sum(i, target, array):
    if target==0:
        return True
    if i<0 or target<0:
        return False
    include=subset_sum(i-1,target-array[i], array)
    exclude=subset_sum(i-1,target,array)
    return include or exclude

def subsetsum_memo(i, target, array, dp):
    if dp[i][target]!=-1:
        return dp[i][target]

    if target==0:
        return True
    if i<0 :
        return False

        # Include current element (only if target >= array[i])
    include = False
    if target >= array[i]:
        include = subsetsum_memo(i - 1, target - array[i], array, dp)
    exclude=subsetsum_memo(i-1,target,array,dp)
    dp[i][target]=include or exclude
    return dp[i][target]

# Example usage
arr = [3, 34, 4, 12, 5, 2]
target = 9
dp=[[-1]*(target+1) for _ in range(len(arr)+1)]

def subsetsum_memo_dp(target,arr):
    n=len(arr)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    for i in range(n+1):
        dp[0][i]=True
    for i in range(1, n+1):
        for j in range(1, target + 1):
            if j>=arr[i-1]:
                dp[i][j]= dp[i-1][j - arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][target]
print(subsetsum_memo_dp(target,arr))
