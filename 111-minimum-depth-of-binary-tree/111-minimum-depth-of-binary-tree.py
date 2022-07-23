# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0
        
        queue = collections.deque([(root,1)])
        min_depth = 0
        
        while queue:
           
            for _ in range(len(queue)):
                curr, depth = queue.popleft()
                if not curr.left  and not curr.right:
                    return depth
                if curr.left:
                    queue.append([curr.left,depth+1])
                if curr.right:
                    queue.append([curr.right,depth+1])