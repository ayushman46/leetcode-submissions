class Solution(object):
    def findErrorNums(self, nums):
        a = {}
        b = []

        for i in nums:
            if i in a:
                b.append(i)
            else:
                a[i] = 1

        for i in range(1, len(nums) + 1):
            if i not in a:
                b.append(i)

        return b