class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_recursive(self, current, data, position):
        # Base case: Insert at the position
        if position == 0:
            new_node = Node(data)
            new_node.next = current
            return new_node

        # Recursive case: Move to the next node
        if current is None:
            raise IndexError("Position out of bounds")
        current.next = self.insert_recursive(current.next, data, position - 1)
        return current

    def insert(self, data, position):
        self.head = self.insert_recursive(self.head, data, position)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Usage
ll = LinkedList()
ll.insert(10, 0)  # Insert 10 at position 0
ll.insert(20, 1)  # Insert 20 at position 1
ll.insert(20, 1)  # Insert 20 at position 1
ll.insert(15, 1)  # Insert 15 at position 1
ll.print_list()   # Output: 10 -> 15 -> 20 -> None
ll.insert(33, 2)  # Insert 15 at position 1
ll.print_list()   # Output: 10 -> 15 -> 20 -> None
ll.insert(88, 5)  # Insert 15 at position 1
ll.print_list()   # Output: 10 -> 15 -> 20 -> None