
def majorityElement(nums):
    dict={}
    nums.sort()
    count=1
    n=len(nums)//2
    print(n)
    for i in range(len(nums)-1):
        print(count,nums[i])
        if nums[i]==nums[i+1]:
            count=count+1
        else:
            if count>n:
                return nums[i]
            count=1
    if count > n:
        return nums[-1]

ele=majorityElement([3,2,3])
print(ele)

