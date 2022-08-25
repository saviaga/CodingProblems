class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        s= list(s)
      
        stack = []
        #first pass append ( and pop it when ) if open parenteis are in stack
        for i  in range(len(s)):
            if s[i] =='(':
                stack.append(i)
            elif s[i]==')':
                if stack:
                    stack.pop()
                else:
                    s[i]='X'
        
        
        while stack:
                idx = stack.pop()
                s[idx]='X'
        
        for elem in s:
            if elem!='X':
                stack.append(elem)
        
        return "".join(stack)
        