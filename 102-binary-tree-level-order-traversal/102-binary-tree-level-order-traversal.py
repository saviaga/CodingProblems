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
        node_dequeue = collections.deque([root])
        
        while node_dequeue:
            level = []
            for _ in range(len(node_dequeue)):
                curr = node_dequeue.popleft()
                level.append(curr.val)
                if curr.left:
                    node_dequeue.append(curr.left)
                if curr.right:
                    node_dequeue.append(curr.right)
            res.append(level)
        return res
                    
        