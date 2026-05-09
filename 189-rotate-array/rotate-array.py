class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        if k == 0:
            return

        start = 0
        count = 0

        while count < n:
            current = start
            prev = nums[start]

            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if current == start:
                    break

            start += 1