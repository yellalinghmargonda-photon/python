from typing import List, Optional


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, arr: List[Optional[int]]) -> Optional[TreeNode]:
        if not arr:
            return None

        root = TreeNode(arr[0])  # First element is the root
        queue = [root]  # Initialize a queue for level order construction
        i = 1  # Start from the second element in the list

        while i < len(arr):
            node = queue.pop(0)  # Get the next node to assign children

            # If there's a valid left child, create it and add it to the queue
            if arr[i] is not None:
                node.left = TreeNode(arr[i])
                queue.append(node.left)
            i += 1

            # If there's a valid right child, create it and add it to the queue
            if i < len(arr) and arr[i] is not None:
                node.right = TreeNode(arr[i])
                queue.append(node.right)
            i += 1

        return root


# Example Usage:
arr = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
solution = Solution()
root = solution.createBinaryTree(arr)




# Function for inorder traversal to check the created tree (Optional)
class Solution:
    def ansistor(self,node,p,q):
        if node.val==p or node.val==q:
            return node
        left= self.ansistor(node.left,p,q)
        right = self.ansistor(node.right, p, q)

        if left and right:
            return node

        if not left and right:
            return right
        else:
            return left

