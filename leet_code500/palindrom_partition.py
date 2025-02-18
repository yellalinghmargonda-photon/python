def palindrom_partition(remaining, ans, result, idx, n):
    if len(remaining) == 0:
        result.append(ans[:])  # Add a copy of the answer to results
        return

    for i in range(len(remaining)):
        prefix = remaining[:i + 1]  # Take a prefix from start to i
        if prefix == prefix[::-1]:  # Check if it's a palindrome
            ans.append(prefix)  # Choose this partition
            palindrom_partition(remaining[i + 1:], ans, result, idx, n)  # Explore further
            ans.pop()  # Backtrack

    return result  # Return final result


# Test case
print(palindrom_partition('aabb', [], [], 0, 4))
