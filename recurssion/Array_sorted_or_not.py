def sort_validation(array,index):
    if index==len(array)-1:
        return True
    return array[index]<array[index+1] and sort_validation(array,index=index+1)

