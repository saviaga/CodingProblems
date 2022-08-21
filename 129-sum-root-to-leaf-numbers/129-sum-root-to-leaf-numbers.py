# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return
        
        res=[]
        stack = [[root,False,str(root.val),False]] #node,visited,valpath,isleaf
        total=0
        while stack:
            curr,visited,path,isleaf = stack.pop()
            
            if visited:
                if isleaf:
                    res.append(path)
            else:
                
                isleaf = True if not curr.left and not curr.right else False
                stack.append([curr,True,path,isleaf])
                
                if curr.right:
                    temp1=path+str(curr.right.val)
                    stack.append([curr.right,False,temp1,isleaf])
                if curr.left:
                    temp2=path+str(curr.left.val)
                    stack.append([curr.left,False,temp2,isleaf])
        
        for elem in res:
            total+=int(elem)
        return total
            
        