class max_heap:
    def __init__(self):
        self.heap=[]
    def prnt_idx(self, idx):
        return (idx-1)//2
    def left_idx(self, idx):
        return idx*2+1
    def right_idx(self, idx):
        return idx * 2 + 2

    def swap(self, i,j):
        self.heap[i], self.heap[j]=self.heap[j],self.heap[i]
    def hepfy_up(self, idx):
        while idx>0:
            prnt=self.prnt_idx(idx)
            if self.heap[idx]>self.heap[prnt]:
                self.swap(idx,prnt)
                idx=prnt
            else:
                break
    def hepfy_dwn(self, idx):
        while True:
            largest=idx
            left=self.left_idx(idx)
            right=self.right_idx(idx)
            if left<len(self.heap) and self.heap[left]>self.heap[idx]:
                largest=left
            if right < len(self.heap) and self.heap[right] > self.heap[idx]:
                largest = right
            if largest != idx:
                self.swap(idx, largest)
                idx = largest
            else:
                break


    def insert(self,val):
        self.heap.append(val)
        self.hepfy_up(len(self.heap)-1)


    def remove(self):
        if len(self.heap)==0:
            return 0
        if len(self.heap)==1:
            return self.heap.pop()
        root=self.heap[0]
        self.heap[0] = self.heap.pop()  # Replace root with the last element
        self.hepfy_dwn(0)
        return root
    def __len__(self):
        """Return the number of elements in the heap."""
        return len(self.heap)

    def __bool__(self):
        """Return True if the heap is not empty."""
        return len(self.heap) > 0
heap = max_heap()
print(bool(heap))

for ele in [2, 7, 4, 1, 8, 1]:
    heap.insert(ele)

# Process elements until only one or no stone is left
while len(heap) > 1:
    stone1 = heap.remove()  # Largest stone
    stone2 = heap.remove()  # Second largest stone
    diff = abs(stone1 - stone2)
    if diff > 0:  # Insert the difference back if not zero
        heap.insert(diff)

# Output the weight of the last stone or 0 if no stones remain
print(heap.remove() if len(heap) > 0 else 0)

