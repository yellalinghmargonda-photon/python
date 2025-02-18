def skip(p, up):
    if len(up)==0:
        return p
    ch=up[0]
    print(ch)
    if ch=='a':
        return skip(p,up[1::])
    else:
        return ch+skip(p, up[1::])

print(skip('','sadsakk'))

def skip2(up):
    if len(up)==1:
        return up
    ch=up[0]
    if ch=='a':
        return skip2(up[1::])
    else:
        return ch+skip2(up[1::])
print(skip2('sadsakk'))
