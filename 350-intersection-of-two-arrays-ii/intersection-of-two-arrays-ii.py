class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        

        count1={}
        count2={}
        for i in nums1:
            if i not in count1:
                count1[i]=1
            else:
                count1[i]+=1
        for i in nums2:
            if i not in count2:
                count2[i]=1
            else:
                count2[i]+=1

        


        a=min(len(nums1),len(nums2))
        res=[]

        if a == len(nums2):
            for i in range(len(nums2)):
                if nums2[i] in count1 and count1[nums2[i]] > 0:
                    res.append(nums2[i])
                    count1[nums2[i]] -= 1
        else:
            for i in range(len(nums1)):
                if nums1[i] in count2 and count2[nums1[i]] > 0:
                    res.append(nums1[i])
                    count2[nums1[i]] -= 1

        return res
 
        