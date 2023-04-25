def merge_sort(array):
    if len(array)==1 or len(array)==0:
        return array
    array_length=len(array)
    mid=int(array_length/2)
    leftarray=merge_sort(array[0:mid])
    righarray=merge_sort(array[mid:])
    newarray=merge(leftarray,righarray)
    return newarray

def merge(left,right):
    new_list=[]
    i=0
    j=0
    while(i<len(left) and j<len(right)):
        if (left[i]<right[j]):
            new_list.append(left[i])
            i=i+1
        else:
            new_list.append(right[j])
            j=j+1
    if i<len(left):
        new_list.extend(left[i:])
    if j<len(right):
        new_list.extend(right[j:])
    return new_list