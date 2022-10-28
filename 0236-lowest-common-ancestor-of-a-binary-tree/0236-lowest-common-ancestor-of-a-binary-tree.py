# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        curr = root
        dic_ancestors = {root:None}
        stack = [root]
        
        
        while stack:
            curr = stack.pop()
            if curr.right:
                stack.append(curr.right)
                dic_ancestors[curr.right] = curr
                
            if curr.left:
                stack.append(curr.left)
                dic_ancestors[curr.left] = curr
        
        ancestors_p = set()
       
        while p:
            ancestors_p.add(p)
            p = dic_ancestors[p]
            
        while q not in ancestors_p:
            q = dic_ancestors[q]
        return q
                
            