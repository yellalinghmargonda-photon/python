class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # Initial height for a new node is 1

class BST:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def insert(self, val, node=None):
        if node is None:
            if self.root is None:  # Handle inserting into an empty tree
                self.root = Node(val)
                return self.root
            else:
                return Node(val)

        if val < node.val:
            node.left = self.insert(val, node.left)
        elif val > node.val:
            node.right = self.insert(val, node.right)
        # Update the height of the current node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return node

    def display(self, node=None, level=0):
        if node is None and level == 0:
            node = self.root
        if node is not None:
            self.display(node.right, level + 1)
            print(' ' * 4 * level + '->', node.val)
            self.display(node.left, level + 1)

    def search(self, val):
        current = self.root
        while current:
            if val < current.val:
                current = current.left
            elif val > current.val:
                current = current.right
            else:
                return True
        return False
    def node_balaced(self, node=None):
        if node==None or node==self.root :
                return  True
        return (node.left.height-node.right.height)<=1 and self.node_balaced(node.left) and self.node_balaced(node.left)
# Create an instance of the BST
tree = BST()

# Insert some values
values_to_insert = [50, 30, 70, 20, 40, 60, 80]
for value in values_to_insert:
    tree.insert(value, tree.root)

# Display the tree
tree.display()

# Search for a value
print("Search for 40:", tree.search(40))  # Output: True
print("Search for 100:", tree.search(100))  # Output: False
bal=tree.node_balaced()
print(bal)
