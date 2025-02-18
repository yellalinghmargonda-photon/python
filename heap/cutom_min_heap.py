class min_heap:
    def __init__(self):
        self.heap=[]
    def prnt_idx(self, idx):
        return (idx - 1) // 2

    def left_idx(self, idx):
        return idx * 2 + 1

    def right_idx(self, idx):
        return idx * 2 + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, idx):
        while idx>0:
            prnt=self.prnt_idx(idx)
            if self.heap[idx]<self.heap[prnt]:
                self.swap(idx, prnt)
                idx=prnt
            else:
                break
    def heapify_down(self, idx):
        while True:
            smallest=idx
            left=self.left_idx(idx)
            right=self.right_idx(idx)
            if left<len(self.heap) and self.heap[left]<self.heap[idx]:
                smallest=left
            if right<len(self.heap) and self.heap[right]<self.heap[idx]:
                smallest=right
            if smallest!=idx:
                self.swap(idx, smallest)
                idx=smallest
            else:
                break

    def insert(self,val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)

    def remove(self):
        if len(self.heap)==0:
            raise IndexError(f"index is out of bound")
        if len(self.heap)==1:
            return self.heap.pop()
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        return root
    def __len__(self):
        """Return the number of elements in the heap."""
        return len(self.heap)

    def __bool__(self):
        """Return True if the heap is not empty."""
        return len(self.heap) > 0


