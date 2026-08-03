class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq={}
        a=len(nums)
        for i in range(a):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1  #key -> value
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]    