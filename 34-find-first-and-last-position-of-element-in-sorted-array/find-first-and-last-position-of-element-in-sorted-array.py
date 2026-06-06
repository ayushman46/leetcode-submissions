class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
        if len(res)==0:
            return [-1,-1]
        else:
            return [res[0],res[-1]]
