class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def climbStairsHelp(i,dp):
            if i<0: return 0
            if i==0 or n==1: return 1
            
            if dp[i]>0:
                return dp[i]
            
            dp[i] = climbStairsHelp(i-1,dp) + climbStairsHelp(i-2,dp)
            return dp[i]
        
        
        
        
        dp = [0]*(n+1)
        return climbStairsHelp(n,dp)
        
        