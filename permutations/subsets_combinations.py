def subsets_of_three(arr, idx, current, res):
    # Base case: If the current subset has 3 elements, add it to the result
    if len(current) == 3:
        res.append(current[:])
        return

    # Iterate over the array to select elements for the subset
    for i in range(idx, len(arr)):
        # Include the current element
        current.append(arr[i])
        # Recurse with the next index
        subsets_of_three(arr, i + 1, current, res)
        # Backtrack: Remove the last element to explore other possibilities
        current.pop()
    return res

# Example Usage
arr = [1, 2, 3]
result = subsets_of_three(arr, 0, [], [])
print("Subsets of 3 elements:", result)
