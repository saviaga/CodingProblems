class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        
        
        res = []
        a = len(num1) - 1
        b = len(num2) - 1
        curr_sum = 0
        carry = 0
        curr_a,curr_b = 0,0
        
        while a>=0 or b>=0:
            curr_a = ord(num1[a]) - ord('0') if a>=0 else 0
            curr_b = ord(num2[b]) - ord('0') if b>=0 else 0
            
            curr_sum = carry + curr_a + curr_b 
            res.append(str(curr_sum %10))
            carry = curr_sum //10
            a-=1
            b-=1
            
        if carry:
            res.append(str(carry))
            
        return "".join(reversed(res))
            
            
           
            
        
        
       