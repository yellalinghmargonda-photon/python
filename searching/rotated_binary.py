def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        print(mid)
        # If the middle element is greater than the rightmost element,
        # the smallest element must be in the right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Otherwise, the smallest element is in the left half or at mid
            right = mid

    # At the end of the loop, left == right, and pointing to the smallest element
    return nums[left]
print(findMin([4,5,6,7,0,1,2]))