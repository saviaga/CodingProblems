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
        if root == None:
            return
        
        stack = [root]
        dic_ancestors = {root:None}
        LCA = set()

        
        # Iterate until we find both the nodes p and q
        #while p not in dic_ancestors or q not in dic_ancestors:
        while p not in dic_ancestors or q not in dic_ancestors:
                curr = stack.pop()
                if curr.right:
                    dic_ancestors[curr.right] = curr
                    stack.append(curr.right)
                if curr.left:
                    dic_ancestors[curr.left] = curr
                    stack.append(curr.left)
    
        # Process all ancestors for node p using parent pointers.
        

        while p:
            LCA.add(p)
            p = dic_ancestors[p]
            
        while q not in LCA:
            q = dic_ancestors[q]
        
        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        

            
        return q
        