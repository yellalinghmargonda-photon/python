points = [(0, 0), (1, 2), (3, 1)]
ad_list={node:[] for node in points}
n=len(points)
for i in range(n):
    x1, y1 = points[i]
    for j in range(n):
        if i!=j:
            x2, y2 = points[j]
            dis=abs((x1-x2)+(y1-y2))
            ad_list[points[i]].append((points[j],dis))
print(ad_list)

import heapq

# Example list to represent a heap
heap = [3, 5, 7, 9, 2]

# Push a new item into the heap
heapq.heappush(heap, 1)

# Output the updated heap
print(heap)
