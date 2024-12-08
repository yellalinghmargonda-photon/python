class CircularQueue:
    def __init__(self, start=0, end=0, capacity=5):
        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.start = start
        self.end = end
        self.size = 0  # Keep track of the current number of elements in the queue

    def is_full(self):
        return self.size == self.capacity  # The queue is full when size equals capacity

    def is_empty(self):
        return self.size == 0  # The queue is empty when size is 0

    def push(self, item):
        if self.is_full():
            print(f"over flow occured {self.size}")
            self.resize()
        self.queue[self.end] = item
        self.end = (self.end + 1) % self.capacity  # Circular increment
        self.size += 1  # Increment the size after pushing an item

    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is empty")  # Raise an error if trying to pop from an empty queue
        item = self.queue[self.start]
        self.queue[self.start] = None  # Optional: Clear the popped position
        self.start = (self.start + 1) % self.capacity  # Circular increment
        self.size -= 1  # Decrement the size after removing an item
        return item

    def display(self):
        # Displays the elements in the queue in order, considering the circular indexing
        if self.is_empty():
            print("Queue is empty")
        else:
            index = self.start
            elements = []
            for _ in range(self.size):
                elements.append(self.queue[index])
                index = (index + 1) % self.capacity  # Move to the next index circularly
            print("Queue elements:", elements)

    def resize(self):
        new_capacity = self.capacity * 2
        new_queue = [None] * new_capacity
        index = 0

        # Copy elements in order
        for i in range(self.size):
            new_queue[index] = self.queue[(self.start + i) % self.capacity]
            index += 1

        # Update the queue attributes
        self.queue = new_queue
        self.start = 0
        self.end = self.size
        self.capacity = new_capacity

    def __str__(self):
        return (
            f"Queue: {self.queue}, "
            f"Start: {self.start}, End: {self.end}, Size: {self.size}"
        )
# Create a CircularQueue with a capacity of 5
cq = CircularQueue(capacity=1)

# Push elements into the queue
cq.push(1)
cq.push(2)
cq.push(3)
cq.display()  # Output: Queue elements: [1, 2, 3]

# Pop an element
cq.pop()
cq.display()  # Output: Queue elements: [2, 3]

# Push more elements
cq.push(4)
cq.push(5)
cq.push(6)
cq.display()  # Output: Queue elements: [2, 3, 4, 5, 6]

# Pop all elements
while not cq.is_empty():
    cq.pop()
cq.display()  # Output: Queue is empty
