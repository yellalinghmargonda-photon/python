def intersection(nums1, nums2):
    new_array=[]
    i,j=0,0
    nums1.sort()
    nums2.sort()
    while i < len(nums1) and j <len(nums2):
        if nums1[i]==nums2[j]:
            new_array.append(nums1[i])
            i+=1
            j+=1
        if i < len(nums1) and j <  len(nums2) and nums1[i]>nums2[j]:
            j+=1
        else:
            i+=1
    return  new_array

[3, 2, 6, 5, 0, 3]
print(intersection([4,9,5],[9,4,9,8,4]))