def search_insert_position(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid  # Target found, return index
        elif nums[mid] < target:
            l = mid + 1  # Search in the right half
        else:
            r = mid - 1  # Search in the left half
    return l  # Position where target should