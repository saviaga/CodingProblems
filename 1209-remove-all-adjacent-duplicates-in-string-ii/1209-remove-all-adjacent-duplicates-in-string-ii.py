class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []  # [char, count]
        res = ''
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1 #increment the count of char [char,count+1]
            else:
                stack.append([c,1]) #append the char with value 1 (exists)
            
            if stack[-1][1] == k:
                stack.pop()
        for char,count in stack:
            res+= char*count
        
        return "".join(res)
        
                
                    
            
        