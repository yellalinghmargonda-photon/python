
def can_partition_k_subsets(nums, k, target, subsets, idx):
    # Base case: if we successfully fill all subsets
    if idx < 0:
        return all(s == target for s in subsets)

    # Try placing the current number in one of the `k` subsets
    for i in range(k):
        if subsets[i] + nums[idx] <= target:
            subsets[i] += nums[idx]  # Add number to subset
            if can_partition_k_subsets(nums, k, target, subsets, idx - 1):
                return True  # Found a valid partition
            subsets[i] -= nums[idx]  # Backtrack

        # Optimization: If this subset is empty, don't try others
        if subsets[i] == 0:
            break

    return False
k=5
nums=[1,2,3,3,1,3,1,]
total = sum(nums)


target = total // k  # Each subset must sum to this
nums.sort(reverse=True)  # Sorting helps reduce unnecessary recursion
subsets = [0] * k  # Track sums of each subset
can_partition_k_subsets(nums, k, target, subsets, len(nums) - 1)