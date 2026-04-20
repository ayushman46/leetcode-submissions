class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the lowest price seen so far
            if price < min_price:
                min_price = price
            # Calculate profit if we sell today
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit