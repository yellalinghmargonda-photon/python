import time
start_time = time.time()

def bestComb(target, array):
    if target==0: return []
    if target <0: return None
    shortcom=None
    for ele in array:
        restremaing=bestComb(target-ele,array)
        if restremaing is not  None:
            com = restremaing+[ele]
            if shortcom is None or len(com)<len(shortcom):
                shortcom=com
    return shortcom

print(bestComb(30,[5,3,6,2,8]))
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()


def bestComb(target, array, memo={}):
    if target==0: return []
    if target <0: return None
    if target in memo:
        return memo[target]
    shortcom=None
    for ele in array:
        restremaing=bestComb(target-ele,array)
        if restremaing is not  None:
            com = restremaing+[ele]
            if shortcom is None or len(com)<len(shortcom):
                shortcom=com
    memo[target]=shortcom
    return shortcom
print(bestComb(30,[5,3,6,2,8]))

print("--- %s seconds ---" % (time.time() - start_time))