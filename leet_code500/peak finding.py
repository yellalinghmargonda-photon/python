def findPeakElement(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]:  # Descending slope, move left
            r = mid
        else:  # Ascending slope, move right
            l = mid + 1
    return l  # l and r converge to a peak

# Example Test Cases
print(findPeakElement([1, 2, 3, 1]))  # Output: 2 (nums[2] = 3 is a peak)
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Output: 5 (nums[5] = 6 is a peak)
print(findPeakElement([10, 20, 15, 2, 23, 90, 67]))  # Output: 1 or 5
