def count_z(n: int, c: int)-> int:
    if n//10==0:
       return c
    if n%10==0:
        return count_z(n//10,c+1)
    else:
        return count_z(n // 10, c )
c_z=count_z(199001000000,0)
print(c_z)