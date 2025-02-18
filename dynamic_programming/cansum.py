def canSum(target,array):
    if target==0:
        return True
    if target<0:
        return False
    for ele in array:
            if canSum(target-ele,array):
                return True
    return False

def canSumMemo(target,array,memo={}):
    if target == 0:
        return True
    if target < 0:
        return False
    if target in memo:
        memo[target]

    for ele in array:
        if canSum(target - ele, array):
            memo[target]=True
            return memo[target]

    memo[target]=False
    return memo[target]
print(canSumMemo(3,[7,14]))

