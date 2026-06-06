class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a=list(s)
        b=list(t)
        if len(a)!=len(b):
            return False
        if sorted(a)==sorted(b):
            return True
        else:
            return False