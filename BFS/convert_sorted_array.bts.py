# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inser_binary(self,node,val):
        new_node=TreeNode
        if node.val<val:
            node.right=new_node
        else:
            node.right = new_node
        return  node

    def sortedArrayToBST(self, nums):
        root_Val=nums[int(len(nums)/2)]
