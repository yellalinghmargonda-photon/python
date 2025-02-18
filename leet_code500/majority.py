def majority(nums):
    candidate = None
    count = 0

    # Step 1: Find a candidate
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    # Step 2: Verify the candidate
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None  # No majority element


# Example Usage
print(majority([3, 3, 2, 1, 3, 1, 2, 3, 3, 3, 3]))  # Output: 3
print(majority([1, 2, 3, 4, 5]))  # Output: None (No majority)
