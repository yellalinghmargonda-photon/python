def dutch_sort(nums):
    low,  mid,high=0,0, len(nums)-1
    while mid<=high:
        if nums[mid]==0:
            nums[low], nums[mid]=nums[mid],nums[low]
            mid+=1
            low+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high-=1

    return  nums
print(dutch_sort([1,1,2,0,1,0]))