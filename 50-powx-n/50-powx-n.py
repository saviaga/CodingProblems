class Solution:
    def myPow(self, x, n):

        def myPowHelp(x,n):
                if n==0:return 1

                temp = myPowHelp(x,n//2)
                result = temp*temp
                return result*x if n%2==1 else result 

        
        if n<0:
            return 1/myPowHelp(x,abs(n))
        else:
            return myPowHelp(x,n)

           
      
        


            