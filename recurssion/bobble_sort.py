
def swap_fun(array,i,j):
    array[j],array[i]=array[i],array[j]

def bobble_sort(array,r,c):
    if(r==0):
        return
    if(c<r):
        if(array[c]>array[c+1]):
            swap_fun(array,c,c+1)
        bobble_sort(array,r,c+1)
    else:
        bobble_sort(array, r-1, c=0)
