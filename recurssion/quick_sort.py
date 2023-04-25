def swap(array,i,j):
    array[i],array[j]=array[j],array[i]

def quick_sort(array,low,high):
    if(low>high):
        return
    s=low
    e=high
    m =  int((e + s) / 2)

    pivot = array[m];
    s=low
    e=high
    while(s<=e):
        while(array[s]<pivot):
            s=s+1
        while(array[e]>pivot):
            e=e-1
        if (s<=e):
            swap(array,s,e)
            s=s+1
            e=e-1
    #now pivot is at correct place
    quick_sort(array,low,e)
    quick_sort(array,s,high)
