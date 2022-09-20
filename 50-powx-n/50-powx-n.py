class Solution:
    def myPow(self, x, n):

        def myPowHelp(x,n):
                if n==0:return 1
                if x==0: return 0

                temp = myPowHelp(x,n//2)
                result = temp*temp
                if n%2==1:
                    result= result*x
                return result
        
        if n<0:
            return 1/myPowHelp(x,abs(n))
        else:
            return myPowHelp(x,n)

           
      
        


            