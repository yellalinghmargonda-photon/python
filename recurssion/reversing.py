def rever(n: int,rev: int) -> int:
    if n==0:
        return rev
    else:
        rev = rev * 10 + n % 10
        return rever(n//10, rev)

print(rever(123,0))
