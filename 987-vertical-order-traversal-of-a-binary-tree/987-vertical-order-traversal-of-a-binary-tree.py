# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return
        
        queue = collections.deque([(root, 0, 0)]) #node, row, col
        res = []  #works as dict but defaultdict never raises a KeyError.
    
        all_levels = defaultdict(list)
        min_col = 0
        max_col = 0
        while queue:
            for _ in range(len(queue)):
                curr,row,col = queue.popleft()
                res.append((col,row,curr.val,))
                min_col = min(min_col,col)
                max_col = max(max_col,col)
                
                if curr.left:
                    queue.append((curr.left,row+1,col-1))
                if curr.right:
                    queue.append((curr.right,row+1,col+1))
                    
        res.sort()

        
        for col,row,val in res:
              
                all_levels[col].append(val)
        
        return all_levels.values()
            
        

            