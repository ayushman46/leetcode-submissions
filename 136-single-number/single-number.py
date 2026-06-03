class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]]=1
            else:
                count[nums[i]]+=1
        for i in count:
            if count[i]==1:
                return i
