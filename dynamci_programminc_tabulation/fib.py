def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

def fib_memo(n, memo):
    if n<=1:
        return n
    if n in memo:
        return memo[n]
    memo[n]=fib_memo(n-1, memo)+fib_memo(n-2,memo)
    return memo[n]
print(fib_memo(10,{}))
def fib_tabulation(n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n-1]
print(fib_tabulation(10))