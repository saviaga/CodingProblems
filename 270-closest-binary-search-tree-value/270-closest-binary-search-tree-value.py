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
            
            self.ans.append(root.val)
            closestValueHelper(root.right)
            closestValueHelper(root.left)
        
        
        
        
        self.ans = []
        min_dif = float('inf')
        value = 0
        closestValueHelper(root)
        for elem in self.ans:
            if abs(elem-target) < min_dif:
                    min_dif = abs(elem-target)
                    value = elem
            
        return value
        