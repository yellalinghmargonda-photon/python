def permu(ans, array, seen,res, index):
    if index==len(array):
        return res.append(ans[:])

    local_seen=set()
    for i in range(len(array)):
        if i not in seen and array[i] not in local_seen:
            local_seen.add(array[i])
            seen.add(i)
            ans.append(array[i])
            permu(ans,array, seen, res, index+1)
            seen.remove(i)
            ans.pop()
    return res
print(permu([], [1,2], set(),[], 0))