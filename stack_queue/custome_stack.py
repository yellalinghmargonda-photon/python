from custome_exception import CustomErrorWithDetails

class custom_stack:
    def __init__(self, ptr=0, size=3):
        self.size = size
        self.list = [None] * self.size
        self.ptr = ptr

    def isfull(self):
        # Check if the stack is full
        return self.ptr == self.size

    def isempty(self):
        # Check if the stack is empty
        return self.ptr == 0

    def insert(self, item):
        # Check if stack is full before inserting
        self.isfull()
        self.list[self.ptr] = item
        self.ptr += 1
        return self.list

    def remove(self):
        # Check if stack is empty before removing
        self.isempty()
        self.ptr -= 1
        item = self.list[self.ptr]
        self.list[self.ptr] = None  # Clear the spot after removing
        return item

    def peek(self):
        # Check if stack is empty before peeking
        self.isempty()
        return self.list[self.ptr - 1]

