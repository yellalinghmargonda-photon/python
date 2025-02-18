def merg(arr1,arr2):
    n=0
    l=len(arr1)-1
    for i in range(l):
        if arr1[l-i]==0:
            n=n+1
        else:
            break
    i = n-1
    j = len(arr2) - 1  # Last element in arr2
    k = len(arr1) - 1  # Last position in arr1
    while i>=0 and j>=0:
        if arr1[i]>arr2[j]:
            arr1[k]=arr1[i]
            i=i-1
        else:
            arr1[k] = arr2[j]
            j = j - 1
        k=k-1
    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1
arr1 = [1, 3, 5, 7, 0, 0, 0, 0]  # arr1 has enough space to hold arr2's elements
arr2 = [2, 4, 6, 8]
merg(arr1, arr2)  # n=4, m=4 because arr1 has 4 valid elements and arr2 has 4 elements
print(arr1)

