class Solution:
    def simplifyPath(self, path: str) -> str:
        
        
        stack = []
        s = path.split('/')
        for elem in s:
            if elem =='..':
                if stack:
                    stack.pop()
            elif elem =='.' or elem=='':
                continue
            else:
                stack.append(elem)
        
        return "/" + "/".join(stack)
           