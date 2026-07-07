class Solution(object):
    def maxProfit(self, prices):
        
      
        profit=0
        buy = prices[0]
        maxi=0
        for price in prices:
            if price<buy:
                buy=price
            else:
                profit=price-buy
                maxi=max(maxi,profit)
        return maxi

        