def can_partition_memo(nums, n, target, memo):
    # Base Cases
    if target == 0:
        return True
    if n == 0 or target < 0:
        return False

    # Check if result is already computed
    if (n, target) in memo:
        return memo[(n, target)]

    # Exclude the current element
    exclude = can_partition_memo(nums, n - 1, target, memo)

    # Include the current element
    include = can_partition_memo(nums, n - 1, target - nums[n - 1], memo)

    # Store result in memoization table
    memo[(n, target)] = exclude or include
    return memo[(n, target)]





def canPartition(nums) -> bool:

        total_sum = sum(nums)

        # If sum is odd, partitioning is not possible
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        # Base case: Sum of 0 is always possible
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[n][target]  # Final answer



