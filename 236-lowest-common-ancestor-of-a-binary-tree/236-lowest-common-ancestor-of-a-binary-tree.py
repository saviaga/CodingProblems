# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #1.store all the prev parents in a dict
        
        stack = [root]
        dict_val = {root:None}
        
        while stack:
            curr = stack.pop()
            if curr.left:
                stack.append(curr.left)
                dict_val[curr.left]=curr
            if curr.right:
                stack.append(curr.right)
                dict_val[curr.right]=curr
        
        ancestors = set()
        while p:
            ancestors.add(p)
            p=dict_val[p] 
            
        while q not in ancestors:
            q = dict_val[q]
            
        return q
            
            

                  
            
                    
        
       
        
        
        