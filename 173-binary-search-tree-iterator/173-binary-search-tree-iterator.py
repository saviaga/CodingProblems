# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # Array containing all the nodes in the sorted order
        self.stack = []
        self.leftmost_inorder(root)
       
       
    def leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left
        

    def next(self):
        """
        :rtype: int
        """
        top_node = self.stack.pop()
        if top_node.right:
            self.leftmost_inorder(top_node.right)
        return top_node.val
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()