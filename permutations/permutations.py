temp=[]
def permu(p, up):
    if len(up)==0:
        return [p]
    ch=up[0]
    res=[]
    for i in range(0, len(p)+1):
        r=permu(p[0:i]+ch+p[i::],up[1::])
        res.extend(r)
    return  res
temp=permu('','abc')
print((temp))

def permu2(p, up):
    if len(up)==0:
        return [p]
    ch=up[0]
    res=[]
    for i in range(0, len(p)+1):
        r=permu2(p[0:i]+[ch]+p[i::],up[1::])
        res.extend(r)
    return  res
temp=permu2([],[1,2,3])
print((temp))


def backtrack_permutations(nums, path, used, result):
    # Base case: If the path contains all elements, it's a valid permutation
    if len(path) == len(nums):
        result.append(path[:])  # Add a copy of the path to the result
        return

    # Iterate through all elements
    for i in range(len(nums)):
        if used[i]:  # Skip if this element is already used in the current path
            continue

        # Choose the current element
        path.append(nums[i])
        used[i] = True  # Mark this element as used

        # Explore further
        backtrack_permutations(nums, path, used, result)

        # Backtrack: Undo the choice
        path.pop()
        used[i] = False


def permutations(nums):
    result = []
    backtrack_permutations(nums, [], [False] * len(nums), result)
    return result


# Example Usage
nums = [1, 2, 3]
all_permutations = permutations(nums)
print(all_permutations)
