class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        need_c = 0
        open_p = 0
        
        for p in s:
            if p=='(':
                open_p+=1
            elif p==')':
                if open_p>0:
                    open_p-=1
                else:
                    need_c+=1
        return open_p+need_c