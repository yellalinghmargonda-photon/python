class custom_heap:
     def __init__(self):
         self.heap=[]
     def prnt_indx(self, idx):
         return (idx-1)//2
     def left_idx(self, idx):
        return (2*idx+1)
     def right_idx(self, idx):
        return (2*idx+2)
     def swap(self, idx1, idx2):
         self.heap[idx1],self.heap[idx2]=self.heap[idx2],self.heap[idx1]
     def up_hepfy(self, idx):

            while idx>0:
                prnt=self.prnt_indx(idx)
                if self.heap[idx]<self.heap[prnt]:
                    self.swap(idx,prnt)
                else:
                    break



     def insert(self,val):
         self.heap.append(val)
         self.up_hepfy(len(self.heap)-1)

     def remove(self):
         if not self.heap:
            raise IndexError("remove from an empty heap")
         if len(self.heap)==1:
             return self.heap.pop()
         root = self.heap[0]  # Root element to return
         self.heap[0] = self.heap.pop()  # Move the last element to the root
         self.down_hepfy(0)  # Restore heap property
         return root
     def down_hepfy(self, idx):
         while True:
            smallest=idx
            left=self.left_idx(idx)
            right=self.right_idx(idx)
            if left<len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest=left
            if right<len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest=right
            if smallest != idx:
                self.swap(idx, smallest)
                idx = smallest
            else:
                break

heap = custom_heap()

# Insert elements
heap.insert(5)
heap.insert(2)
heap.insert(8)
heap.insert(1)
