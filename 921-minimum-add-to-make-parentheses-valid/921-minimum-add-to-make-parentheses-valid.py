class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        
        stack = []
        for elem in s:
            if elem =='(': 
                stack.append(elem)
            else:
                if stack and stack[-1] =='(': 
                    stack.pop()
                else:
                    stack.append(elem)
        return len(stack)
                    
        