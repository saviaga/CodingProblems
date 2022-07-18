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
        nodes = [(root,False)]
        res = []
        
        while nodes:
            current,visited = nodes.pop()
            if visited:
                res.append(current.val)
                
            else:
                nodes.append([current,True])
                if current.right:
                    nodes.append([current.right,False])
                if current.left:
                    nodes.append([current.left,False])
        return res
                    
                    
            
        
        