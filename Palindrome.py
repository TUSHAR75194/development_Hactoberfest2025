class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            r=0
            num=x
            while x!=0:
                r=r*10+x%10
                x=x//10
            return r==num
