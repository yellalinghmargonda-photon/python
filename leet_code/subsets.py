def dfs(ans, nums, idx):
    if idx == len(nums):
        return [ans[:]]
    ans.append(nums[idx])
    left = dfs(ans, nums, idx + 1)
    ans.pop()
    while idx+1<len(nums) and nums[idx]==nums[idx+1]:
        idx+=1
    right = dfs(ans, nums, idx + 1)
    return left + right
print(dfs([],[1,2,2,3],0))