class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        g = [0]*(n+1)
        g[0] = 1
        g[1] = 1
        
        for i in range(2,n+1):
            g[i] = g[i-1] + g[i-2]
        return g[n]
            
        