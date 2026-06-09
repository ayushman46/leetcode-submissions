class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=sum(nums)
        s=0
        for i in nums:
            while i>0:
                s+=i%10
                i//=10

        return a-s