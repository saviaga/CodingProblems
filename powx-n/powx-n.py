class Solution:
    def myPow(self, x, n):

        def myPowHelp(x,n):
                if n==0:return 1

                temp = myPowHelp(x,n//2)
                
                if n%2==0:
                    return temp*temp
                else:
                    return temp*temp*x
        
        if n<0:
            return 1/myPowHelp(x,abs(n))
        else:
            return myPowHelp(x,n)

           
      
        


            