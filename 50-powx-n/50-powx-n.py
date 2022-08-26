class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        def myPowHelper(a,b):
            if b==0: return 1
           
            temp = myPowHelper(a,b//2)
            
            if b%2==0:
                result= temp*temp
            else:
                 result= temp*temp*a
            return result
            
        if n<0:
            x=1/x
            n=-n
       
        return myPowHelper(x,n)
            
        
        
            
        