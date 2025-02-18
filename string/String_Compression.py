def compress(chars) :
    temp = {}
    keys = []
    for ele in chars:
        if ele in temp:
            temp[ele] = temp[ele] + 1
        else:
            temp[ele] = 1
            keys.append(ele)
    res = []
    for ele in keys:
        if temp[ele]==1:
            res.append(ele)
        else:
            res.append(ele)
            for s in str(temp[ele]):
                res.append(s)
    return res
res=compress(["a","b","b","c","c","c","c","c","c","c","c","c","c","c","c"])
print(res)