class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=0
        stack=[]
        for ele in s:
            if ele==')':
                if len(stack)>0 and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(ele)
            else:
                stack.append(ele)
        return len(stack)
