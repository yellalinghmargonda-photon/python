target=7
candidates=[2,3,6,7]
def dfs(i, curr, total):
    if total == target:
        return [curr[:]]
    if i >= len(candidates) or total > target:
        return
    curr.append(candidates[i])
    left = dfs(i, curr, total + candidates[i])#including the current
    curr.pop()
    right = dfs(i + 1, curr, total)#not including the current
    if left and right:
        return left+right
    elif left:
        return  left
    elif right:
        return right

res=dfs(0, [], 0)
print(res)