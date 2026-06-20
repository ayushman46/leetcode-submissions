class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        ans=nums
        ans.extend(nums[::-1])
        return ans
        