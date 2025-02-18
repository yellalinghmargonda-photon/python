res=[]
def subseq(ans,input, i):
    if i==len(input):
        return [ans[:]]
    include=subseq(ans+input[i],input, i+1)
    exlude=subseq(ans,input, i+1)
    return include+exlude
print(subseq('','adsf',0))
print(res)