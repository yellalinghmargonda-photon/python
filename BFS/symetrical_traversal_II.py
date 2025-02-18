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
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if (not root.left and root.right) or (not root.right and root.left):
            return False

        queue=[root.left, root.right]
        while queue:
            current_result=[]
            size=len(queue)
            for i in range(size):
                left = queue.pop(0)
                right = queue.pop(0)
                if  (not left and right) or (left and not right) :
                    return False
                if not left and not right:
                    pass
                if left.val!= right.val:
                    return False
                queue.append(left.left)
                queue.append(right.right)
                queue.append(left.right)
                queue.append(right.left)

        return True
