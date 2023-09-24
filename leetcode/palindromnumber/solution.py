class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def rev(num):
            sum=0
            multiplier=10
            while num>0:
                rem=num%10
                num=int(num/10)
                sum=sum*multiplier+rem       
            return sum
        rev_val=rev(x)
        if x<0:
            return False
        elif x-rev_val==0:
            print('here')
            return True
        else:
            return False