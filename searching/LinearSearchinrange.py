def LinearSearchInRange(array:list,start:int,end:int,item:int)-> int:
    for i in range(start,end):
        if array[i]==item:
            return i
    return -1
print(LinearSearchInRange([1,2,34,5,6,7,8,9],0,4,6))