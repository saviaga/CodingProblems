# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root == None:
            return
        
        stack = [root]
        
        while stack:
            curr = stack.pop()
            if curr.val == val:
                return curr
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return None
        