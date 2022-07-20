# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        current = root
        stack = []
        res = []
        cont = 0
        while current:
            stack.append(current)
            current = current.left
            
            while current == None and stack:
                current = stack.pop()
                k-=1
                if not k: 
                    return current.val
                current = current.right

        