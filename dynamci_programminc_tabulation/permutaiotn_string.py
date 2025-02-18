def permutation(array, ans, result, visited):
    if len(ans) == len(array):
        result.append(ans)  # Store permutation as a string
        return
    seen = set()  # Track elements used at this recursion level
    for i in range(len(array)):
        # Skip already visited elements
        if visited[i]:
            continue

        if array[i] in seen:  # Skip duplicate elements in the same recursion level
            continue

        seen.add(array[i])  # Mark element as used at this level

        visited[i] = True  # Mark as used
        permutation(array, ans + array[i], result, visited)  # Add character
        visited[i] = False  # Backtrack


def permute_unique(s):
    result = []
    sorted_s = sorted(s)  # Sort to handle duplicates correctly
    visited = [False] * len(s)  # Track visited characters
    permutation(sorted_s, "", result, visited)
    return result


# Example Usage
nums = "aabc"
print(permute_unique(nums))
