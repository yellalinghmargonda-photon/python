def permutation(ans, array, res,seen):
    if len(array)==len(ans):
        return res.append(ans[:])

    for i in range(len(array)):
        if array[i] not in seen:
            ans.append(array[i])
            seen.add(array[i])
            permutation(ans,array,res,seen)
            seen.remove(array[i])
            ans.pop()

res=[]
permutation([],[1,2,3],res,set())
print(res)


def permutation(ans, array, res, used):
    if len(ans) == len(array):
        res.append(ans[:])
        return

    for i in range(len(array)):
        if used[i]:  # Skip already used elements
            continue

        # Skip duplicate elements (except for the first occurrence in this level)
        if i > 0 and array[i] == array[i - 1] and not used[i - 1]:
            continue

        ans.append(array[i])
        used[i] = True  # Mark as used
        permutation(ans, array, res, used)
        ans.pop()  # Backtrack
        used[i] = False  # Unmark for next iterations


# Example usage:
array = [1, 1, 2]  # Contains duplicate elements
array.sort()  # Sorting ensures duplicates are adjacent
res = []
used = [False] * len(array)  # Tracks used elements
permutation([], array, res, used)

def permutation_sawp(array, res,idx):
    if len(array)==idx:
        return res.append(array[:])

    for i in range(idx,len(array)):

        array[i],array[idx]=array[idx],array[i]
        permutation_sawp(array,res, idx+1)
        array[idx], array[i] = array[i], array[idx]

res=[]
permutation_sawp([1,2,3],res,0)
print(res)


def permutation(ans, array, res,seen):
    if len(array)==len(ans):
        return res.append(ans[:])
    local_seen=set()
    for i in range(len(array)):
        if i not in seen and array[i] not in local_seen:
            ans.append(array[i])
            seen.add(i)
            local_seen.add(array[i])
            permutation(ans,array,res,seen)
            seen.remove(i)
            local_seen.remove(array[i])
            ans.pop()
