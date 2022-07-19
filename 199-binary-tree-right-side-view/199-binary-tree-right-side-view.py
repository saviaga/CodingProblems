# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return
        
        res = []
        nodes = collections.deque([root])
        
        while nodes:
            level = []
            first = False
            for _ in range(len(nodes)):
                current = nodes.popleft()
                if not first:
                    res.append(current.val)
                    first = True
                
                if current.right:
                    nodes.append(current.right)
                if current.left:
                    nodes.append(current.left)
            
        return res