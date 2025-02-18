res=[]

def subset(arr, ans, idx, target):
    if target == 0:
        res.append(ans[:]) # Return a copy of the current subset
    if target<0 or idx >= len(arr):
        return
    # Include the current element
    ans.append(arr[idx])
    subset(arr, ans, idx + 1, target-arr[idx])
    # Backtrack by removing the last element
    ans.pop()
    while idx+1<len(arr) and arr[idx]==arr[idx+1]:
        idx=idx+1
    subset(arr, ans, idx + 1,target)


# Example usage
arr=[10,1,2,7,6,1,5]
arr.sort()
result = subset(arr, [], 0,8)
print(res)

