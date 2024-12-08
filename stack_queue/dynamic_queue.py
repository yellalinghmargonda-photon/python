from custome_queue import  custom_queue

class dynamic_queue(custom_queue):
    def __int__(self, ptr=0, size=3):
        super.__init__(ptr,size)

    def push(self, item):
        if self.isfull():
            self.resize()
        return super().insert(item)
    def resize(self):
        new_size=self.size*2
        temp=[None]*new_size
        for i in range(self.ptr):
            temp[i] = self.list[i]
        self.list = temp
        self.size = new_size

    def display(self):
        print(self.list)

c_stack = dynamic_queue()
r = c_stack.push(10)
c_stack.display()
r = c_stack.push(12)
c_stack.display()
r = c_stack.push(13)
c_stack.display()
r = c_stack.push(10)
c_stack.display()
r = c_stack.push(12)
c_stack.display()
r = c_stack.push(13)
c_stack.display()
r = c_stack.push(10)
c_stack.display()
r = c_stack.push(12)
c_stack.display()
r = c_stack.push(13)
c_stack.display()
r = c_stack.push(10)
c_stack.display()
r = c_stack.push(12)
c_stack.display()
r = c_stack.push(10)
c_stack.display()
r = c_stack.push(12)
c_stack.display()
r = c_stack.push(13)
c_stack.display()
r = c_stack.push(10)
c_stack.display()
r = c_stack.push(12)
c_stack.display()
r = c_stack.push(13)
c_stack.display()
r = c_stack.push(10)
c_stack.display()
r = c_stack.push(12)
c_stack.display()
r = c_stack.push(13)
c_stack.display()
r = c_stack.push(10)
c_stack.display()
r = c_stack.push(12)
c_stack.display()

r = c_stack.remove()
c_stack.display()