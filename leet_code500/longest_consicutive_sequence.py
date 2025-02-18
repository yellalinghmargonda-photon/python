def LCS(nums):
    nums_set=set(nums)
    longest_streak=0

    for num in nums_set:
        if num-1 not in nums_set:
            current_num=num
            current_streak=1
            while current_num+1 in nums_set:
                current_num+=1
                current_streak+=1
            longest_streak=max(longest_streak,current_streak)
    return longest_streak
nums = [100, 4, 200, 1, 3, 2]
print(LCS(nums))  # Output: 4