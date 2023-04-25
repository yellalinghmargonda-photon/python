def recursive_sort(inputarray,target,start,end):
    if start>end:
        return -1
    mid=int((end+start)/2)
    if target==inputarray[mid]:
        print(f"found match at  index {mid} and value is {inputarray[mid]}")
        return mid
    if target>inputarray[mid]:
        start=mid+1
        return recursive_sort(inputarray, target, start, end)
    if target<inputarray[mid]:
        end = mid-1
        return recursive_sort(inputarray, target, start, end)


inputarray=[2,3,4,5,6,8,9]
target=5
start=0
end=len(inputarray)-1
index=recursive_sort(inputarray,target, start,end)
print(index)