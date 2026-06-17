class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=[]
        b=[]
        for i in nums:
            if i<10:
                a.append(i)
            else:
                b.append(i)
        if sum(a)>sum(b) or sum(b)>sum(a):
            return True
        else:
            return False