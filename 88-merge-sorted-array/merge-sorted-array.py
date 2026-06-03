class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        a=[]
        b=[]
        res=[]
        for i in range(m):
            a.append(nums1[i])
        for j in range(n):
            b.append(nums2[j])
        i,j=0,0
        while i<m and j<n:
            if a[i]<b[j]:
                res.append(a[i])
                i+=1
            else:
                res.append(b[j])
                j+=1
        res.extend(a[i:])
        res.extend(b[j:])
        
        for k in range(m+n):
            nums1[k]=res[k]
            