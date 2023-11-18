class Solution(object):
    def helper(self, n,list_num):
        sum = 0
        while n > 0:
            n, remainder = divmod(n, 10)
            sum = sum + remainder ** 2
        if sum in list_num:
            return False
        elif sum==1:
            return True
        else:
            list_num.append(sum)
            return self.helper(sum,list_num)

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.helper(n,list_num=[])
    