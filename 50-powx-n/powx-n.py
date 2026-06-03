class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x>0:
            return x**n
        else:
            sign=-1
            if n%2!=0:
                return sign*(abs(x)**n)
            else:
                return abs(x)**n