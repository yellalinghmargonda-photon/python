# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#https://leetcode.com/problems/binary-tree-level-order-traversal/
#https://leetcode.com/problems/binary-tree-level-order-traversal/
class Solution:
    def levelOrder(self, root):
        result=[]
        queue=[root]
        while queue:
            current_result=[]
            size=len(queue)
            for i in range(size):
                node = queue.pop(0)
                current_result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            avg=sum(current_result)/len(current_result)
            result.append(avg)
        return result
