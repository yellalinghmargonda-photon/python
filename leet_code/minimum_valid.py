#https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/submissions/1478849354/

#solution is similar to the valid parathesis only difference is we push openning brace on to stack even if we don't find any closiing brach on top of stack

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for ele in s:
            if ele ==')':
                if len(stack)>0 and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(ele)
            else:
                stack.append(ele)
        return len(stack)