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
        if root == None:
            return
        queue = collections.deque([root])
        
        res = [] 
        
        while queue:
            
            for _ in range(len(queue)):
                current = queue.popleft()
                
                current.left,current.right = current.right,current.left
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
        return root
        
        #Since each node in the tree is visited / added to the queue only once, the time complexity is O(n), where nn is the number of nodes in the tree.

#Space complexity is O(n), since in the worst case, the queue will contain all nodes in one level of the binary tree. For a full binary tree, the leaf level has n/2 = 0(n) leaves.