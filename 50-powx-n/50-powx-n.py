class Solution:
    def myPow(self, x, n):
        if n<0:
            return 1/self.myPowHelp(x,abs(n))
        else:
            return self.myPowHelp(x,n)

    def myPowHelp(self,x,n):
            if n==0:return 1
            if x==0: return 0
            
            temp = self.myPowHelp(x,n//2)
            result = temp*temp
            if n%2==1:
                result= result*x
            return result
           
      
        


            