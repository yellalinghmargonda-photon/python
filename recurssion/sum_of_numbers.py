def sum_of_nnumber(n: int)-> int:
    if n<=1:
        return n
    return n+sum_of_nnumber(n-1)
print(sum_of_nnumber(5e))