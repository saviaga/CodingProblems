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
        def pathSumHelper(root,path, needsum):
            if not root:
                return 

            if not root.left and not root.right and needsum == root.val:
                path.append(root.val)
                result.append(path)
            pathSumHelper(root.left,path + [root.val],needsum - root.val)
            pathSumHelper(root.right,path + [root.val],needsum - root.val)
        
        result = []
        pathSumHelper(root,[],targetSum)
        return result
    
        
        
   
        
            
            
            
        
         
        
       
        
        
                
            
        