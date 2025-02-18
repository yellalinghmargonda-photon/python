def jump(index, nums):
    if index==len(nums)-1:
        return True
    if nums[index]==0:
        return False
    max_jump=nums[index]
    for j in range(index+1, min(max_jump+index+1, len(nums))):
        if jump(j ,nums):
            return True
    return False
nums = [2,3,1,1,4]
print(jump(0, nums))

def jumpdp(nums):
    n=len(nums)
    dp=[False]*(n)
    dp[-1]=True

    for i in range(n-2, -1, -1):
        max_jump=nums[i]
        for j in range(i + 1, min(i + max_jump + 1, n)):
            if dp[j]:
                dp[i]=True
                break
    return dp[0]
nums = [3, 2, 1, 0, 4]
print(jumpdp(nums))  # Output: True


