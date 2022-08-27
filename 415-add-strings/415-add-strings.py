class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        
        
        res = deque()
        a = len(num1) - 1
        b = len(num2) - 1
        curr_sum = 0
        carry = 0
        curr_a,curr_b = 0,0
        
        while a>=0 or b>=0:
            #ord("1")->49 - ord("0")->48 just convert thhe string 1 to the correct integer number 1 
            curr_a = ord(num1[a]) - ord('0') if a>=0 else 0 #because if one number is bigger then indices would go to negative
            curr_b = ord(num2[b]) - ord('0') if b>=0 else 0
            
            curr_sum = carry + curr_a + curr_b 
            res.appendleft(str(curr_sum %10))
            carry = curr_sum //10
            a-=1
            b-=1
            
        if carry:
            res.appendleft(str(carry))
            
        return "".join(res)
            
            
           
            
        
        
       