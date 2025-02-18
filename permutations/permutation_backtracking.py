def permutation(result, nums, templist,used):
    if len(templist)==len(nums):
        result.append(templist[:])
        return

    for i in range(len(nums)):
        # Skip used elements or duplicate elements in the same recursive level
        if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
            continue
        used[i] = True
        templist.append(nums[i])
        permutation(result, nums, templist, used)
        templist.pop()
        used[i] = False
    return  result
nums=[1,2,2,3]
result=permutation([],nums,[],[False] * len(nums))
print(result)