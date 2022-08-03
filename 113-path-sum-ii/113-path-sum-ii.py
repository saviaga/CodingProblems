# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        
        result = []
        self.pathSumHelper(root,[],targetSum, result)
        return result
    
        
        
    def pathSumHelper(self,root,path, needsum,result):
        if not root:
            return 
        
        if not root.left and not root.right and needsum == root.val:
            path.append(root.val)
            result.append(path)
        self.pathSumHelper(root.left,path + [root.val],needsum - root.val,result)
        self.pathSumHelper(root.right,path + [root.val],needsum - root.val,result)
        
            
            
            
        
         
        
       
        
        
                
            
        