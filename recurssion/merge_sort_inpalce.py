def merge_sort_inpalce(array,s,e):
    if e-s==1:
        return;
    m=int((s+e)/2)
    merge_sort_inpalce(array,s,m)
    merge_sort_inpalce(array,m,e)
    merge_inplace(array,s,m,e)
def merge_inplace(array,s,m,e):
    new_list=[]
    i=s
    j=m
    while(i<m and j<e):
        if (array[i]<array[j]):
            new_list.append(array[i])
            i=i+1
        else:
            new_list.append(array[j])
            j=j+1
    while i<m:
        new_list.append(array[i])
        i=i+1
    while j<e:
        new_list.append(array[j])
        j = j + 1
    for l in range(0,len(new_list)):
        array[s+l]=new_list[l]
list=[3,1,-88,100,8,766,-99]
merge_sort_inpalce(list,s=0,e=len(list))
print(list)

