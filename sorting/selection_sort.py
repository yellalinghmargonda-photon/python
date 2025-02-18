def selection_sort(array: list)-> list:
    for i in range(len(array)):
        min_index = i
        for j in range(i,len(array)-1):
            if array[j] < array[min_index]:
                min_index = j
                # Swap the smallest element with the first element of the unsorted portion
            array[i], array[min_index] = array[min_index], array[i]
        array[i], array[min_index]=array[min_index],array[i]
    return array

array=selection_sort([1,5,2,7,3])
print(array)