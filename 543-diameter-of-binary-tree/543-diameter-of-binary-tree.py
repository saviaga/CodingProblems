# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def diameterOfBinaryTreeHelper(root):
            if root == None:
                return 0
            

            left =  diameterOfBinaryTreeHelper(root.left)
            right = diameterOfBinaryTreeHelper(root.right)
            
            self.diameter = max(self.diameter,left + right)
            
            return max(left,right) + 1    
    
        self.diameter = 0
        diameterOfBinaryTreeHelper(root)
        return self.diameter
        
        #Time complexity: O(N). This is because in our recursion function longestPath, we only enter and exit from each node once. We know this because each node is entered from its parent, and in a tree, nodes only have one parent.

#Space complexity: O(N). The space complexity depends on the size of our implicit call stack during our DFS, which relates to the height of the tree. In the worst case, the tree is skewed so the height of the tree is O(N)O(N). If the tree is balanced, it'd be O(\log N)O(logN).