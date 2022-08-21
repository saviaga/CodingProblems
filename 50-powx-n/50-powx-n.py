class Solution:
    def myPow(self, x: float, n: int) -> float:
   
        
        def helper(x,n):
            if x==0: return 0
            if n==0: return 1
            
            res = helper(x*x,n//2)
            
            if n%2==1:
                return res*x
            else:
                return res
            
    
        if n>0: 
            return helper(x,n)
        else:
            return helper(1/x,-n)    
        