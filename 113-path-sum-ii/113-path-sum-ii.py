# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        stack = [[root,[str(root.val)],targetSum-root.val]]
        res = []
        while stack:
            curr, currpath, currsum = stack.pop()
           
            if not curr.left and not curr.right and currsum == 0:
                res.append(currpath)
            if curr.right:
                stack.append([curr.right,currpath + [curr.right.val], currsum - curr.right.val])
            if curr.left:
                stack.append([curr.left,currpath + [curr.left.val], currsum - curr.left.val])
        return res
            
       
        
        
                
            
        