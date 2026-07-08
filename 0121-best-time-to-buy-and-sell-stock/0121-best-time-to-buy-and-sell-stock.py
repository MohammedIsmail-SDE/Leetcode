class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        profit=0
        min_price=prices[0]
        for price in prices:
            if price<min_price:
                min_price=price

            if price-min_price>profit:
                profit=price-min_price
        return profit



        