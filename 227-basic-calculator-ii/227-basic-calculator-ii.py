class Solution:
    def calculate(self, s: str) -> int:
        i=0
        cur, prev, res = 0, 0, 0
        cur_operator =  '+'
        
        while i<len(s):
            cur_char = s[i]
            
            if cur_char.isdigit():
                while i<len(s) and s[i].isdigit():
                    cur=cur*10+int(s[i])
                    i+=1
                i-=1
               
           
                if cur_operator == '+':
                    res += cur
                    prev = cur
                elif cur_operator == '-':
                    res -= cur
                    prev = -cur
                elif cur_operator == '*':
                    res -= prev
                    res += prev * cur
                    prev = cur * prev
                elif cur_operator == '/':
                    res -= prev
                    res += int(prev/cur)
                    prev = int(prev/cur)
                cur = 0
            elif cur_char!=" ":
                cur_operator = cur_char
            i+=1
        return res            
            
                
        