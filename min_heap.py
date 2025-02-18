class minheap:
    def __init__(self):
        self.ptr=0
        self.size=5
        self.array=[None]*self.size
    def getprnt(self, idx):
        return (idx-1)//2
    def left(self, idx):
        return 2*idx+1
    def right(self, idx):
        return 2*idx+2
    def resize(self):
        new_size=self.size*2
        new_array=[None]*new_size
        for i in range(self.ptr):
            new_array.append(self.array[i])
        self.array=new_array
        self.size=new_size

    def isFull(self):
        return self.ptr==self.size

    def insert(self, val):
        if self.isFull():
            self.resize()
        self.array.append(val)
        self.ptr+=1
    def remove(self):
        ele=self.array.pop()

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def heapfy(self, idx):
        while idx>0:
            prnt=self.getprnt(idx)
            if self.array[idx]<self.array[prnt]:
                self.swap(prnt,idx)
                idx=prnt
            else:
                break