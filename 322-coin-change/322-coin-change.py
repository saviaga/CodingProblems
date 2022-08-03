class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for c in coins:
            for i in range(c,amount+1):
                dp[i] = min(dp[i],dp[i-c]+1)
                
        if dp[amount]!=float('inf'):
            return dp[amount]
        else:
            return -1
                
                
            
            