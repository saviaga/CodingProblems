# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return
        stack  = []
        curr = root
        res = []
        
        while curr:
            stack.append(curr)
            curr = curr.left
            while curr==None and stack:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
        return res
            
        