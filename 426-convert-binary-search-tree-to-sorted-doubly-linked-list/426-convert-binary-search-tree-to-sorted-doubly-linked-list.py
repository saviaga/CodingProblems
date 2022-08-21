"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root==None:
            return None
        
        self.first=None
        self.last=None
        
        self.inorder_helper(root)
        
        self.first.left = self.last
        self.last.right = self.first
        
        return self.first
    
    def inorder_helper(self,node):
        if node :
            self.inorder_helper(node.left)
        
            if not self.last:
                self.first = node
            else:
                node.left = self.last
                self.last.right = node
                
            self.last = node
            self.inorder_helper(node.right)
        
        
        