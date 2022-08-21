class Solution:
    def calculate(self, s: str) -> int:
        
        curr, prev, result = 0, 0, 0
        cur_operator =  '+'
        for i in range(len(s) + 1):
            if i < len(s):
                c = s[i]
            else:
                c = '+'

            if c == ' ': 
                continue
            if c.isdigit():
                curr = 10 * curr + int(c)
                continue

            if cur_operator == '+':
                result += prev
                prev = curr
            elif cur_operator == '-':
                result += prev
                prev = -curr
            elif cur_operator == '*':
                prev = prev * curr
            elif cur_operator == '/':
                prev = int(prev / curr)
            curr, cur_operator = 0, c
        return result + prev                
            
                
        