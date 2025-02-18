def closest(nums, target):
    l,r=0, len(nums)-1
    while l<=r:
        mid=l+(r-l)//2
        if nums[mid]==target:
            return mid
        if nums[mid]<target:
            l=mid+1
        else:
            r=mid-1

    return nums[l] if abs(nums[l]-target)<abs(nums[r]-target) else nums[r]

print(closest([1, 3, 8, 10, 15], 12))  # Output: 10
