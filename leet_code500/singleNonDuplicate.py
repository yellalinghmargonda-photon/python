def singleNonDuplicate(nums):
    l = 0
    r = len(nums) - 1
    if r == 0:
        return nums[0]
    while l <= r:
        mid = l + (r - l) // 2
        # Check if nums[mid] is the single element
        if (mid == 0 or nums[mid] != nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] != nums[mid + 1]):
            return nums[mid]
        # if mid is even and mid=mid-1 then element is on the left side so move search is left, if mid is even and mid!=mid-1 then search on the right
        if mid % 2 == 0:
            if nums[mid] == nums[mid - 1]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] == nums[mid - 1]:
                l = mid + 1
            else:
                r = mid - 1
    return -1