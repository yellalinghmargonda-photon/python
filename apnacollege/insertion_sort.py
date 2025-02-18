def insertion_sort(arr):
    for i in range(len(arr)-2):
        j=i+1
        while j>0:
            if arr[j]<arr[j-1]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
            j=j-1
    return arr
print(insertion_sort([3,2,9,10]))