class custom_queue():
    def __init__(self, ptr=0,size=3):
        self.size = size
        self.list = [None]*self.size
        self.ptr=ptr
    def isfull(self):
        return self.ptr == self.size

    def isempty(self):
        return self.ptr==0
    def insert(self, item):
        self.isfull()
        self.list[self.ptr]=item
        self.ptr=self.ptr+1
        return  True

    def remove(self):

        if self.isempty():
             raise Exception("CANNOT REMOVE FROM AND EMPTY que")

        item=self.list[0]
        self.list=[ele for ele in self.list[1::]]
        self.ptr=self.ptr-1
        print(f"updated list {self.list}")
        return  self.list
    def peek(self):
        if self.isempty():
            raise Exception(" stack is empty")
        return self.list[self.ptr]
    def display(self):
        print(self.list)

c_stack = custom_queue()
r=c_stack.insert(10)
c_stack.display()
r=c_stack.insert(12)
c_stack.display()
r=c_stack.insert(13)
c_stack.display()
r=c_stack.remove()
c_stack.display()