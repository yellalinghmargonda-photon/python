def parlindrom(s):
    """
    Check if a string is a palindrome.
    """
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def subset(path, remaining, result):
    """
    Recursive function to generate all palindrome partitions.
    """
    # Base case: if no characters are left to process, add the current path to the result.
    if not remaining:
        result.append(path[:])
        return

    # Loop through the remaining string and create partitions.
    for i in range(1, len(remaining) + 1):
        temp=remaining
        l=i

        prefix = temp[:i]  # Take the first i characters as a prefix.
        if parlindrom(prefix):  # Check if the prefix is a palindrome.
            path.append(prefix)  # Add it to the current path.
            subset(path, temp[i:], result)  # Recur with the remaining string.
            l = i
            temp2=remaining
            path.pop()  # Backtrack and remove the last added prefix.


# Example usage
s = "aab"
result=[]
subset([], s, result)
print(result)

