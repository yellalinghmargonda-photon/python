def findMin(array: list):
    min=array[0]
    for i in range(len(array)):
        if min>array[i]:
            min=array[i]
    return min

print(findMin([1,2,3,5,-1,4,5,7]))