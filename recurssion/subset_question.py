def subset(p,up):
    if(len(up)==0):
        temp_list=[]
        if(len(p)>0):
            temp_list.append(p)
        return temp_list
    ch=up[0]
    up=up[1:]
    list2=subset(p+ch,up)
    list1=subset(p,up)
    list2.extend(list1)
    return list2

