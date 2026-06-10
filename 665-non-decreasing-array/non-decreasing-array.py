class Solution(object):
    def checkPossibility(self, nums):
        count = 0

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1

                if count > 1:
                    return False

                if i > 0 and i < len(nums) - 2:
                    if nums[i - 1] > nums[i + 1] and nums[i] > nums[i + 2]:
                        return False

        return True