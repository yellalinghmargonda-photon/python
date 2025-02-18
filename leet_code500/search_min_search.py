def min_serach(nums,start,end):
    if start==end:
        return nums[start]
    mid=start+(end-start)//2

    if nums[mid]>nums[end]:
        return min_serach(nums,mid+1,end)
    else:
        return min_serach(nums,start, mid)
print(min_serach([4,5,6,7,8,0,1,2,3],0, 8))