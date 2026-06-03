class Solution(object):
    def majorityElement(self, nums):
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
        max=0
        b=0
        for i in count:
            if count[i]>max:
                max=count[i]
                b=i
        return b

            