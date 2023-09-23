class Solution(object):
    def twoSum(self, nums, target):
        for i,ele1 in enumerate(nums):
            for j,ele2 in enumerate(nums[i+1:]):
                if ele1+ele2==target:
                    return (i,j+1+i)

        