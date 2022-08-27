class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        
        res = deque()
        i=len(num1)-1
        j=len(num2)-1
        curr_sum = 0
        carry = 0
        while i>=0 or j>=0:
            
            curr_n1 = ord(num1[i]) - ord("0") if i>=0 else 0
            curr_n2 = ord(num2[j]) - ord("0") if j>=0 else 0
            
            curr_sum = carry + curr_n1 + curr_n2
            
            res.appendleft(str(curr_sum%10))
            carry = curr_sum//10
            
            i-=1
            j-=1
            
        if carry>0:
            res.appendleft(str(carry))
            
        return "".join(res)
        