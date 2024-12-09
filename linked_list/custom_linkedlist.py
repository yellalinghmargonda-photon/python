class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class cll:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def insert_first(self, data):
        node=Node(data)
        node.next=self.head
        self.head=node
        if not self.tail:
            self.tail=self.head
        self.size+=1

    def insert_last(self, data):
        if (self.tail==None):
            self.insert_first(data)
            return
        node=Node(data)
        self.tail.next=node
        self.tail=node
        self.size+=1

    def insert_index(self,data,index):
        if index < 0 or index > self.size:  # Ensure index is valid
            print("Index out of bounds")
            return
        if index==0:
            self.insert_first(data)
            return
        if index==self.size:
            self.insert_last(data)
            return
        temp=self.head
        for i in range(index-1):
            temp=temp.next
        new_node= Node(data)
        new_node.next=temp.next
        temp.next=new_node
        self.size+=1


    def deletefirst(self):
        if not self.head:
            return None
        val = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return val

    def get(self, num):
        temp=self.head
        for _ in range(num):
            temp=temp.next
        return  temp


    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.value, end='->')
            temp=temp.next
        print('END')
    def deleteLast(self):
        if self.size <= 1:
            return self.delete_first()
        node=self.get(self.size-2)
        val=self.tail.value
        self.tail=node
        self.tail.next=None
        self.size-=1
        return val
    def delete_index(self, index):
        if index < 0 or index > self.size:  # Ensure index is valid
            print("Index out of bounds")
            return
        if index==0:
            return self.deletefirst()
        if index==self.size:
            return self.deleteLast()
        node=self.get(index-1)
        val=node.value
        prv_node=self.get(index-2)
        nxt_node = self.get(index)
        prv_node.next=nxt_node
        self.size-=1
        return  val



lLi=cll()
lLi.insert_first(1)
lLi.insert_first(2)
lLi.insert_last(3)
lLi.display()
lLi.insert_index(9,2)
print('sadasd')
lLi.display()
a=lLi.delete_index(5)
print(a)
lLi.display()