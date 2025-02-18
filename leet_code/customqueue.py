class MyQueue:

    def __init__(self):
        self.size = 3
        self.ptr = 0
        self.array = [None] * self.size

    def isFull(self):
        return self.ptr == self.size - 1

    def resize(self):
        new_size = self.size * 2
        new_array = [None] * new_size
        for i in range(self.ptr):
            new_array[i] = self.array[i]
        self.array = new_array
        self.size = new_size

    def push(self, x: int) -> None:
        if self.isFull():
            self.resize()
        self.array[self.ptr] = x
        self.ptr += 1

    def pop(self) -> int:
        if self.empty():
            raise Exception("CANNOT REMOVE FROM AND EMPTY que")
        item = self.array[0]
        self.array = [ele for ele in self.array[1::]]
        self.array.append(None)
        self.ptr = self.ptr - 1
        return item

    def peek(self) -> int:
        if self.empty():
            return None
        return self.array[0]

    def empty(self) -> bool:
        return self.ptr == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.peek()
# # param_4 = obj.empty()
# ["MyQueue","push","push","pop","push","peek","pop","push","pop"]
# [[],[1],[8],[],[3],[],[],[5],[]]
# obj.push(1)
# obj.push(8)
# obj.pop()
# obj.push(3)
# obj.peek()
# obj.pop()
# obj.push(5)
# obj.pop()

a=[1,2,3,4,5]
print(a.insert(0,2))
print(a)