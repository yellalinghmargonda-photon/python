def partitions_3(nums, a,b, c, idx):
    if a==0 and b==0 and c==0:
        return True
    if idx<0:
        return  False
    A=False
    if a-nums[idx]>=0:
        A=partitions_3(nums, a-nums[idx],b,c, idx-1)
    B = False
    if  not A  and b - nums[idx] >= 0:
        B = partitions_3(nums, a, b - nums[idx], c, idx -1)
    C=False
    if  not A  and not B and c - nums[idx] >=0:
        C = partitions_3(nums, a, b , c- nums[idx], idx - 1)
    return  A or B or C

S = [7, 3, 2, 1, 5, 4, 8]

    # get the sum of all elements in the set
total = sum(S)

# return true if the sum is divisible by 3 and the set `S` can
# be divided into three subsets with an equal sum
print(partitions_3(S,  total // 3, total // 3, total // 3,len(S) - 1))