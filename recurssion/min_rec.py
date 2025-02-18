def min_rec(a,n):
    if n==1:
        return a[0]
    return min(a[n-1],min_rec(a, n-1))

A = [1, 4, 45, 6, -50, 10, 2]
n = len(A)
min_rec(A, n)