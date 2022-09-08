class Solution:
    def calculate(self, s: str) -> int:
        
        operator = '+'
        res = 0
        prev = 0
        i=0
        
        while i < len(s):
            curr = 0
            if s[i]!=' ' and not s[i].isdigit():
                operator = s[i]
            elif s[i].isdigit():
                #334
                #0*10 + 3 = 30
                #3*10 + 3 = 33
                #33*10 + 4 = 334
                while i<len(s) and s[i].isdigit():
                    curr=curr*10 + int(s[i])
                    i+=1
                #3+5
                # ^
                i-=1
                if operator=='+':
                    res+=curr
                    prev = curr
                elif operator=='-':
                    res-=curr
                    prev = -curr
                elif operator =='*':
                    res-=prev
                    res+= prev * curr
                    prev = prev * curr
                elif operator =='/':
                    res-=prev
                    res+= int(prev/curr)
                    prev = int(prev/curr)
            i+=1
        return res
                    
        