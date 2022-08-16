class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path_list = path.split('/')
        
        for elem in path_list:
            if elem == '..':
                if stack:
                    stack.pop()
            elif elem=='.' or elem=='':
                continue
            else:
                stack.append(elem)
        return '/' + '/'.join(stack)
        
        
                    
                
                
                    
        