# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root
        
        while curr:
            #if not left, go to right
            if curr.left==None:
                res.append(curr.val)
                curr = curr.right
            else: #if there is left tree
                predecessor = curr.left 
                while predecessor.right!=curr and predecessor.right!=None: #keep going to the right
                    predecessor = predecessor.right
                if  predecessor.right==None:
                    predecessor.right=curr
                    curr = curr.left
                else:
                    predecessor.right=None
                    res.append(curr.val)
                    curr = curr.right
        return res
                    
                
        