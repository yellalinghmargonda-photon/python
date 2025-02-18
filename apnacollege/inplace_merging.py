def merging(nums1, nums2):
    # Initialize pointers for nums1, nums2, and the end of the merged array
    i, j, k = len(nums1) - len(nums2) - 1, len(nums2) - 1, len(nums1) - 1

    # Merge the arrays from the end to the beginning
    print(i,j,k)
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        print(nums1,nums2,i,j)
        k -= 1

    # If there are remaining elements in nums2, add them to nums1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1

# Example Usage:
nums1 = [1, 2, 3, 0, 0, 0]  # nums1 has enough space for nums2
nums2 = [2, 5, 6]
result = merging(nums1, nums2)
print(result)
