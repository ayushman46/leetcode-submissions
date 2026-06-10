class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []

        a = b = 0
        i = 0
        res = []

        while i + 1 < len(nums):
            if nums[i + 1] - nums[i] == 1:
                b += 1
            else:
                if a == b:
                    res.append(str(nums[a]))
                else:
                    res.append(str(nums[a]) + "->" + str(nums[b]))

                a, b = b+1, b+1

            i += 1

        # Process the last range
        if a == b:
            res.append(str(nums[a]))
        else:
            res.append(str(nums[a]) + "->" + str(nums[b]))

        return res