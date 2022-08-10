class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic_map = {')':'(',']':'[','}':'{'}
        
        stack = []
        
        
        for elem in s:
            if elem == '(' or elem == '[' or elem == '{':
                stack.append(elem)
            elif elem in dic_map:
                if stack and stack[-1]==dic_map[elem]:
                    stack.pop()
                else:
                    return False
            
            
            
        if len(stack) ==0:
            return True
        else:
            return False