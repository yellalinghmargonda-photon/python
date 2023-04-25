def linear_search(arr,index,target):
    if index>len(arr)-1:
        return -1
    if target==arr[index]:
        return index
    else:
        return linear_search(arr,index+1,target)

def linear_search_flag(arr,index,target):
    if index>len(arr)-1:
        return False
    if target==arr[index]:
        return True
    else:
        return linear_search_flag(arr,index+1,target)

def linear_search_flag_last(arr,index,target):
    if index<0:
        return False
    if target==arr[index]:
        return True
    else:
        return linear_search_flag(arr,index-1,target)