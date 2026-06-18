class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                delL,delR = s[l+1 : r+1], s[l:r]
                return (delL==delL[::-1] or delR==delR[::-1])
            l+=1
            r-=1
        return True
        