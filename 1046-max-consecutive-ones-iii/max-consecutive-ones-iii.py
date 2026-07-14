class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=0
        count=0
        maxl=0
        for r in range(len(nums)):
            if nums[r]==0:
                count+=1
            while count>k:
                if nums[l]==0:
                    count-=1
                l+=1
            maxl=max(maxl,r-l+1)
        return maxl
