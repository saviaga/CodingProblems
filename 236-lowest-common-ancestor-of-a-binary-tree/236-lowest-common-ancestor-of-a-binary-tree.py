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
        
        dic_val = {root:None}
        

        while stack:
                curr = stack.pop()
                if curr.left:
                    stack.append(curr.left)
                    dic_val[curr.left]=curr
                if curr.right:
                    stack.append(curr.right)
                    dic_val[curr.right]=curr
        
        # Process all ancestors for node p using parent pointers.
        #start with p because a node can be its own ancestor
        p_ancestors = set()
        while p:
            p_ancestors.add(p)
            p=dic_val[p]
           
        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in p_ancestors:
            q=dic_val[q]
        
        return q
            

                  
            
                    
        
       
        
        
        