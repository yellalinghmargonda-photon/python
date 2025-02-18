def count_path(r,c):
    if(r==1 or c==1):
        return 1
    left=count_path(r-1,c)
    right=count_path(r,c-1)
    return left+right
print(count_path(3,3))