class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def insert_first(self, data):
        node=Node(data)
        if self.head is not None:
            node.next=self.head
            self.head=node
            self.tail.next=self.head

        else:
            self.head=node
            self.tail=node
            self.head.next = node
        self.size+=1
        return  True

    def insert_last(self,data):
        node=Node(data)
        if self.tail is not None:
            node.next=self.head
            self.tail.next=node
            self.tail=node
        else:
            self.head = node
            self.tail = node
            node.next = node
        self.size += 1
        return True

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        i=0
        while True:
            i+=1
            print(current.value, end=" -> ")
            current = current.next
            if current == self.head:  # Break when we complete the circle
                break
        print("(back to head)")

# Test the corrected code
cll = CircularLinkedList()
cll.insert_first(1)
cll.insert_first(2)
cll.insert_last(3)
cll.insert_first(9)
cll.insert_first(11)
cll.insert_last(0)
cll.display()

