class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = list(s)
        stack = []
        final = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s[i]='X'
        
        while stack:
            idx = stack.pop()
            s[idx] = 'X'
                    
        for j in range(len(s)):
            if s[j]!='X':
                final.append(s[j])

        return "".join(final)            
                    
    
   