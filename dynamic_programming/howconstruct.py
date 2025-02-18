res=[]
def howconstrucnt(remaining,strs ):
    if len(remaining)==0:
        return 1
    count=0
    for ele in strs:
        if remaining.startswith(ele):
            sufix=remaining[len(ele):]
            cal=howconstrucnt(sufix, strs)
            count=count+cal

    return  count
print(howconstrucnt('purple',['purp','p','ur','le','purpl']))

def howconstrucnt_memo(remaining,strs, memo={}):
    if remaining in memo:
        return memo[remaining]
    if len(remaining)==0:
        return 1

    count=0
    for ele in strs:
        if remaining.startswith(ele):
            sufix=remaining[len(ele):]
            cal=howconstrucnt_memo(sufix, strs,memo)

            count=count+cal
    memo[remaining]=count

    return  memo[remaining]
print(howconstrucnt_memo('purple',['purp','p','ur','le','purpl']))
