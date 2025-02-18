def permutation(array, ans, result, visited):
    if len(ans) == len(array):
        result.append(ans[:])  # Store a copy of the permutation
        return

    seen = set()  # Track elements used at this recursion level

    for i in range(len(array)):
        if visited[i]:  # Skip already used elements
            continue

        if array[i] in seen:  # Skip duplicate elements in the same recursion level
            continue

        seen.add(array[i])  # Mark element as used at this level
        visited[i] = True  # Mark index as used

        permutation(array, ans + [array[i]], result, visited)  # Recursive call

        visited[i] = False  # Backtrack


def permute_unique(nums):
    result = []
    nums.sort()  # Sort to ensure duplicates are adjacent
    visited = [False] * len(nums)
    permutation(nums, [], result, visited)
    return result


# Example Usage
nums = [1, 1, 2]
print(permute_unique(nums))
