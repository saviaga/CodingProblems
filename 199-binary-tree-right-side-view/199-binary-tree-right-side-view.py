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
        
        queue = collections.deque([root])
        res = []
        
        
        while queue:
           
            done = False
            for _ in range(len(queue)):
                current = queue.popleft()
                if not done:
                    res.append(current.val)
                    done = True
                if current.right:
                    queue.append(current.right)
                if current.left:
                    queue.append(current.left)
            
        return res