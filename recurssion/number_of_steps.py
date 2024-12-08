def number_steps(n: int, c: int)-> int:
    if n==0:
        return c
    if n%2==0:
        return number_steps(n//2,c+1)
    else:
        return number_steps(n-1, c + 1)
print(number_steps(123,0))