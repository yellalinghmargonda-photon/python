def subset(arr, ans, idx):
    if idx == len(arr):
        return [ans[:]]  # Return a copy of the current subset

    # Include the current element
    ans.append(arr[idx])
    include = subset(arr, ans, idx + 1)
    # Backtrack by removing the last element
    ans.pop()
    while idx+1<len(arr) and arr[idx]==arr[idx+1]:
        idx=idx+1
    exclude = subset(arr, ans, idx + 1)

    # Combine the results from including and excluding the current element
    return include + exclude

# Example usage
result = subset([1, 2, 3], [], 0)
print(result)
