# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        def construct_paths(root, path):
            if root == None:
                return
            path+=str(root.val)
            if root.left == None and root.right == None:
                paths.append(path)
            else:
                path+='->'
                construct_paths(root.left,path)
                construct_paths(root.right,path)
        
    
    
        paths = []
        construct_paths(root,'')
        return paths
    
        