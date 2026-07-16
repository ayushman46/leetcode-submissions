class Solution(object):
    def maxProfit(self, prices):
        
      
        buy=prices[0]
        
        res=0
        for price in prices:
            if price<buy:
                buy=price
            else:
                profit=price-buy
            res=max(res,profit)
        return res

            

