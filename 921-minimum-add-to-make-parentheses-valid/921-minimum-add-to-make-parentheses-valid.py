class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        count=0
        stack = []
        for elem in s:
            if elem =='(':
                stack.append(elem)
            
            elif elem ==')':
                if stack and stack[-1] =='(':
                    stack.pop()
                else:
                    if stack:
                        stack.pop()
                    count+=1
        return count+len(stack)
                    
        