class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x,n):
           
            if x==0: return 0
            if n==0: return 1
            
            temp = helper(x,n//2)
            result = temp*temp
            if n%2==1:
                result =result*x
            return result
            
        res = helper(x,abs(n))
        if n>0: 
            return res
        else:
            return 1/res
            
        