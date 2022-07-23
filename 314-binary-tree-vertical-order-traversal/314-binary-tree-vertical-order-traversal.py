# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return
        max_col = 0
        min_col = 0
        
        queue = collections.deque([(root,0)])
        all_levels = defaultdict(list)
        res = []
        
        while queue:
            
            for _ in range(len(queue)):
                curr,col = queue.popleft()
                max_col = max(max_col,col)
                min_col = min(min_col,col)
                all_levels[col].append(curr.val)
                if curr.left:
                    queue.append((curr.left,col-1))
                if curr.right:
                    queue.append((curr.right,col+1))
        
        for i in range(min_col,max_col+1):
            res.append(all_levels[i])
        return res
                                 
                
                                 
                
        