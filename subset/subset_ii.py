def subset(arr,ans,idx):
    if idx==len(arr):
        return [ans[:]]
    ans.append(arr[idx])
    left=subset(arr,ans,idx+1)
    ans.pop()
    while idx+1<len(arr) and arr[idx]==arr[idx+1]:
        idx=idx+1
    right=subset(arr,ans,idx+1)
    return left+right
reuslt=subset([1,2,3],[],0)
print(reuslt)
