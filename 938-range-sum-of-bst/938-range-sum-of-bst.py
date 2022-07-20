# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        nodes = [root]
        res = 0
        
        while nodes:
            current = nodes.pop()
            if current.val >= low and current.val <= high:
                res+=current.val
            if current.right:
                nodes.append(current.right)
            if current.left:
                nodes.append(current.left)
        return res
            
        