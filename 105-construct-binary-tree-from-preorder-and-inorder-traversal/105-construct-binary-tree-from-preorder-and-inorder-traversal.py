# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
       
        def array_to_tree(left,right):
            
            # if there are no elements to construct the tree
            if left > right: return None
            
            root_value = preorder[self.preorder_index]
            root = TreeNode(root_value)
            
            self.preorder_index +=1
            
            root.left = array_to_tree(left,inorder_index[root_value]-1 )
            root.right =  array_to_tree(inorder_index[root_value]+1,right)
            
            return root
        
        self.preorder_index = 0
        inorder_index = {}
        
        for index, value in enumerate(inorder):
            inorder_index[value] = index

        return array_to_tree(0, len(preorder) - 1)