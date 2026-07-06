class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        l=0
        count={}
        res=0
        for r in range(len(answerKey)):
            count[answerKey[r]]=1+count.get(answerKey[r],0)
            while (r-l+1)-max(count.values())>k:
                
                count[answerKey[l]]-=1
                l+=1
            res=max(res,(r-l+1))
        return res