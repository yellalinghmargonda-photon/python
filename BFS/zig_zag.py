# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        result = []
        queue = [root]
        rev = False
        while queue:
            current_result = []
            size = len(queue)
            for i in range(size):
                if rev:
                    node = queue.pop(-1)
                    current_result.append(node.val)
                    if node.right:
                        queue.insert(0, node.right)
                    if node.left:
                        queue.insert(0, node.left)

                else:
                    node = queue.pop(0)
                    current_result.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            result.append(current_result)
            rev = not rev
        return result
root = TreeNode(1)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.zigzagLevelOrder(root))  # Output: 3