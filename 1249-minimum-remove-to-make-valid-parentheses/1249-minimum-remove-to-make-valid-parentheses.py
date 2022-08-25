class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        s= list(s)
        res = []
        open_par = 0
        #first pass append ( and pop it when ) if open parenteis are in stack
        for i  in range(len(s)):
            if s[i] =='(':
                open_par+=1
            elif s[i]==')':
                if open_par>0:
                    open_par-=1
                else:
                    s[i]='X'
        
        
        for i in reversed(range(len(s))):
                if s[i]=='(' and open_par>0:
                    s[i]='X'
                    open_par-=1
                    
        
        for elem in s:
            if elem!='X':
                res.append(elem)
        
        return "".join(res)
        