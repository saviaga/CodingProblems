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
        parent_val = root.val
        
        p_val = p.val
        q_val = q.val
        
        #If both p and q are lesser than parent, then search in the right subtree
        if p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left,p,q)
        
        #If both p and q are greater than parent, then search in the left subtree
        elif p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right,p,q)
        
        # if p is in one side and q is in the other then the root is the lca
        else:
            return root
        
        
        