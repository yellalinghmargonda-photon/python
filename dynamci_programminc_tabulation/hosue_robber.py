def house_robber(i, nums):
    if i < 0:
        return 0  # No house left to rob
    if i == 0:
        return nums[0]  # Only one house to rob

    # Choice: Rob current house or skip it
    rob = nums[i] + house_robber(i - 2, nums)  # Rob house i, move to i-2
    skip = house_robber(i - 1, nums)  # Skip house i, move to i-1

    return max(rob, skip)  # Take the max of both choices

# Example usage:
nums = [2, 7, 9, 3, 1]
print(house_robber(len(nums) - 1, nums))  # Expected Output: 12

def house_robber_memo(i, nums, memo):
    if i < 0:
        return 0  # No house left to rob
    if i == 0:
        return nums[0]  # Only one house to rob
    if i in memo:
        return  memo[i]

    # Choice: Rob current house or skip it
    rob = nums[i] + house_robber(i - 2, nums)  # Rob house i, move to i-2
    skip = house_robber(i - 1, nums)  # Skip house i, move to i-1
    memo[i]=max(rob, skip)
    return memo[i]  # Take the max of both choices

def house_robber_tabulation(nums):
    n=len(nums)
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=nums[0]
    dp[2]=max(nums[0],nums[1])
    for i in range(3, n):
        dp[i]= max(dp[i]+dp[i-2],dp[i-1])
    return dp[n-1]
