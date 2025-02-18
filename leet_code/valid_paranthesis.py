def isValid(s):
    stack = []
    memo = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    op = ['[', '{', '(']
    for ele in s:
        if ele in op:
            stack.append(ele)
            print(stack)
        else:
            if len(stack) > 0:
                temp = stack.pop()
                print(memo[ele],temp)
                if temp != memo[ele]:
                    return False
            else:
                return False
    return len(stack) == 0
print(isValid('()'))