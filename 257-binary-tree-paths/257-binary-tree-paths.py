# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = [(root,str(root.val))]
        paths = []
        while stack:
            curr, path = stack.pop()
            if not curr.left and not curr.right:
                paths.append(path)
            if curr.left:
                stack.append((curr.left,path+"->"+str(curr.left.val)))
            if curr.right:
                stack.append((curr.right,path+"->"+str(curr.right.val)))
        return paths
        