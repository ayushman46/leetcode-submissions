class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        res=[]
        if len(s)<3:
            return 0
        while i+3!=len(s)+1:
            res.append(s[i:i+3])
            i+=1
        count=0
        for i in res:
            if len(set(i))==3:
                count+=1
        return count
