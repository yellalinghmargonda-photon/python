def climb(n):
    res=[0]*(n+1)
    res[0]=1
    res[1]=1
    res[2] = 2
    for i in range(3,n+1):
        res[i]=res[i-1]+res[i-2]

    return res[n]
print(climb(6))

def climb(n):
    if n==1:
        return  1
    if n==2:
        return 2
    return  climb(n-1)+climb(n-2)
print(climb(3))