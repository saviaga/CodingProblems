class Solution(object):
    
    
    def isHappyHelper(self, n):
        result = 0
        if n in self.res: return False
        if n==1:  return True
       
        self.res.add(n)
        while n > 0:
            digit = n%10
            n=n//10
            result += digit * digit
        
        return self.isHappyHelper(result)
        
    def isHappy(self, n):
        self.res = set()
        return self.isHappyHelper(n)
                
        