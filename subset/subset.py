def subset(p,up):
    if len(up)==0:
        print(p)
        return
    ch=up[0]
    subset(p+ch,up[1::])
    subset(p, up[1::])
# subset('','abc')

def subset2(p,up):
    if len(up)==0:
        return [p]
    ch=up[0]
    left=subset2(p+ch,up[1::])
    right=subset2(p, up[1::])
    return left+right



def subset3(p, up, result):
    if len(up) == 0:
        result.append(p)
        return

    ch = up[0]

    # Include the character and recurse
    subset3(p + ch, up[1:], result)

    # Exclude the character and recurse
    subset3(p, up[1:], result)


# Driver code
result_list = []
subset3('', 'abc', result_list)
print(result_list)
