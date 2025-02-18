def recursive_merge(array, start, end):
    if end-start<=1:
        return
    mid=start+(end-start)//2
    recursive_merge(array,start, mid)
    recursive_merge(array, mid,end)
    mergeInplace(array, start,mid,end)

def mergeInplace(array, start, mid,end):
    i, j=start,mid
    res=[]
    while i<mid and j<end:
        if array[i]<array[j]:
            res.append(array[i])
            i+=1
        else:
            res.append(array[j])
            j+=1
    while i<mid:
        res.append(array[i])
        i+=1
    while j<end:
        res.append(array[j])
        j+=1
    for k in range(len(res)):
        array[start+k]=res[k]



array = [8, 3, 7, 6, 2, 5]

start=0
end=len(array)
sorted_array = recursive_merge(array,start,end)
print(array)

