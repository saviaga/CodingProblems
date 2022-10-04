class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        dic_parenthesis = {']':'[',')':'(','}':'{'}
        
        stack = []
        for i in range(len(s)):
            ch = s[i]
            if ch == '(' or ch=='{' or ch=='[':
                stack.append(ch)
            elif stack and stack[-1] == dic_parenthesis[ch]:
                stack.pop()
            else:
                return False
        return len(stack)==0
        