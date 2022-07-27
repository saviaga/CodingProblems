class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cheapest = float("inf")
        max_profit = 0
        
        for i in range(len(prices)):
            cheapest = min(cheapest,prices[i])
            max_profit = max(max_profit,prices[i] - cheapest)
           # if prices[i] < cheapest:
           #     cheapest = prices[i]
           # elif prices[i] - cheapest > max_profit:
           #     max_profit = prices[i] - cheapest
        return max_profit
            
            
        