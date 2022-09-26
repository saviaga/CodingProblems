class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def fibHelp(n):
            if n <2:
                return n 
            
        
            
            self.fibo[n] = fibHelp(n-1) + fibHelp(n-2)
            return self.fibo[n]
       
        self.fibo = {0:0,1:1}

        return fibHelp(n)

        
        
            