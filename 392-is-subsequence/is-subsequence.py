class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i,j=0,0
        count=0
        s=list(s)
        t=list(t)
        res=[]
        
        while count<len(s):
            if i>=len(t):
                return False
            if t[i]==s[j]:
                count+=1
                res.append(i)
                j+=1
                i+=1
            else:
                i+=1
        if sorted(res)==res:
            return True
        else:
            return False

        
