class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        
        
        for c in coins:
            for a in range(c,amount+1):
                    
                    dp[a] = min(dp[a],dp[a-c]+1)
                 
       
        if dp[amount]!=amount+1:
            return dp[amount]
        else:
            return -1
        