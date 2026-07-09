class Solution:
    def twoSum(self, numbers, target):

        a={}
        for i,n in enumerate(numbers):
            dif=target-n
            if dif in a:
                return [a[dif]+1,i+1]
            else:
                a[n]=i
       