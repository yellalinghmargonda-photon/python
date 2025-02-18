def booble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1]=array[j+1], array[j]
    return array

array=booble_sort([1,5,2,7,3])
