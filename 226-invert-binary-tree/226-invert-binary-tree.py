# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
    
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #base case
        if root == None:
            return
        
        #invert
        right =self.invertTree(root.right)
        left = self.invertTree(root.left)
        
        #swap children
        root.left = right
        root.right = left
        
        return root
        #iterative
        #Since each node in the tree is visited / added to the queue only once, the time complexity is O(n), where nn is the number of nodes in the tree.

#Space complexity is O(n), since in the worst case, the queue will contain all nodes in one level of the binary tree. For a full binary tree, the leaf level has n/2 = 0(n) leaves.

        #recursion
    # space is the number of recursive calls 
    #Because of recursion, O(h) function calls will be placed on the stack in the worst case, where h is the height of the tree. Because h∈O(n), the space complexity is O(n).