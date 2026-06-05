class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        a=nums[:n]
        b=nums[n:]
        res=[]
        for i in range(n):
           res.append(a[i])
           res.append(b[i])
        return res
        
