from collections import defaultdict

def counting_sort_hashmap(arr):
    if not arr:
        return arr  # Handle empty input

    # Step 1: Find min and max values
    min_val, max_val = min(arr), max(arr)

    # Step 2: Count occurrences using a HashMap
    count = defaultdict(int)
    for num in arr:
        count[num] += 1

    # Step 3: Iterate from min_val to max_val and reconstruct the sorted array
    sorted_arr = []
    for num in range(min_val, max_val + 1):  # Loop over max number
        if num in count:  # Add only if num exists in count
            sorted_arr.extend([num] * count[num])

    return sorted_arr

# Example Usage
nums = [4, 2, 2, 8, 3, 3, 1, -2, -1, 0, -2]
sorted_nums = counting_sort_hashmap(nums)
print(sorted_nums)  # Output: [-2, -2, -1, 0, 1, 2, 2, 3, 3, 4, 8]
