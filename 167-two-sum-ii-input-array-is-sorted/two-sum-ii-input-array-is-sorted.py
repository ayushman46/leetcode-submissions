class Solution:
    def twoSum(self, numbers, target):

        a={}
        for i,num in enumerate(numbers):
            dif=target-num
            if dif in a:
                return[a[dif]+1,i+1]
            else:
                a[num]=i
        