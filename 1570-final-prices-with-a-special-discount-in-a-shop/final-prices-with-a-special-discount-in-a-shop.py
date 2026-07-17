class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        l,r=0,1
        
        while l<len(prices):
            if r<len(prices):

                if prices[r]<=prices[l]:
                    prices[l]=prices[l]-prices[r]
                    l+=1
                    r=l+1
                else:
                    r+=1
            else:
                l+=1
                r=l+1
        return prices
        
