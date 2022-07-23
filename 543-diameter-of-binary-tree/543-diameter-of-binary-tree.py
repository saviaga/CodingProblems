# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def diameterOfBinaryTreeHelper(root):
            if root == None:
                return 0
            
            
            left =  diameterOfBinaryTreeHelper(root.left)
            right = diameterOfBinaryTreeHelper(root.right)
            
            self.diameter = max(self.diameter,left + right)
            
            return max(left,right) + 1    
    
    
        self.diameter = 0
        diameterOfBinaryTreeHelper(root)
        return self.diameter
        
        