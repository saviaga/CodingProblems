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
        
        while current:                      #TO(N)  S#O(N)
            stack.append(current)
            current = current.left
            
            while current == None and stack:
                current = stack.pop()
                res.append(current.val)
                current = current.right
        
        heapq.heapify(res)  #O(N)
        
        for _ in range(k):   
            num = heappop(res)
        return num
        