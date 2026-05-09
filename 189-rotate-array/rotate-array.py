class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # Handle large k

        # Create a new array to store rotated values
        result = [0] * n

        # Place each element in its new position
        for i in range(n):
            new_index = (i + k) % n
            result[new_index] = nums[i]

        # Copy back to nums (in-place)
        for i in range(n):
            nums[i] = result[i]
        return nums