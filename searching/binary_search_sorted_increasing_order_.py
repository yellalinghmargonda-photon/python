def bin_ser(array: list, start:int,end:int, target:int)->int:
    if start > end:  # Base case: target is not in the array
        return -1
    mid=start+(end-start)//2
    if array[mid]==target:
        return mid
    if array[mid]>target:
        return bin_ser(array,start,mid-1,target)
    else:
        return bin_ser(array,mid+1,end,target)

array=[1,2,3,4,5,9]
index=bin_ser(array,0,len(array),9)
print(index)