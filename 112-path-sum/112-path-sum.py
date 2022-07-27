# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        stack = [(root,targetSum-root.val)]
        
        
        while stack:
            curr,cum_sum = stack.pop()
            
            if not curr.left and not curr.right and cum_sum == 0:
                return True
            
            if curr.right:
                stack.append((curr.right, cum_sum-curr.right.val))
            if curr.left:
                stack.append((curr.left,cum_sum-curr.left.val))
            
        return False
        