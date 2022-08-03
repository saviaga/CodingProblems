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
        current = root
        
        while current:
            if val < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(val)
                    return root
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    return root
        return TreeNode(val)
            
    #Time complexity : O(H), where H is a tree height. That results in O(logN) in the average case, and O(N) in the worst case. Space O(1) since is constant space
            
       