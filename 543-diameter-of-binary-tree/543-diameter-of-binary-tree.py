# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    
    def height(self,root):
        if not root:
            return 0
        stack = [(0,root)]
        max_height = 0
        while stack:
            current_height, current_node = stack.pop()
            max_height = max(max_height,current_height)
            if current_node:
                stack.append((current_height+1,current_node.left))
                stack.append((current_height+1,current_node.right))
        return max_height
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return
        
        
        stack = [(root,0)]
        max_diam = 0
        max_height = 0
        while stack:
            cur_node, curr_diam = stack.pop()
            if cur_node.right:
                stack.append((cur_node.right,curr_diam+1))
            if cur_node.left:
                stack.append((cur_node.left,curr_diam+1))
            
            cur_height = self.height(cur_node.left)+self.height(cur_node.right)
            max_diam = max(max_diam,max(cur_height ,curr_diam))               
        return max_diam