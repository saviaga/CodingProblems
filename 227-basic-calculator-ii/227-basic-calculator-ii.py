class Solution:
    def calculate(self, s: str) -> int:
        
        cur_operator = '+'
        res = 0
        cur = 0
        i=0
        
        #grab the first number
        while i < len(s):
            cur = 0
            if s[i]!=" " and not s[i].isdigit():
                cur_operator = s[i]
            #process the first number which can contain several digits #324+24
            elif s[i].isdigit():
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
                    res+= prev * cur
                    prev = prev * cur  # 4×20÷4 -> 80÷4, we need to save the result of prev*curr
                elif cur_operator == '/':
                    res-=prev
                    res+= int(prev/cur)
                    prev= int(prev/cur)  #30 ÷ 5 × 3	=	6 × 3
                   
                
            
            i+=1
        return res            
        