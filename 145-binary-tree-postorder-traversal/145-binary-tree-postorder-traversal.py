# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return
        
        stack = [(root,False)]
        res = []
        
        while stack:
            current,visited = stack.pop()
            if visited:
                res.append(current.val)
                
            else:
                stack.append([current,True])
                if current.right:
                    stack.append([current.right,False])
                if current.left:
                    stack.append([current.left,False])
        return res