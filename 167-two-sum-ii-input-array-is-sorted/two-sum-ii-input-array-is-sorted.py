class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        a={}
        for i,num in enumerate(numbers):
            diff=target-num
            if diff in a:
                return [a[diff]+1,i+1]
            else:
                a[num]=i