def gridTraveller(m,n, memo={}):
    if m==1 and n==1:
        return 1
    if m<=0 or n<=0:
        return 0
    if (m,n) in memo:
        return memo[(m,n)]
    left=gridTraveller(m-1, n,memo)#down
    right=gridTraveller(m, n-1,memo)#right
    memo[(m,n)]=left+right
    return left+right

print(gridTraveller(2,3))