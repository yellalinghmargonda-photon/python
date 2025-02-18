def subsets_iterative(nums):
    """
    Generate all subsets of a list of numbers iteratively.

    Parameters:
    nums (list): The list of numbers for which subsets are to be generated.

    Returns:
    list: A list containing all subsets of the input list.
    """
    # Start with the empty subset
    result = [[]]  # At the beginning, the only subset is the empty subset

    # Iterate over each number in the input list
    for num in nums:
        """
        For each number, take all the existing subsets in the result list and create new subsets
        by adding the current number to each of those subsets. Append these new subsets to the result.
        """
        new_subsets = []  # Temporary list to store newly created subsets
        for subset in result:
            # Create a new subset by adding the current number to an existing subset
            new_subset = subset + [num]
            new_subsets.append(new_subset)
            # print(new_subsets)
        # Add all the newly created subsets to the result list
        result=result+new_subsets

    return result


# Driver code
nums = [1, 2, 3]  +[6]# Example input list
result = subsets_iterative(nums)  # Generate subsets iteratively
print(result)  # Output all subsets
print(nums)
