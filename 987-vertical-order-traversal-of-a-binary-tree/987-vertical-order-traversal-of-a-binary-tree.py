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
        res = defaultdict(list) #works as dict but defaultdict never raises a KeyError.
    
        all_levels = [] #works as dict but defaultdict never raises a KeyError.
        min_col = 0
        max_col = 0
        while queue:
            for _ in range(len(queue)):
                curr,row,col = queue.popleft()
                res[col].append((row,curr.val))
                min_col = min(min_col,col)
                max_col = max(max_col,col)
                
                if curr.left:
                    queue.append((curr.left,row+1,col-1))
                if curr.right:
                    queue.append((curr.right,row+1,col+1))
        for i in range(min_col,max_col+1):
                temp=[]
                if len(res[i])>1:
                    res[i].sort()
                    for elem in res[i]:
                        temp.append(elem[1])
                    all_levels.append(temp)  
                else:
                    all_levels.append([res[i][0][1]])
                
        return all_levels
            
        

            