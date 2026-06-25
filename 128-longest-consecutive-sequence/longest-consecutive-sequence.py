class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums))
        count=1
        i=0
        maxi=1
        if len(nums)== 0:
            return 0
        while i<len(nums)-1:

            if nums[i+1]-nums[i]==1:
                count+=1
                
                
            else:
                
                count=1
            maxi=max(count,maxi)
            i+=1
        return maxi
            