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
        def diameterOfBinaryTreeHelper(node):
            
            if node == None:
                return 0
            
            #explore left and right
            left =  diameterOfBinaryTreeHelper(node.left)
            right = diameterOfBinaryTreeHelper(node.right)
            
            #update the max_diameter
            self.diameter = max(self.diameter,left + right)
            return max(left,right) + 1    
    
    
        self.diameter = 0
        diameterOfBinaryTreeHelper(root)
        return self.diameter
        
        
        