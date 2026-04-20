class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr=0
        max=nums[0]
        for i in range(len(nums)):
            curr+=nums[i]
            if curr>max:
                max=curr
            if curr<=0:
                curr=0
        return max