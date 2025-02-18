def recursive_merge(array):
    if len(array)==1:
        return  array
    mid=len(array)//2
    left=recursive_merge(array[0:mid])
    right = recursive_merge(array[mid:])
    return merge(left,right)

def merge(left, right):
    res=[]
    i, j=0,0
    while i< len(left)and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    while i < len(left):
        res.append(left[i])
        i+=1

    while j < len(right):
        res.append(right[j])
        j += 1
    return res
array = [8, 3, 7, 6, 2, 5]
sorted_array = recursive_merge(array)
print(sorted_array)  # Output: [2, 3, 5, 6, 7, 8]

