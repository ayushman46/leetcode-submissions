class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a={}
        res=[]
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in a:
            if a[i]==1:
                res.append(i)
        return res
