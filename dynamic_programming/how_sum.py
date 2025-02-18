def howSum(target,array):
    if target==0:
        return []
    if target<0:
        return None
    for ele in array:
            remresult= howSum(target-ele,array)
            if remresult is not None:
                return remresult + [ele]
    return None
# print(howSum(7,[2,2,3]))


def howSum(target,array,memo={}):
    if target==0:
        return []
    if target<0:
        return None
    if target in memo:
        return memo[target]
    for ele in array:
            remresult= howSum(target-ele,array)
            if remresult is not None:
                memo[target]=remresult + [ele]
                return memo[target]
    memo[target]=None
    return memo[target]
print(howSum(7,[2,2,3]))