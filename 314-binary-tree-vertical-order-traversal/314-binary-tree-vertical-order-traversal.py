# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        min_col=0
        max_col=0
        if root ==None:
            return 
        
        queue = deque([(root,0)])
        
        res = defaultdict(list)
        min_col =0
        max_col = 0
        all_levels = []
        while queue:
            curr,col = queue.popleft()
            res[col].append(curr.val)
            min_col = min(min_col,col)
            max_col = max(max_col,col)
            if curr.left:
                queue.append((curr.left,col-1))
            if curr.right:
                queue.append((curr.right,col+1))
        
        for i in range(min_col,max_col+1):
            all_levels.append(res[i])
        return all_levels
        
        
            
            
            
        