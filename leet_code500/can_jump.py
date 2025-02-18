def canJump(nums):
    def jump(index):
        # Base case: if we are at or past the last index
        if index >= len(nums) - 1:
            return True

        # If the current index cannot move anywhere (i.e., nums[index] == 0), return False
        max_jump = nums[index]
        if max_jump == 0:
            return False

        # Try all possible jumps from the current position
        for next_index in range(index + 1, index + max_jump + 1):
            if jump(next_index):
                return True

        return False

    # Start from the first index
    return jump(0)


# Test the function
nums = [2, 3, 1, 1, 4]
print(canJump(nums))  # Output: True

nums = [3, 2, 1, 0, 4]
print(canJump(nums))  # Output: False
