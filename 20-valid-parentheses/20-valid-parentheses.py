class Solution:
    def isValid(self, s: str) -> bool:
        
        dic_par = {')':'(',']':'[','}':'{'}
        stack = []
        for elem in s:
            if elem == '(' or elem == '[' or elem == '{':
                stack.append(elem)
            elif elem in dic_par:
                if stack and stack[-1] == dic_par[elem]:
                    stack.pop()
                else:
                    return False

        return stack==[]
                
                