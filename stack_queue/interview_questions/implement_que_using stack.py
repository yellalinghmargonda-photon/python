#leetcode https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:

    def __init__(self):
        self.size = 5
        self.stack = [None] * self.size
        self.ptr = 0
    def isFull(self):
        if self.ptr==self.size:
            self.size=self.size*2
            temp=[None]*self.size # this temp is the second stack
            for i in range(self.ptr):
                temp[i]=self.stack[i]
            self.stack=temp

    def push(self, x: int) -> None:
        self.isFull()
        self.stack[self.ptr] = x
        self.ptr += 1
    def empty(self) -> bool:
        # Check if the stack is empty
        return self.ptr == 0
    def pop(self) -> int:
        if not self.empty():
            item=self.stack[0]
            temp = [None] * self.size
            for i in range(1,self.ptr):
             temp[i-1] = self.stack[i]
            self.stack = temp
            self.ptr=self.ptr-1
            return item
        else:
            return None




    def peek(self) -> int:
        return self.stack[0]


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(2)
# param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2,param_3,param_4)