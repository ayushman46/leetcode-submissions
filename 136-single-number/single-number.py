class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        a={}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in a:
            if a[i]==1:
                return i