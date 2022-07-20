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
        current = root
        stack = []
        res = []
        
        while current:
            stack.append(current)
            current = current.left
            while current == None and stack:
                current=stack.pop()
                res.append(current.val)
                current= current.right
        return res