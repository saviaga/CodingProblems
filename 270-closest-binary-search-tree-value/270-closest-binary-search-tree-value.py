# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        
        if root == None:
            return
        
        closest = root.val 
            
        while root:
            
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return closest
    
             
        
        