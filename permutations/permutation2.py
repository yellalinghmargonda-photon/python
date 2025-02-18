
def permu(arr,idx,res):
    if idx==len(arr):
        return res.append(arr[:])

    for i in range(idx,len(arr)):
        arr[i],arr[idx]=arr[idx],arr[i]
        permu(arr,idx+1,res)
        arr[i], arr[idx] = arr[idx], arr[i]
    return res

r=permu([1,2,3],0,[])
print(r)
