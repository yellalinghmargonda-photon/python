def gen_permutation(arr: list) -> list:
    # Base case: if the list is empty, return a list containing an empty list
    if len(arr) == 0:
        return [[]]

    first_element = arr[0]
    remaining_elements = arr[1:]
    # Get permutations of the remaining elements
    perms_of_remaining = gen_permutation(remaining_elements)

    result = []

    # Insert the first element at every possible position in each permutation of the remaining elements
    for perm in perms_of_remaining:
        # Insert the first_element at each possible index in the current permutation
        for i in range(len(perm) + 1):
            result.append(perm[:i] + [first_element] + perm[i:])

    return result


# Example usage
arr = [1, 2, 3]
print(gen_permutation(arr))
