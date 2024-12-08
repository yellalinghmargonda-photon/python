from custome_stack import  custom_stack
class dynamic_stack(custom_stack):
    def __init__(self, ptr=0, size=3):
        # Initialize using the parent class
        super().__init__(ptr, size)
    def push(self, item):
        if self.isfull():
            self.resize()
        return super().insert(item)

    def resize(self):
        # Double the size of the stack and move all items
        new_size = self.size * 2
        new_list = [None] * new_size
        for i in range(self.ptr):
            new_list[i] = self.list[i]
        self.list = new_list
        self.size = new_size

c_dynmcstack=dynamic_stack()


r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)
r=c_dynmcstack.push(1)
print(r)



