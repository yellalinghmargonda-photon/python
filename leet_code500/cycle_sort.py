def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1  # Correct position for nums[i]
        if 1 <= nums[i] <= len(nums) and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]  # Swap
        else:
            i += 1  # Move forward only if no swap happens
        print(nums)

# Example usage
arr = [3, 4, -1, 1]
cyclic_sort(arr)
print(arr)  # Output: [1, 2, 3, 4, 5]
