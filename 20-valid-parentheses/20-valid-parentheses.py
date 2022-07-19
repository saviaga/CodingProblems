class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {")": "(", "]": '[',  "}": "{"}
        
        stack = []
        for elem in s:
                if elem in bracket_map:
                    if stack and stack[-1] == bracket_map[elem] :
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(elem)
                    
         # In the end, if the stack is empty, then we have a valid expression.
        return stack == []
    #Time complexity : O(n) because we simply traverse the given string one character at a time and push and pop operations on a stack take O(1) time.
    #Space complexity : O(n) as we push all opening brackets onto the stack and in the worst case, we will end up pushing all the brackets onto the stack. e.g. ((((((((((
            
                
                