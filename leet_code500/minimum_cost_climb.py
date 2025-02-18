def min_Cost(i, nums, memo):
    # Base cases
    if i == len(nums):  # We’ve reached beyond the last step
        return 0

    # If we've already computed the minimum cost for this index, return it
    if i in memo:
        return memo[i]

    # Otherwise, compute the minimum cost to reach the end from this index
    cost_from_next = nums[i] + min_Cost(i + 1, nums, memo)  # Move one step ahead
    cost_from_next_next = float('inf')  # Default to infinity if out of bounds
    if i + 2 < len(nums):
        cost_from_next_next = nums[i] + min_Cost(i + 2, nums, memo)  # Move two steps ahead

    # Find the minimum cost between moving one or two steps ahead
    memo[i] = min(cost_from_next, cost_from_next_next)

    return memo[i]


def minCostClimbingStairs(nums):
    memo = {}
    # We start from the first step or the second step
    return min(min_Cost(0, nums, memo), min_Cost(1, nums, memo))


# Test the function with your example
nums = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(nums))  # Expected output: 6
