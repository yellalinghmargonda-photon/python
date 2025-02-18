# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.daimeter = 0  # Initialize the diameter at the class level

    def height(self, node):
        if node is None:
            return 0  # Base case: height of an empty tree is 0

        # Recursively calculate the height of the left and right subtrees
        lh = self.height(node.left)
        rh = self.height(node.right)

        # Update the diameter (number of edges in the longest path)
        self.daimeter = max(self.daimeter, lh + rh)  # Note: No +1 for edges

        # Return height of the current subtree
        return max(lh, rh) + 1  # +1 for the current node's edge

    def diameterOfBinaryTree(self, root):
        self.height(root)  # Calculate height to update diameter
        return self.daimeter  # Return the maximum diameter
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
print(sol.diameterOfBinaryTree(root))  # Output: 3