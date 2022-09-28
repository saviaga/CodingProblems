class Solution:
    def myPow(self, x, n):

        if n< 0:
            x = 1/x
            n = abs(n)
            
        res = 1 
        while n>0:
            if n%2==1:
                res = res*x
            x=x*x
            n=n//2
           
        
        return res
        
       
      
        


            