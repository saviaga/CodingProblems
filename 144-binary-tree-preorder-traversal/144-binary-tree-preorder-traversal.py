# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return
        
        res = []
        nodes = [root]
        
        while nodes:
            current = nodes.pop()
            res.append(current.val)
            if current.right:
                nodes.append(current.right)
            if current.left:
                nodes.append(current.left)
        return res
    