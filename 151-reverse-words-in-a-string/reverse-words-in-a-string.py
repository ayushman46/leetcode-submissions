class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s.strip()
        a=s.split()
        
        
        b=a[::-1]
        return " ".join(b)