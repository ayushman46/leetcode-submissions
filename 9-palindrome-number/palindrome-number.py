class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            a=list(map(int,str(x)))
            b=len(a)
            if a==a[::-1]:
                return True
            else:
                return False