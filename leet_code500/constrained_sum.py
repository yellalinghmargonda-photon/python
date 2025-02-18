def maxSumRec(nums, k, i, memo):
    # Base case: If we have reached the end of the array
    if i >= len(nums):
        return 0

    # Check if the result for this index i has already been computed
    if i in memo:
        return memo[i]

    # Option 1: Skip the current element and move to the next element
    skip = maxSumRec(nums, k, i + 1, memo)

    # Option 2: Include the current element in the subsequence
    include = nums[i]

    # Iterate over all valid indices j in the range [i + 1, i + k], ensuring we do not go beyond array bounds
    for j in range(i + 1, min(i + k + 1, len(nums))):
        include = max(include, nums[i] + maxSumRec(nums, k, j, memo))

    # Store the maximum of both options (skip and include) in the memo dictionary
    memo[i] = max(skip, include)

    return memo[i]


def maxSum(nums, k):
    memo = {}
    result = maxSumRec(nums, k, 0, memo)

    # Ensure that if all numbers are negative, we return the largest negative number (i.e., least negative)
    if result <= 0:
        return max(nums)  # This handles cases like [-1, -2, -3], where -1 is the largest

    return result


# Example usage
nums = [10, -2, -10, -5, 20]
k = 2
print(maxSum(nums, k))  # Output should be 23
