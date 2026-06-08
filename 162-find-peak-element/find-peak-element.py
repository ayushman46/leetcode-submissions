class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        if len(nums)==1:
            return 0
        if len(nums)==2:
            if nums[-1]>nums[0]:
                return 1
            else:
                return 0
        while i+1 < len(nums):
            if nums[i]-nums[i+1]>=1 and nums[i]-nums[i-1]>=1:
                return i
            else:
                i+=1
        if nums[-1]>nums[len(nums)-2]:
            return len(nums)-1
        else:
            return 0
        
                