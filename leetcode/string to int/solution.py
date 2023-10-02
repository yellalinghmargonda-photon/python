import re
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        x = re.search(r"^(-?[+]?\d+\s?)", s)
        if x == None:
            return 0
        pos = x.span()
        s = s[pos[0]:pos[1]]
        y = re.search(r"\d+", s)
        if y.span()[0]>1:
            return 0
        if s[0] == '-':
            sign = -1
            s = s[1::]
        else:
            sign = 1
        s = int(s) * sign
        if s < -2147483648:
            return -2147483648
        elif s > 2147483647:
            return 2147483647
        else:
            return s

        