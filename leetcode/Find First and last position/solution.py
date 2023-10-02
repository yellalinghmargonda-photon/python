class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start_pos=-1
        end_pos=-1
        update_start_pos_flag=True
        update_end_pos_flag=True
        
        for i,ele in enumerate(nums):
            if ele==target and update_start_pos_flag==True:
                start_pos=i
                end_pos=i
                update_start_pos_flag=False
            elif ele==target and update_start_pos_flag==False:
                end_pos=i
        return [start_pos,end_pos]
        