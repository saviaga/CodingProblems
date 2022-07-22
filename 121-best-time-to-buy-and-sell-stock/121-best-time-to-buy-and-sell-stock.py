class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_buy = prices[0]
        max_profit = 0
        
        for i in range(1,len(prices)):
            if prices[i] - min_buy > max_profit:
                max_profit = prices[i] - min_buy
            elif prices[i] < min_buy:
                min_buy = prices[i]
        return max_profit
            
            