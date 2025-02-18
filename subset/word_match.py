def singleNonDuplicate(nums):
    l = 0
    r = len(nums) - 1

    while l <= r:
       mid=l+(r-l)//2

       if nums[mid]!=nums[mid+1] and mid==0:
           return nums[mid]
       if nums[mid]!=nums[mid-1] and mid==len(nums)-1:
           return nums[mid]
       if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
           return nums[mid]
       if mid%2==0:
            if nums[mid]==nums[mid-1]:
               r = mid-1
            else:
                l= mid+1
       else:
           if nums[mid] == nums[mid - 1]:
               l = mid + 1
           else:
               r = mid - 1

# Test case
nums = [1, 1, 2,2, 3, 3, 4, 4, 5,8, 8]
print(singleNonDuplicate(nums))  # Output: 2