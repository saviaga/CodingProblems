class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic_map = {')':'(',']':'[','}':'{'}
        
        stack = []
        for elem in s:
            
            if elem in dic_map:
                if stack and stack[-1] == dic_map[elem]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(elem)
        return stack ==[]
    
    
                
        