class CustomHeap:
    def __init__(self):
        """Initialize an empty heap."""
        self.heap = []

    def parent_index(self, idx):
        """Return the index of the parent node."""
        return (idx - 1) // 2

    def left_index(self, idx):
        """Return the index of the left child node."""
        return 2 * idx + 1

    def right_index(self, idx):
        """Return the index of the right child node."""
        return 2 * idx + 2

    def insert(self, val):
        """Insert a value into the heap and restore the max-heap property."""
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def _swap(self, i, j):
        """Swap elements at indices i and j."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, idx):
        """Restore the heap property by sifting up the element at idx."""
        while idx > 0:
            parent = self.parent_index(idx)
            if self.heap[idx] > self.heap[parent]:  # Child is larger than the parent
                self._swap(idx, parent)
                idx = parent
            else:
                break

    def remove(self):
        """Remove and return the largest value (root) from the heap."""
        if not self.heap:
            return 0  # Return 0 if the heap is empty
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Replace root with the last element
        self._sift_down(0)
        return root

    def _sift_down(self, idx):
        """Restore the heap property by sifting down the element at idx."""
        while True:
            largest = idx
            left = self.left_index(idx)
            right = self.right_index(idx)

            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left

            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != idx:
                self._swap(idx, largest)
                idx = largest
            else:
                break

    def peek(self):
        """Return the largest value without removing it."""
        if not self.heap:
            raise IndexError("peek from an empty heap")
        return self.heap[0]

    def __len__(self):
        """Return the number of elements in the heap."""
        return len(self.heap)

    def __bool__(self):
        """Return True if the heap is not empty."""
        return len(self.heap) > 0


# Max-Heap usage for the problem
heap = CustomHeap()

# Insert all elements into the heap
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
