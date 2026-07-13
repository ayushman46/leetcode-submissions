class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        max_i = 0
        max_diff = 0

        for k in range(len(nums)):
            res = max(res, max_diff * nums[k])
            max_diff = max(max_diff, max_i - nums[k])
            max_i = max(max_i, nums[k])

        return res