class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort()
        if nums[0]+nums[1]<=nums[2]:
            return "none"
        else:
            a=set(nums)
            if len(a)==1:
                return "equilateral"
            if len(a)==2:
                return "isosceles"
            elif len(a)==3:
                return "scalene"