# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return
        stack=[(root,False)]
        
        res = []
        
        while stack:
            curr,visited = stack.pop()
            if visited:
                res.append(curr.val)
            else:
                stack.append((curr,True))
                if curr.right:
                    stack.append((curr.right,False))
                if curr.left:
                    stack.append((curr.left,False))
        return res