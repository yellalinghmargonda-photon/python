def par(open, ans,close, n, res):
    if len(ans)==2*n:
        return res.append(''.join(ans[:]))

    if open <n:
        ans.append('(')
        par(open+1,ans, close, n, res)
        ans.pop()
    if close<open:
        ans.append(')')
        par(open, ans, close+1, n, res)
        ans.pop()

res=[]
par(0,[],0,2,res)
print(res)
