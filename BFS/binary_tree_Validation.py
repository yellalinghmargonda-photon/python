# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def validation(self, node, low, high):
        if not node:  # Base case: empty node is valid
            return True

        # Check if the current node value is within the valid range
        if not (low < node.val < high):
            return False  # Violation of BST property

        # Recursively validate the left and right subtrees
        return self.validation(node.left, low, node.val) and self.validation(node.right, node.val, high)

    def isValidBST(self, root) -> bool:
        if not root:
            return True
        return self.validation(root, float('-inf'), float('inf'))

t=TreeNode(4)

s=Solution()
out=s.isValidBST(t)
print(out)