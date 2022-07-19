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
        def closestValueHelper(root):
            if root == None:
                return
            
           
            if abs(root.val-target) < self.min_dif:
                self.min_dif = abs(root.val-target)
                self.value = root.val
            closestValueHelper(root.right)
            closestValueHelper(root.left)
        
        self.min_dif = float('inf')
        self.value = 0
        closestValueHelper(root)
        return self.value
        