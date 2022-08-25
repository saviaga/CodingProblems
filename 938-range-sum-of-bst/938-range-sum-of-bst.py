# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        
        stack=[root]
        total=0
        while stack:
            curr=stack.pop()
            if low <= curr.val <=high:
                total+=curr.val
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return total
                
        