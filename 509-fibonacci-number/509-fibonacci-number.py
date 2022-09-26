class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        #memoization bottom up
        if n <2:
                return n
        fibo = {0:0,1:1}       
              
        for i in range(2,n+1):
                fibo[i] = fibo[i-1]+fibo[i-2]
        
        return fibo[n]
                
        
        
            