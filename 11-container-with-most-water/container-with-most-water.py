class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        area=0
        max=0
        while l<r:
        
            area=min(height[r],height[l])*(r-l)
            if area>max:
                max=area
            
            if height[l]>height[r]:
                r-=1
            else:
                l+=1

        return max
            
        
