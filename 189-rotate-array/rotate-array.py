class Solution(object):
    def rotate(self, nums, k):
        a=k%len(nums)
        r=len(nums)-a
        temp=nums[r:]
        nums[r:]=nums[:r]
        nums[:r]=temp
        
        




       