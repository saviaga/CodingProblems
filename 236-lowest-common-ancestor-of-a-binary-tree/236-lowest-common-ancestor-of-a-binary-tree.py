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
        
        stack = [root]
        dic_ans = {root:None}
        LCAs = set()
        while p not in dic_ans or q not in dic_ans:
            curr = stack.pop()
            if curr.left:
                dic_ans[curr.left] = curr
                stack.append(curr.left)
            if curr.right:
                dic_ans[curr.right] = curr
                stack.append(curr.right)

        while p:
            LCAs.add(p)
            p = dic_ans[p]
            
        while q not in LCAs:
            q = dic_ans[q]
        return q
        
                