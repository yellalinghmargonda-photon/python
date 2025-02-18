"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        level_start = root

        while level_start.left:  # Continue until the last level is reached
            current = level_start

            while current:
                # Connect left child to right child
                current.left.next = current.right

                # Connect right child to the next node's left child, if it exists
                if current.next:
                    current.right.next = current.next.left

                # Move to the next node in the same level
                current = current.next

            # Move down to the next level
            level_start = level_start.left

        return root
