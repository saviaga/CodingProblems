class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_buy = 0
        max_profit = 0
        start = 0
        for end in range(len(prices)):
            if prices[start] < prices[end]:
                max_profit = max(max_profit, prices[end] - prices[start])
            
            else:
                start = end
        return max_profit
            
            