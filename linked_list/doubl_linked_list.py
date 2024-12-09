class Node:
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self,data):
        node=Node(data)
        node.next=self.head
        node.prev=None
        if self.head is not None:
            self.head.prev=node
        else:
            self.tail=node
        self.head=node
        self.size+=1
        return True

    def insert_last(self,data):
        node=Node(data)
        node.next=None
        node.prev=self.tail
        if self.tail is not None:
            self.tail.next=node
        else:
            self.head=node
        self.tail=node
        self.size+=1
        return True
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.value,end='->')
            temp=temp.next
        print('END')

lLi=DLL()
lLi.insert_first(1)
lLi.insert_first(2)
lLi.insert_last(3)
lLi.display()