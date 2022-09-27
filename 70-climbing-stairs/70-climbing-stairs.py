class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def climbStairsHelper(i,n,dp):
            if i>n:
                return 0
            if i==n:
                return 1
            
            
            if dp[i] > 0:
                return dp[i]
            dp[i] = climbStairsHelper(i+1,n,dp) + climbStairsHelper(i+2,n,dp)
            return dp[i]
            
            
            
            
        dp = [0]*(n+1)
        return climbStairsHelper(0,n,dp)
       