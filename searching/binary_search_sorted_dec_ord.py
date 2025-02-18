def bin_ser(array: list, start:int,end:int, target:int)->int:
    if start > end:  # Base case: target is not in the array
        return -1
    mid=start+(end-start)//2
    if array[mid]==target:
        return mid
    if array[mid]>target:
        return bin_ser(array, mid + 1, end, target)
    else:
        return bin_ser(array, start, mid - 1, target)

array=[9,5,4,3,2,1,-1]
index=bin_ser(array,0,len(array)-1,2)
print(index)