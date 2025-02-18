heights = [2,1,5,6,2,3]
n = len(heights)

# Arrays to store the closest smaller bar indices on the left and right
left = [-1] * n
right = [n] * n

# Calculate left[] array: left[i] is the index of the leftmost bar smaller than heights[i]
for i in range(n):
    j = i - 1
    while j >= 0 and heights[j] >= heights[i]:
        j = left[j]
    left[i] = j
print(left)
# Calculate right[] array: right[i] is the index of the rightmost bar smaller than heights[i]
for i in range(n - 2, -1, -1):
    j = i + 1
    while j < n and heights[j] >= heights[i]:
        j = right[j]
    right[i] = j

# Calculate the maximum area for each bar using left[] and right[] arrays
max_area = 0
for i in range(n):
    width = right[i] - left[i] - 1
    max_area = max(max_area, heights[i] * width)
