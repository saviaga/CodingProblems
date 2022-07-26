# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return
        
        
        queue=collections.deque([[root,0]])
        res = defaultdict(list)
        min_col = 0
        max_col = 0
        all_levels = []
        while queue:
            for _ in range(len(queue)):
                curr,col = queue.popleft()
                min_col = min(min_col,col)
                max_col = max(max_col,col)
                res[col].append(curr.val)
                if curr.left:
                    queue.append([curr.left,col-1])
                if curr.right:
                    queue.append([curr.right,col+1])
        
        
        for i in range(min_col,max_col+1):
            all_levels.append(res[i])
            
        return all_levels
        
        
        