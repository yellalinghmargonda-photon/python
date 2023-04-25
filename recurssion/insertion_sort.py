
def swap_fun(array,i,j):
    array[j],array[i]=array[i],array[j]

def selection_sort(array,r,c,max_index):
    if(r==0):
        return

    if(c<r):
        if(array[c]>array[max_index]):
            selection_sort(array,r,c+1,c)
        else:
            selection_sort(array, r, c + 1, max_index)
    else:
        swap_fun(array, r-1, max_index)
        selection_sort(array, r-1, c=0,max_index=0)

