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
        right_side = []
        node_dequeue =collections.deque([root])
        
        while node_dequeue:
            level = []
            for _ in range(len(node_dequeue)):
                current = node_dequeue.popleft()
                level.append(current.val)
                if current.left:
                    node_dequeue.append(current.left)
                if current.right:
                    node_dequeue.append(current.right)
            res.append(level[-1])
        return res
        
        