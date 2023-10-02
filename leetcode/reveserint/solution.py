class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num=x
        sum=0
        multiplier=10
        if num<0:
            sign=-1
        else:
            sign=1
        num=num*sign
        while num>0:
            rem=num%10
            num=int(num/10)
            sum=sum*multiplier+rem 
        sum=sum*sign    
        if -2147483648 <=sum<= 2147483647:
            return sum
        else:
            return 0
        