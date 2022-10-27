# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
            
        curr = root
        
        while curr:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    return root
            elif val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    return root
        return TreeNode(val)
        
        