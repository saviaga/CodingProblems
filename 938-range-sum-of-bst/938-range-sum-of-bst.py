# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        if root == None:
            return
        
        res = []
        sum_nodes = 0
        nodes = [root]
        
        while nodes:
            current = nodes.pop()
            res.append(current.val)
            if current.left:
                nodes.append(current.left)
            if current.right:
                nodes.append(current.right)
        
        for elem in res:
            if elem >=low and elem <=high:
                sum_nodes+=elem
        return sum_nodes
        
        