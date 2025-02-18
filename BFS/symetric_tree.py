# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#https://leetcode.com/problems/binary-tree-level-order-traversal/
#https://leetcode.com/problems/binary-tree-level-order-traversal/
class Solution:
    def symmetric(self,L):
        for i in range(len(L)):
            if L[i] != L[len(L) - i - 1]:
                return False
        else:
            return True

    def levelOrder(self, root):
        result=[]
        queue=[root]
        while queue:
            current_result=[]
            size=len(queue)
            for i in range(size):

                node = queue.pop(0)
                if node:
                    current_result.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    else:
                        queue.append(None)
                    if node.right:
                        queue.append(node.right)
                    else:
                        queue.append(None)
                else:
                    current_result.append(None)
            sym_val= self.symmetric(current_result)
            if not sym_val:
                return False

        return True
