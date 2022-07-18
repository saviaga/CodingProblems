# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return 
        res = []
        nodes = collections.deque([root])
        
        while nodes:
            level = []
            for _ in range(len(nodes)):
                current = nodes.popleft()
                level.append(current.val)
                if current.left:
                    nodes.append(current.left)
                if current.right:
                    nodes.append(current.right)
            res.append(level)
        return res