def quick_sort(array):
    if len(array) <= 1:  # Base case
        return array
    pivot = array[len(array) // 2]  # Choose the middle element as the pivot
    left = [x for x in array if x < pivot]  # Elements less than pivot
    middle = [x for x in array if x == pivot]  # Elements equal to pivot
    right = [x for x in array if x > pivot]  # Elements greater than pivot
    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort and combine

# Example Usage
array = [8, 3, 7, 6, 2, 5]
sorted_array = quick_sort(array)
print(sorted_array)  # Output: [2, 3, 5, 6, 7, 8]
