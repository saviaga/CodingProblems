class Solution(object):
    
    
    def isHappyHelper(self, n):
        print(n)
        result = 0
        if n in self.res:
            return False
        if n=='1':
            return True
       
        self.res.append(n)
        for elem in n:
            result += int(elem)*int(elem)
        
        return self.isHappyHelper(str(result))
        
    def isHappy(self, n):
        self.res = []
        return self.isHappyHelper(str(n))
                
        