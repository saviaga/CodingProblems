# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def check(self,p,q):
        if not p and not q:          
            return True
        
        if not p or not q:
            return False
         
        if p.val != q.val:
            return False
        return True
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        stack = [(p,q)]
        
        while stack:
            p,q = stack.pop()
            if not self.check(p,q):
                return False
            if p or q: 
                stack.append((p.left,q.left))
                stack.append((p.right,q.right))
            
        return True
        
        
        
      
        
            
        