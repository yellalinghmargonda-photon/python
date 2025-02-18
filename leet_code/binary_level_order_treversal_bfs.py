#https://leetcode.com/problems/binary-tree-level-order-traversal/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        queue = [root]
        while queue:
            current_result = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node:
                    current_result.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            # here number of elements in the queue are going to be equal to the number of nodes in the next level

            result.append(current_result)
        return result
