def combination(ans, array, idx, result, k):
    if len(ans)==k:
        result.append(ans[:])
        return
    if idx >= len(array):  # Base case: end of array
        return

        # Include current element
    ans.append(array[idx])
    combination(ans, array, idx + 1, result, k)

    # Exclude current element
    ans.pop()
    combination(ans, array, idx + 1, result, k)

array=[1,2,3,4]
result=[]
print(combination([],array,0,result,2))
print(result)