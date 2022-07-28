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
        
        stack = [(root,False)]
        diameter = 0
        heights = {}
        
        while stack:
            curr,visited = stack.pop()
            
            if visited:
                hleft = heights.get(curr.left, 0)
                hright = heights.get(curr.right,0)
                
                diameter = max(diameter,hleft+hright)
                
                heights[curr] = max(hleft,hright)+1
            else:
                stack.append((curr,True))
                if curr.right:
                     stack.append((curr.right,False))
                if curr.left:
                     stack.append((curr.left,False))
        return diameter