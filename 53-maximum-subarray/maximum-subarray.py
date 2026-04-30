class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr=0
        sum=nums[0]
    
        for i in range(len(nums)):
            curr+=nums[i]
            if curr>sum:
                sum=curr
            if curr<=0:
                curr=0
        return sum
        