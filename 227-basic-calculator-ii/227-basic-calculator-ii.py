class Solution:
    def calculate(self, s: str) -> int:
        
        cur_operator = '+'
        res = 0
        cur = 0
        i=0
        
        #grab the first number
        while i < len(s):
            cur = 0
            #process the first number which can contain several digits #324+24
            if s[i].isdigit():
                while i <len(s) and s[i].isdigit():
                    #0 *10 + 3  = 3
                    #3 *10 + 2  = 32
                    #32*10 + 4  = 324
                    cur = cur* 10 + int(s[i])
                    i+=1
                ##324+24
                #    ^  is gonna finish there so we need to go back one place to grab the operator at the last iteration. 
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
                
            elif s[i]!=" ":
                cur_operator = s[i]
            i+=1
        return res            
        