def search(nums, start, end, target):
    if start > end:
        return [-1, -1]  # Not found

    mid = start + (end - start) // 2

    if nums[mid] == target:
        l, r = mid, mid

        # Expand left boundary
        while l >= start and nums[l] == target:
            l -= 1

        # Expand right boundary
        while r <= end and nums[r] == target:
            r += 1

        return [l + 1, r - 1]  # Adjusting for extra decrement/increment

    elif nums[mid] > target:
        return search(nums, start, mid - 1, target)
    else:
        return search(nums, mid + 1, end, target)  # Corrected right half search

# Test cases
print(search([1, 2, 3, 4], 0, 3, 3))  # Output: [2, 2] (3 is at index 2)
print(search([1, 1, 2, 2, 3, 3, 3, 4], 0, 7, 3))  # Output: [4, 6] (3 occurs from index 4 to 6)
print(search([1, 2, 3, 4], 0, 3, 8))  # Output: [-1, -1] (8 is not in the list)
