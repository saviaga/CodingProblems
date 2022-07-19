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
        
        current = root
        nodes = []

        sum_val = 0
        while current:
            nodes.append(current)
            current = current.left
            
            while current == None and nodes:
                current = nodes.pop()
               
                if current.val >= low  and current.val<= high:

                    sum_val+=current.val
                current = current.right
                
        return sum_val 
            
            
            